from django.shortcuts import render
from django.shortcuts import redirect
import json
import requests
from django.contrib.auth.models import User 
from django.contrib.auth import login , authenticate , logout
from django.http import HttpResponseRedirect
from .models import dev
from django.http import HttpResponse
import datetime
from base.models import *
# Create your views here.
# 
# headers = {"Authorization": "Bearer ya29.a0AfH6SMDocF56q1ihTzPj98e2gezJ8Gp0pS1CrxkgQGMv6ZJlq7gd9_ypLYutSOvnhuRp7A3eXfDhCtOZFbsC0QwOW1myw2PJdsGa6UhZ5RR-1ONxGCCSQBASuqVX5kIxOsKRh-ZsOalcg4pPNGFUGnTjbcy7"}
def get_access_token():
    token_obj = tokenStuff.objects.all()[0]
    access_token = token_obj.access_token
    refresh_token = token_obj.refresh_token
    token_time = token_obj.time
    print(token_time , "CDDDDDDDDDDDd", datetime.datetime.now().time())
    comp_time = token_time.hour *60 + token_time.minute
    curr_time = datetime.datetime.now().time().hour *60 + datetime.datetime.now().time().minute
    curr_date = datetime.datetime.now().date()
    token_date = token_obj.date
    print(curr_time  , comp_time , curr_date == token_date  , "&&&&&&&&&&&&&&&&&&&&&&&")
    if curr_date == token_date and curr_time - comp_time <= 60: #by using old token
        return access_token
    else:
        url = 'https://oauth2.googleapis.com/token'
        data = {
            "client_id": "1091937598228-5aan4ts4lm6u28r38q29926b81jatcts.apps.googleusercontent.com",
            "client_secret": "ZkzCCfgnau4hEhaH__PYflke",
            "refresh_token": refresh_token,
            "grant_type": "refresh_token"
        }
        res  = requests.post(url ,  data=data)
        obj = tokenStuff.objects.all()[0]
        obj.time = datetime.datetime.now().time()
        obj.date = datetime.datetime.now().date()
        obj.access_token = res.json()['access_token']
        obj.save()
        return res.json()['access_token']
def deV(request):
    msg =''
    if request.method == 'POST':
        res= request.POST
        if res['type'] == 'data':
            obj = dev(topic=res['topic'] , session=res['session'] , resource=res['resource'])
            obj.save()
        elif res['type'] == 'doc':
            file = request.FILES.get('name' , False)
            print(res , file)
            file_name = str(file)
            infile = request.FILES["name"].read()
            para = {
            "name": str(file_name),
            "parents":["1Mf3RLjcdplr7r00R12Ep1AgGFGotnP8s"]
            }
            files = {
                'data': ('metadata',json.dumps(para), 'application/json; charset=UTF-8'),
                'file':infile
            }
            print(type(files))
            token = get_access_token()
            token = "Bearer "+token
            headers = {"Authorization": token}
            r = requests.post(
                "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                headers=headers,
                files=files
            )
            print(r.text)
        else:
            msg='Thanks for Submitting Query'
    # book = requests.get(' http://6cf7a3821881.ngrok.io/getfiles/1si7zP4RQa5Lhy0JbEZkgP6ubjGOTrRlK').json()
    # if len(book) > 0:
    #    context={
    # #         'book':book,
    # #         'msg':msg
    # #     }
    obj = dev.objects.all()
    resource = []
    for objects in obj:
        resource.append(objects.resource.split(','))
    return render(request , 'dev.html' , {'msg':msg , 'alldata':zip(resource , obj)})


def edit_dev(request , id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/dev')
    obj = dev.objects.get(id=id)
    if request.method == 'POST':
        res = request.POST
        
        obj.topic = res['topic']
        obj.session=res['session']
        obj.resource=res['resource']
        obj.save()
        return HttpResponseRedirect('/dev')
    
    return render(request , 'edit_dev.html' , {'obj':obj})
    