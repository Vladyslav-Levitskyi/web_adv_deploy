from django.urls import path
from .views import chat_view
from .import views


urlpatterns = [
    path('', chat_view, name='chat'),
    path('clear/', views.clear_chat, name='clear_chat'),
]