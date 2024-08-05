import os
from typing import List
from groq import Groq
from .models import ChatMessage
from django.contrib.auth.models import User
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
