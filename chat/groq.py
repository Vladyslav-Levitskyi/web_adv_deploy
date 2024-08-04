import os
from typing import List
from groq import Groq
from .models import ChatMessage
import logging

groq = Groq()


def get_groq_response(content, chat_history):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    # Додайте повідомлення користувача до історії
    chat_history.append({"role": "user", "content": content})

    # Формування повідомлень для відправки
    messages_to_send = [
        {"role": "system", "content": "You always attempt the query."},
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


def load_chat_history(user: str) -> List[dict]:
    # Завантаження історії чату з бази даних
    messages = [
        {
            "role": "user" if message["sender"] == user else "assistant",  # Встановлюємо правильний role
            "content": message["text"]
        }
        for message in ChatMessage.objects.filter(sender=user).order_by("timestamp").values("sender", "text")
    ]
    
    # Логування отриманих повідомлень
    logging.debug(f"Loaded messages: {messages}")

    return messages  # Повертаємо прості словники


def save_chat_history(user: str, messages: List[dict]):
    for message in messages:
        if 'content' in message:
            logging.debug(f"Saving message: {message}")  # Логування збереження
            sender = user if message['role'] == 'user' else 'assistant'
            ChatMessage.objects.create(sender=sender, text=message["content"])
        else:
            raise KeyError('Message content is missing the key "content"')