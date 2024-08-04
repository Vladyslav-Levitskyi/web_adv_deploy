from django.db import models
from django.contrib.auth.models import User


class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, default='user')

    def __str__(self):
        return f"{self.sender.username}: {self.text[:50]}"
