from django.shortcuts import render, redirect
from .models import ChatMessage
from .forms import ChatForm
from .groq import get_groq_response


def chat_view(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['text']
            message = ChatMessage(sender="You", text=user_message)
            message.save()

            response_text = get_groq_response(user_message)
            response = ChatMessage(sender="Ai", text=response_text)
            response.save()
            return redirect('chat')
    else:
        form = ChatForm()

    messages = ChatMessage.objects.all().order_by('timestamp')
    return render(request, 'chat/chat.html', {'form': form, 'messages': messages})


def clear_chat(request):
    if request.method == 'POST':
        ChatMessage.objects.all().delete()
        return redirect('chat')
    return render(request, 'chat/chat.html')