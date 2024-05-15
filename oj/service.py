import json
import time

import requests
def qoj_login(
        ojHost = ""
):
    request_host = ojHost + "api/login"
    profile_host = ojHost + "api/profile"
    headers = {
        "Cookie": "_ga=GA1.1.1668753489.1709641705; _gid=GA1.1.1023487727.1713970481; _gat=1; csrftoken=JGZOxKsiBSwycWeW2XkpdZSOjKELU3QdaQSjgDszpZ8Gv9rWjld78r9zoF2U1XBl; sessionid=jnyifqkyazadansmtuykbj939z7xbwxs; _ga_59QEB25NR7=GS1.1.1713970481.2.1.1713970519.0.0.0",

    }
    data = {
        "username":'admin',
        'password':'y1297616113',
    }
    r = requests.post(url = request_host, headers = headers, data = data)
    data = requests.get(headers = headers, url= profile_host)
    return data.text
def qoj_submit(
        ojHost = "",
        code= "",
        lang = "C++",
        pid = 1,
        headers = ""
):
    request_host = ojHost + "api/submission"
    data = {
        "problem_id":pid,
        "language":lang,
        "code":code,
    }

    res = requests.post(url=request_host, headers=headers, data=data)
    res = res.text
    res = json.loads(res)
    submission_id = res['data']['submission_id']
    return submission_id

def qoj_result( ojHost = "",submission_id= "", headers = ""):
    requesturl = ojHost + f'api/submission?id={submission_id}'
    r = requests.get(url=requesturl, headers=headers)
    return r.text

def qoj_problems(ojHost = "", headers = ""):
    url = ojHost + 'api/problem?paging=true&offset=0&limit=250&page=1'
    print(url)

    data = requests.get(url= url, headers=headers)
#     print(data)

    return data.text

def qoj_problem(ojHost = "", headers = "", pid=1):
    url = ojHost + f'api/problem?problem_id={pid}'
    data = requests.get(url= url, headers=headers)
    return data.text
    