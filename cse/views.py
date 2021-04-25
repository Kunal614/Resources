from django.shortcuts import render
from django.shortcuts import redirect
import json
import requests
from django.contrib.auth.models import User 
from django.contrib.auth import login , authenticate , logout
from django.http import HttpResponseRedirect
from .models import *
from django.http import HttpResponse
import datetime
from base.models import *
from dateutil.parser import parse
from django.core.mail import send_mail
from django.conf import settings
# headers = {"Authorization": "Bearer ya29.a0AfH6SMCPUInnjHmPzT_vUgKYDt2g2cLivHp76eplwAuBktAE4arb5AEyhcAa-_Lan0pdw4XEgZ5vxPiQJ7ftPSscYJaePATyEbw5YROkPTrZnIQAf_twrsd9Y_31gPBMYJuMgitdJiXjkqwZm9WPT8LUZG0V"}

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
    if curr_date == token_date and curr_time - comp_time <= token_obj.expires_in: #by using old token
        print("Alreay exist ^^^^^^^^^^^^^^^^")
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
        obj.expires_in = res.json()['expires_in']/60
        obj.access_token = res.json()['access_token']
        obj.save()
        return res.json()['access_token']
def cse(request):
    msg = ''
    if request.method == 'POST':
        res = request.POST
        msg = ''
        if res['type'] == 'query':
            res = request.POST
            name = res['name']
            name+=" Made Query"
            body = "My Mail Id : " + res['email']+"\n"
            body+= res['description']
            send_mail(name, body,settings.EMAIL_HOST_USER,['iiitk660@gmail.com'], fail_silently = False)
            obj  = details(name=res['name'] , email = res['email'] , description = res['description'] , date= datetime.datetime.now().date())
            obj.save()
            msg='Thanks for Submitting Query'
            
        
        if res['year'] == 'first': 

            sem = ['1st' , '2nd']
            sem1 = 'first_sem'
            sem2 = 'second_sem'
            context ={
                'name':'first',
                'msg':msg,
                'sem':sem,
                'sem1':sem1,
                'sem2':sem2
            }
            return render(request , 'year.html' , context=context)
        elif res['year'] == 'second':
            sem = ['3rd' , '4th']
            sem1 = 'third_sem'
            sem2 = 'fourth_sem'
            context ={
                'name':'second',
                'msg':msg,
                'sem':sem,
                'sem1':sem1,
                'sem2':sem2
            }
            return render(request , 'year.html' , context=context)
        elif res['year'] == 'third':
            sem = ['5th' , '6th']
            sem1 = 'fifth_sem'
            sem2 = 'sixth_sem'
            context ={
                'name':'third',
                'msg':msg,
                'sem':sem,
                'sem1':sem1,
                'sem2':sem2
            }
            return render(request , 'year.html' , context=context)
        elif res['year'] == 'fourth':
            sem1 = 'seventh_sem'
            sem2 = 'eight_sem'
            sem = ['7th' , '8th']
            context ={
                'name':'fourth',
                'msg':msg,
                'sem':sem,
                'sem1':sem1,
                'sem2':sem2
            }
            return render(request , 'year.html' , context=context)
        else:
            return render(request , 'dashboard.html', {'msg':msg})
    return render(request , 'dashboard.html' , {'msg':msg})



def sem(request):
    msg = ''
    if request.method == 'POST':
        res = request.POST
        name = res['name']
        name+=" Made Query"
        body = "My Mail Id : " + res['email']+"\n"
        body+= res['description']
        send_mail(name, body,settings.EMAIL_HOST_USER,['iiitk660@gmail.com'], fail_silently = False)
        obj  = details(name=res['name'] , email = res['email'] , description = res['description'] , date= datetime.datetime.now().date())
        obj.save()
        msg='Thanks for Submitting Query'
        
        print(res)
    else:     
        res = request.GET
    res = res['semester']
    res = semester.objects.filter(sem=res)
    print(res , "%%%%%%%%%%%%%%%%%")
    sub = str(res[0].subjects).split(',')
    return render(request , 'sem.html' , {'msg':msg , 'sub':sub , 'name':res[0].sem})


def sub(request):
    msg = ''
    if request.method == 'POST':
        res = request.POST
        print(res)
        if res['type'] == 'doc':
            file = request.FILES.get('name' , False)
            print(res , file)
            file_name = str(file)
            infile = request.FILES["name"].read()
            subj = res['subject']
            subj = subject.objects.filter(name=subj)[0]
            book = subj.book
            other = subj.other
            if res['doc'] == 'books':
                para = {
                "name": str(file_name),
                "parents":[book]
                }
            else: 
                para = {
                "name": str(file_name),
                "parents":[other]
                }   
            print(type(para))
            files = {
                'data': ('metadata',json.dumps(para), 'application/json; charset=UTF-8'),
                'file':infile
            }
            token = get_access_token()
            token = "Bearer "+token
            headers = {"Authorization": token}
            print(type(files))
            r = requests.post(
                "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                headers=headers,
                files=files
            )
            print(r.text)
        else:
            name = res['name']
            name+=" Made Query"
            body = "My Mail Id : " + res['email']+"\n"
            body+= res['description']
            send_mail(name, body,settings.EMAIL_HOST_USER,['iiitk660@gmail.com'], fail_silently = False)
            obj  = details(name=res['name'] , email = res['email'] , description = res['description'] , date= datetime.datetime.now().date())
            obj.save()
           
            msg = "Thanks for submitting query"
    else:
        print(request.GET)
        res = request.GET
        subj = res['subject']

    #book
    print(msg)
    subj = subject.objects.filter(name=subj)[0]
    books = subj.book
    others = subj.other
   
    print(books , others , "cdcjkndfc^^^^^^^^^^^^^^^^^^^^^^")
    book = {}
    copy = {}
    if books != None:
        book = requests.get('https://iiitkalyani.herokuapp.com/getfiles/'+books).json()
    if others != None:
        copy = requests.get('https://iiitkalyani.herokuapp.com/getfiles/'+others).json()
    
    print(book , copy)
    context={
            'book':book,
            'copy':copy,
            'msg':msg,
            'subject':res['subject']
        }

    return render(request , 'docs.html' , context=context)

