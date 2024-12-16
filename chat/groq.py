import os
from typing import List
from groq import Groq
from .models import ChatMessage
from django.contrib.auth.models import User
from dotenv import load_dotenv
import logging

groq = Groq()
load_dotenv()

def get_groq_response(content, chat_history):
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )
    # Додайте повідомлення користувача до історії
    chat_history.append({"role": "user", "content": content})
    # Формування повідомлень для відправки
    messages_to_send = [
        {"role": "system", 
         "content": "You're a helpful, friendly assistant that always provides accurate and informative answers to any questions. Answer each question clearly and concisely, as if you're chatting with someone who wants straightforward information or assistance. If the question isn`t clear, ask for clarification. Remember to keep your tone polite, engaging, and approachable. If you don't understand the question, politely ask the user to clarify."
        },
        *chat_history
    ]
    
    chat_completion = client.chat.completions.create(
        messages=messages_to_send,
        model="llama3-70b-8192",
    )
    # Отримання відповіді асистента
    response_content = chat_completion.choices[0].message.content

    # Додайте відповідь асистента до історії
    chat_history.append({"role": "assistant", "content": response_content})

    return response_content

logger =  logging.getLogger(__name__)

def load_chat_history(username):
    user = User.objects.get(username=username)
    chat_messages = ChatMessage.objects.filter(sender=user).order_by('timestamp')
    return [{"role": message.role, "content": message.text} for message in chat_messages]


def save_chat_history(username, messages):
    user = User.objects.get(username=username)
    for message in messages:
        if not ChatMessage.objects.filter(sender=user, role=message["role"], text=message["content"]).exists():
            ChatMessage.objects.create(sender=user, role=message["role"], text=message["content"])
            logging.debug(f"Saved message: {message}")  # Логування збереження
        else:
            logging.debug(f"Message already exists, not saving: {message}")
