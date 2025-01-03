import os
from typing import List
from groq import Groq
from .models import ChatMessage
from django.contrib.auth.models import User
from dotenv import load_dotenv
import logging
from django.core.exceptions import ObjectDoesNotExist
import httpx


load_dotenv()


def get_groq_response(content, chat_history):
    try:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            logger.error("GROQ_API_KEY not found in environment variables")
            return "Configuration problem: API key is missing."

        # Створюємо власний HTTP клієнт без проксі
        http_client = httpx.Client(
            base_url="https://api.groq.com/v1",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30.0
        )
        
        # Ініціалізуємо Groq з нашим HTTP клієнтом
        client = Groq(
            api_key=api_key,
            http_client=http_client
        )
        
        # Adding users' messages to history
        chat_history.append({"role": "user", "content": content})
        messages_to_send = [
            {"role": "system", 
             "content": "You're a helpful, friendly assistant that always provides accurate and informative answers to any questions. Answer each question clearly and concisely, as if you're chatting with someone who wants straightforward information or assistance. If the question isn`t clear, ask for clarification. Remember to keep your tone polite, engaging, and approachable. If you don't understand the question, politely ask the user to clarify."
            },
            *chat_history
        ]
        
        try:
            chat_completion = client.chat.completions.create(
                messages=messages_to_send,
                model="llama3-70b-8192",
                temperature=0.7,
                max_tokens=1024
            )
            response_content = chat_completion.choices[0].message.content
            
            # Adding assistants' answer to history
            chat_history.append({"role": "assistant", "content": response_content})
            return response_content
            
        except Exception as e:
            logger.error(f"Error during Groq API call: {str(e)}")
            return f"Error API: {str(e)}"
            
    except Exception as e:
        logger.error(f"Unexpected error in get_groq_response: {str(e)}")
        return f"Unexpected error: {str(e)}"
    finally:
        if 'http_client' in locals():
            http_client.close()

logger =  logging.getLogger(__name__)

def load_chat_history(username):
    try:
        user = User.objects.get(username=username)
        chat_messages = ChatMessage.objects.filter(sender=user).order_by('timestamp')
        return [{"role": message.role, "content": message.text} for message in chat_messages]
    except ObjectDoesNotExist:
        logger.error(f"User not found: {username}")
        return []
    except Exception as e:
        logger.error(f"Error loading chat history: {str(e)}")
        return []


def save_chat_history(username, messages):
    try:
        user = User.objects.get(username=username)
        for message in messages:
            try:
                if not ChatMessage.objects.filter(
                    sender=user, 
                    role=message["role"], 
                    text=message["content"]
                ).exists():
                    ChatMessage.objects.create(
                        sender=user, 
                        role=message["role"], 
                        text=message["content"]
                    )
                    logger.debug(f"Saved message: {message}")
                else:
                    logger.debug(f"Message already exists, not saving: {message}")
            except Exception as e:
                logger.error(f"Error saving message: {str(e)}, message: {message}")
                
    except ObjectDoesNotExist:
        logger.error(f"User not found while saving chat history: {username}")
    except Exception as e:
        logger.error(f"Error in save_chat_history: {str(e)}")
