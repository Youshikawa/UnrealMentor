from django.core import serializers
from django.utils import timezone

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
import http.client
import json

from django.views.decorators.csrf import csrf_exempt

from .service import qoj_login, qoj_submit, qoj_result, qoj_problems, qoj_problem
from django.conf import settings
from .models import Submission
# Create your views here.

@csrf_exempt
def submit_problems(request):
    # print(2131312)
    r = qoj_login(ojHost= settings.JUDGEMENT_URLS)
    data = request.body
    data = data.decode('utf-8')
    data = json.loads(data)
    code = data.get('code')
    lang = data.get('lang')
    pid = data.get('pid')
    problem_name = data.get('title')
    problem_content = data.get("problem_description")
    print("-->deBUg", problem_name)
    if (settings.DEBUG == False) :user = request.user
    else: user = User.objects.filter(username = 'test01')[0]
    if not user.is_authenticated:
        return JsonResponse({
            "code":0,
        })
    submission_id = qoj_submit(code= code, lang= lang, pid= pid,ojHost= settings.JUDGEMENT_URLS, headers= settings.REQUEST_COOKIE)
    
    new_submission = Submission(
        user= user,
        submission_id= submission_id,
        problem_content=problem_content,
        problem_name=problem_name
    )
    new_submission.save()
    print(111111)
    return JsonResponse({
        "code":1,
        'submission_id':submission_id,
        "problem_name":problem_name,
        "problem_content":problem_content,
    })



@csrf_exempt
def submission_result(request):
    data = request.body
    data = data.decode('utf-8')
    data = json.loads(data)
    submission_id = data.get("submission_id")
    title = Submission.objects.filter(submission_id=submission_id)[0].problem_name
    problem_content = Submission.objects.filter(submission_id=submission_id)[0].problem_content
    res = qoj_result(submission_id= submission_id, headers= settings.REQUEST_COOKIE, ojHost= settings.JUDGEMENT_URLS)
    print(json.loads(res))
    return JsonResponse({
        'code':1,
        "data":json.loads(res),
        'problem_content':problem_content,
        'title':title,
    })

@csrf_exempt
def problem_list(request):

    data = qoj_problems(headers= settings.REQUEST_COOKIE, ojHost= settings.JUDGEMENT_URLS)
    data = json.loads(data)
    return JsonResponse({
        "code":1,
        "data":data.get('data').get("results")
    })
@csrf_exempt
def submission_list(request):
    L = Submission.objects.all()
    data = []
    for i in L:
        data.append({
            'submission_id':i.submission_id,
            'problem_name':i.problem_name,
            'user':i.user.username,
        })
    return JsonResponse({
        'code':1,
        'data':data,
    })

@csrf_exempt
def problem_details(request):
    data = request.body
    data = data.decode('utf-8')
    data = json.loads(data)
    pid = data.get('pid')
    data = qoj_problem(headers= settings.REQUEST_COOKIE, ojHost= settings.JUDGEMENT_URLS, pid = pid)
    data = json.loads(data)
    return JsonResponse({
        'code':1,
        'data':data.get('data')
    })