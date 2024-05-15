import http.client
import json
from .models import Message
def user_conversation(user) : # 获取该用户的所有对话编号
    messages = Message.objects.filter(user=user)
    conversations = messages.values_list('conversation_id', flat=True).distinct()
    return conversations
def conversation_messages(conversation_id):
    messages = Message.objects.filter(conversation_id=conversation_id)
    return messages
def get_conversation_id():
    return Message.objects.count()
def chatResponse(
    role = 'user',
    temperature = 0.2,
    top_p = 0.2,
    stream = True,
    stop = 0 ,
    max_tokens = 100,
    content = "hello"
):
    conn = http.client.HTTPSConnection("api.chatanywhere.tech")
    payload = json.dumps({
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": role,
            "content": content
        }
    ]
    })
    headers = {
    'Authorization': 'Bearer sk-p0NCVMAcQOImqyGcfU9rpq7FYRdibbnlpo9B1avUSDrBv3zj',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/v1/chat/completions", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    return data
