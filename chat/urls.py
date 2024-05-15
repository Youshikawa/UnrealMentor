from django.urls import path
from . import views

urlpatterns = [
    path('post_chat/', views.post_chat, name='post_chat'),
    path('history_chat/', views.history_conversations, name = 'history_chat'),
    path('conversation/', views.get_conversation, name = "get_conversation")
]