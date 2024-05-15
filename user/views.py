from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm, UserProfileForm
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from .models import UserProfile
import json
def check_pswd(pswd):
    ans = 1
    if len(pswd) < 8 :
        return False
    return True
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = request.body
        data = data.decode('utf-8')
        data = json.loads(data)
        username = data.get('username')
        password = data.get('password')
        print(username, password,end="\n\n\n\n\n\n\n")
        if User.objects.filter(username = username).exists():
            return JsonResponse({'res':'user exist', 'code':0})
        print(username, password, end = '\n\n')
        if check_pswd(password) == False:
            return JsonResponse({'res':'password error', 'code':0})
        user = User(username = username)
        user.set_password(password)
        
        user.save()
        name = data.get('name')
        if not data.get('name') : name='访客'
        UserProfile.objects.create(user = user, name = name)
        login(request, user)
        return JsonResponse({'res':'success', 'code':1})
        
@csrf_exempt
def get_status(request):
    user = request.user
    print(user)
    if not user.is_authenticated:
        print("111",user.username)
        return JsonResponse({'code':0})
    else :
        return JsonResponse({'code':1, 'username':user.username})
@csrf_exempt
def user_login(request):
    print(request)
    data = request.body
    data = data.decode('utf-8')
    print(data)
    data = json.loads(data)
    
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username = username, password = password)
    if not user :
        return JsonResponse({'res':'no such user', 'code':0})
    else :
        login(request, user)
        return JsonResponse({'res':'success', 'code':1})
@csrf_exempt
def user_logout(request):
    logout(request)
    return JsonResponse({'code':1})

def edit_profile(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})