from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from .groq import get_groq_response, load_chat_history, save_chat_history

def chat_view(request):
    # Якщо користувач не авторизований, відобразіть повідомлення
    if not request.user.is_authenticated:
        return render(request, "chat/chat.html", {
            "messages": [],  # Можливо, ви хочете показати порожній чат
            "info": "Please log in to access the full chat functionality."
        })

    # Якщо користувач авторизований, обробляйте чат як зазвичай
    if request.method == "POST":
        user_message = request.POST.get("text", "").strip()  # Отримання тексту з форми
        if user_message:
            # Завантаження історії чату
            user_chat_history = load_chat_history(request.user.username)

            # Отримання відповіді від асистента
            assistant_response = get_groq_response(user_message, user_chat_history)

            # Збереження нового повідомлення
            new_messages = [
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": assistant_response}
            ]
            save_chat_history(request.user.username, new_messages)

            # Оновлена історія чату
            updated_chat_history = user_chat_history  # + new_messages

            # Рендеринг шаблону з новими повідомленнями
            return render(request, "chat/chat.html", {
                "messages": updated_chat_history,  # Об'єднуємо історію з новими повідомленнями
            })
        else:
            # Обробка випадку, коли повідомлення порожнє
            return render(request, "chat/chat.html", {
                "messages": load_chat_history(request.user.username),
                "error": "Message content is empty."
            })

    # Завантаження історії чату для GET запиту
    chat_history = load_chat_history(request.user.username)
    return render(request, "chat/chat.html", {"messages": chat_history})

@login_required
def clear_chat(request):
    if request.method == 'POST':
        # Видалення історії чату для конкретного користувача
        ChatMessage.objects.filter(sender=request.user).delete()
        return redirect('chat')
    return render(request, 'chat/chat.html')

