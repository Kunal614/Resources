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
from dotenv import dotenv_values
from pytz import timezone
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache


# def get_access_token():
#     config = dotenv_values("./.env")
#     print(config , "^^^^^^^^^^^^^")
#     token_obj = tokenStuff.objects.all()
    
#     if len(token_obj) == 0:
#         url = 'https://oauth2.googleapis.com/token'
#         data = {
#             "client_id": config['CLIENT_ID'],
#             "client_secret": config['CLIENT_SECRET'],
#             "refresh_token": config['REFRESH_TOKEN'],
#             "grant_type": "refresh_token"
#         }
#         res  = requests.post(url ,  data=data)
#         print(res , "&&&&&&&&&&&&&&&&&")
#         obj = tokenStuff(access_token = res.json()['access_token'] , time = datetime.datetime.now() , expires_in = res.json()['expires_in'])
#         obj.save()
#         return res.json()['access_token']
#     token_obj = token_obj[0]
#     access_token = token_obj.access_token
#     token_time = token_obj.time
    
#     y = parse(str(token_time))

#     t1 = y.astimezone(timezone('Asia/Kolkata'))

#     print(token_time , "CDDDDDDDDDDDd", datetime.datetime.now().time())
#     t1 = t1.replace(microsecond=0)
#     t1 = t1.replace(tzinfo=None)
#     print(t1 , y  , "%%%%%%%%%%%%%%%%%%%%%%")
#     now = datetime.datetime.now().replace(microsecond=0)
#     print((now - t1).total_seconds(), token_obj.expires_in , "&&&&&&&&&&&&&&&&&&&&&&&")
#     if int((now - t1).total_seconds()) <= int(token_obj.expires_in): #by using old token
#         print("Alreay exist ^^^^^^^^^^^^^^^^")
#         return access_token
#     else:
#         url = 'https://oauth2.googleapis.com/token'
#         data = {
#             "client_id": config['CLIENT_ID'],
#             "client_secret": config['CLIENT_SECRET'],
#             "refresh_token": config['REFRESH_TOKEN'],
#             "grant_type": "refresh_token"
#         }
#         res  = requests.post(url ,  data=data)
#         print(res , "&&&&&&&&&&&&&&&&&")
#         obj = tokenStuff.objects.all()[0]
#         obj.time = datetime.datetime.now()
#         obj.expires_in = res.json()['expires_in']
#         obj.access_token = res.json()['access_token']
#         obj.save()
#         return res.json()['access_token']
def cse(request):
    msg = ''
    noti = notification.objects.all()
    notific = ""
    if len(noti) > 0:
        notific  = noti[0].notify
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
                'sem2':sem2,
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
    return render(request , 'dashboard.html' , {'msg':msg , 'notification':notific})



# CACHE_TTL = getattr(settings , 'CACHE_TTL' , DEFAULT_TIMEOUT)
# @cache_page(CACHE_TTL)
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
    semes = res
    print(semes , "YE loooooooo baccha")
    # if cache.get(semes):
    #     print("Used redis cache ^^^^^^^^^^^^^^^^^^^")
    #     res = cache.get(semes)
    # else:
    res = semester.objects.filter(sem=res)
    # cache.set(semes , res)
    # print("USED DATABASE")
    # print(res , "%%%%%%%%%%%%%%%%%")
    sub = ''
    name = ''
    if len(res) > 0:
        sub = str(res[0].subjects).split(',')
        name = res[0].sem
    

    return render(request , 'sem.html' , {'msg':msg , 'sub':sub , 'name':semes})


def sub(request):
    msg = ''
    if request.method == 'POST':
        res = request.POST
        print(res)
        if res['type'] == 'doc':
            pass
            # file = request.FILES.get('name' , False)
            # print(res , file)
            # file_name = str(file)
            # infile = request.FILES["name"].read()
            # subj = res['subject']
            # subj = subject.objects.filter(name=subj)[0]
            # book = subj.book
            # other = subj.other
            # if res['doc'] == 'books':
            #     para = {
            #     "name": str(file_name),
            #     "parents":[book]
            #     }
            # else: 
            #     para = {
            #     "name": str(file_name),
            #     "parents":[other]
            #     }   
            # print(type(para))
            # files = {
            #     'data': ('metadata',json.dumps(para), 'application/json; charset=UTF-8'),
            #     'file':infile
            # }
            # token = get_access_token()
            # token = "Bearer "+token
            # headers = {"Authorization": token}
            # print(type(files))
            # r = requests.post(
            #     "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            #     headers=headers,
            #     files=files
            # )
            # refresh = requests.get('https://iiitkalyani.herokuapp.com/updatecache/'+book)
            # refresh = requests.get('https://iiitkalyani.herokuapp.com/updatecache/'+other)

            # print(r.text)
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
    # print(msg)
    sub = subject.objects.filter(name=subj)
    if len(sub) == 0:
        subj = subject(name = subj) 
        subj.save()
        subj = subject.objects.filter(name=sub)[0]
    else:
        subj = sub[0]
    print(subj.id , "Mai hu Id ")
    book = Books.objects.filter(subj = subj)
    print(book)
    other  = Other_stuff.objects.filter(subj = subj)
    # books = subj.book
    # others = subj.other
    
    '''
    print(books , others , "cdcjkndfc^^^^^^^^^^^^^^^^^^^^^^")
    book = {}
    copy = {}
    if books != None:
        book = requests.get('https://iiitkalyani.herokuapp.com/getfiles/'+books).json()
        # refresh = requests.get('https://iiitkalyani.herokuapp.com/updatecache/'+books)
    if others != None:
        copy = requests.get('https://iiitkalyani.herokuapp.com/getfiles/'+others).json()
        # refresh = requests.get('https://iiitkalyani.herokuapp.com/updatecache/'+others)
    
    print(book , copy)
    '''
    context={
            'book':book,
            'other':other,
            'msg':msg,
            'subject':res['subject']
        }
    
    return render(request , 'docs.html' , context=context)


def addCseRecord(request):
    if request.method == 'POST':
        res = request.POST
        subj = res['subject']
        name = res['name']
        url = res['url']
        if res['type'] == 'Book':
            add_book = Books(subj = subj , book_name = name , down_view = url)
            add_book.save()
        else:
            add_other = Other_stuff(subj = subj , other_name = name , view_down = url)
            add_other.save()
        return HttpResponseRedirect('/cse')
    res = request.GET
    subj = res['subject']
    ty = res['type']
    return render(request , 'addRecord.html' , {'subject':subj , 'type':ty})
