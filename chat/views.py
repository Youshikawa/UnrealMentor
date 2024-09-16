from django.core import serializers
from django.utils import timezone

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
import http.client
import json

from django.views.decorators.csrf import csrf_exempt

from .service import chatResponse, conversation_messages, user_conversation
from .models import Message
from .service import get_conversation_id

def new_conversation(user, chat_text):
    conversation_id = get_conversation_id() + 1
    new_message = Message(
        content= chat_text,
        timestamp=timezone.now(),
        sender="user",  # 或者 "chatgpt"
        message_id= conversation_id,
        conversation_id= conversation_id,
        user=user # 使用实际的用户名
    )
    new_message.save()
    return conversation_id
@csrf_exempt
def get_conversation(request):
    data = request.body
    data = data.decode('utf-8')
    data = json.loads(data)
    conversation_id = data.get('conversation_id')
    messages = conversation_messages(conversation_id)
    res = []
    for i in messages:
        if i.sender == "user":
            res.append({"sender":"user", "text":i.content})
        else :
            res.append({"sender":"chatgpt", "text":i.content})
    return JsonResponse({
        "code":1,
        "data": res,
    })
def save_message(conversation_id, user, sender = "chatgpt", text = "") :
    message_id = get_conversation_id() + 1
    new_message = Message(
        content=text,
        timestamp=timezone.now(),
        sender= sender,  # 或者 "chatgpt"
        message_id=message_id,
        conversation_id=conversation_id,
        user=user  # 使用实际的用户名
    )
    new_message.save()

@csrf_exempt
def history_conversations(request):
    user = request.user
    # user = User.objects.filter(username='test01')[0]
    if not user.is_authenticated:
        return JsonResponse({
            'code':0,
        })

    conversations = user_conversation(user).order_by('-conversation_id')
    cnt = 0
    res = {}
    for i in conversations:
        if cnt < 10:
            cnt += 1
            res[i] = Message.objects.filter(conversation_id= i)[0].content
        else :
            break
    return JsonResponse({
        'code':1,
        'data': res
    })
def get_context(conversation_id, context_len = 5):
    messages = conversation_messages(conversation_id)
    res = "你是MentorGPT,是一个程序设计教学机器人哦！\n"
    if (len(messages) > context_len):

        for p in range(len(messages)):
            if ((len(messages)) - p > context_len) :continue
            i = messages[p]
            if i.sender == 'chatgpt':
                res += "ChatGPT:" + i.content + "\n"
            else:
                res += "User:"  + i.content + "\n"
    else :
        for i in messages:
            if i.sender == 'chatgpt':
                res += "ChatGPT:" + i.content + "\n"
            else:
                res += "User:"  + i.content + "\n"
    return res

@csrf_exempt
def post_chat(request):
    data = request.body
    data = data.decode('utf-8')
    data = json.loads(data)
    text = data.get('text')
    user = request.user
    # user = User.objects.filter(username="test01")[0]
    if not user.is_authenticated:
        return JsonResponse({
            'code': 0,

        })
    conversation_id = -1
    if not data.get("conversation_id") :
        conversation_id = new_conversation(user, text)
    else :
        conversation_id = data.get('conversation_id')
        new_message = Message(
            content=text,
            timestamp=timezone.now(),
            sender="user",  # 或者 "chatgpt"
            message_id= get_conversation_id() + 1,
            conversation_id=conversation_id,
            user=user # 使用实际的用户名
        )
        new_message.save()
    text = get_context(conversation_id) + text
    print(text)
    res = chatResponse(content=text)
    print(res)
    text = res.get("choices")[0].get('message').get('content')
    save_message(conversation_id = conversation_id,
                 user = user,
                 text = text
                 )
    return JsonResponse({
        'code':1,
        'conversation_id':conversation_id,
        'text':text,
        'context':get_context(conversation_id),
    })

