from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_histories', null=True)
    message = models.TextField()
    sender = models.CharField(max_length=10)  # Choices to distinguish sender
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat history for {self.user.username} at {self.timestamp}"
