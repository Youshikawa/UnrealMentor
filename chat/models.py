from django.contrib.auth.models import User
from django.db import models

class Message(models.Model):
    sender_choices = (
        ('user', 'User'),
        ('chatgpt', 'ChatGPT')
    )
    
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=10, choices=sender_choices)
    message_id = models.CharField(max_length=50)  # 消息编号
    conversation_id = models.CharField(max_length=50)  # 对话编号
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sender} - {self.content}'
