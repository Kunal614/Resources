from django.shortcuts import render
from django.shortcuts import redirect
import json
import requests
from django.contrib.auth.models import User 
from django.http import HttpResponseRedirect
from .models import *
from django.http import HttpResponse
from datetime import datetime


headers = {"Authorization": "Bearer ya29.a0AfH6SMDocF56q1ihTzPj98e2gezJ8Gp0pS1CrxkgQGMv6ZJlq7gd9_ypLYutSOvnhuRp7A3eXfDhCtOZFbsC0QwOW1myw2PJdsGa6UhZ5RR-1ONxGCCSQBASuqVX5kIxOsKRh-ZsOalcg4pPNGFUGnTjbcy7"}

def cP(request):
    msg= ''
    if request.method == 'POST':
        res = request.POST
        if res['type'] == 'data':
            obj = cp(title=res['title'] , data=res['data'] , question=res['question'])
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
            r = requests.post(
                "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                headers=headers,
                files=files
            )
            print(r.text)
        else:
            msg = 'Thanks For submitting Query'
    obj = cp.objects.all()
    title = []
    data = []
    question = []
    prblm = problemofday.objects.all()
    prblm = prblm[0].problem_of_the_day

    for objects in obj:
        title.append(objects.title)
        data.append(objects.data.split(','))
        question.append(objects.question.split(','))
    
    # book = requests.get(' http://6cf7a3821881.ngrok.io/getfiles/14MBVQyZ6NtKVFHCBJMVsNRWoWFWQpntD').json()
    # if len(book) > 0:
    #    context={
    # #         'book':book,
    # #         'msg':msg,
    #           'alldata':zip(title , data , question , obj),
    #           'prpblem':prblm,
     # #     }

    return render(request , 'cp.html' , {'alldata':zip(title , data , question , obj) , 'msg':msg , 'problem':prblm})


def edit(request , id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/cp')
    obj = cp.objects.get(id=id)
    if request.method == 'POST':
        res = request.POST
        
        obj.title = res['title']
        obj.data=res['data']
        obj.question=res['question']
        obj.save()
        return HttpResponseRedirect('/cp')
    
    return render(request , 'edit_cp.html' , {'obj':obj})
    

def problemsets(request):
    obj = problemset.objects.all()
    prblm = problemofday.objects.all()
    prblm = prblm[0].problem_of_the_day
    return render(request , 'problemset.html' , {'obj':obj , 'msg':'' , 'problem':prblm})
    

