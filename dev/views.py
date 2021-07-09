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
from django.core.mail import send_mail
from django.conf import settings
from dotenv import dotenv_values
from pytz import timezone
from dateutil.parser import parse
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache

# Create your views here.
# 
# headers = {"Authorization": "Bearer ya29.a0AfH6SMDocF56q1ihTzPj98e2gezJ8Gp0pS1CrxkgQGMv6ZJlq7gd9_ypLYutSOvnhuRp7A3eXfDhCtOZFbsC0QwOW1myw2PJdsGa6UhZ5RR-1ONxGCCSQBASuqVX5kIxOsKRh-ZsOalcg4pPNGFUGnTjbcy7"}

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
def deV(request):
    print("tm to bta from where coming &&&&&&&&&")
    msg =''
    if request.method == 'POST':
        res= request.POST
        if res['type'] == 'data':
            obj = dev(topic=res['topic'] , session=res['session'] , resource=res['resource'])
            obj.save()
        # elif res['type'] == 'doc':
        #     file = request.FILES.get('name' , False)
        #     print(res , file)
        #     file_name = str(file)
        #     infile = request.FILES["name"].read()
        #     para = {
        #     "name": str(file_name),
        #     "parents":["1si7zP4RQa5Lhy0JbEZkgP6ubjGOTrRlK"]
        #     }
        #     files = {
        #         'data': ('metadata',json.dumps(para), 'application/json; charset=UTF-8'),
        #         'file':infile
        #     }
        #     print(type(files))
        #     token = get_access_token()
        #     token = "Bearer "+token
        #     headers = {"Authorization": token}
        #     r = requests.post(
        #         "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        #         headers=headers,
        #         files=files
        #     )
        #     refresh = requests.get('https://iiitkalyani.herokuapp.com/updatecache/1si7zP4RQa5Lhy0JbEZkgP6ubjGOTrRlK')
        #     print(r.text)
        else:
            name = res['name']
            name+=" Made Query"
            body = "My Mail Id : " + res['email']+"\n"
            body+= res['description']
            send_mail(name, body,settings.EMAIL_HOST_USER,['iiitk660@gmail.com'], fail_silently = False)
            obj  = details(name=res['name'] , email = res['email'] , description = res['description'] , date= datetime.datetime.now().date())
            obj.save()
            msg='Thanks for Submitting Query'
    # refresh = requests.get('https://iiitkalyani.herokuapp.com/updatecache/1si7zP4RQa5Lhy0JbEZkgP6ubjGOTrRlK')
    # book = requests.get('https://iiitkalyani.herokuapp.com/getfiles/1si7zP4RQa5Lhy0JbEZkgP6ubjGOTrRlK').json()
    book = DevBooks.objects.all()
    obj = dev.objects.all()
    noti = notification.objects.all()
    notific = ""
    if len(noti) > 0:
        notific  = noti[0].notify
    resource = []
    for objects in obj:
        resource.append(objects.resource.split(','))
    context={
            'book':book,
            'msg':msg,
            'alldata':zip(resource , obj),
            'notification':notific,
        }
    return render(request , 'dev.html' , context = context)


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
    

def addDevRecord(request):
    if request.method == 'POST':
        res = request.POST
        name = res['name']
        url = res['url']
        add_book = DevBooks(book_name = name , view_down = url)
        add_book.save()
        return HttpResponseRedirect('/dev')
    print(settings.BASE_DIR, "^^^^^^^^")
    return render(request , settings.BASE_DIR+'/cp/templates/addotherRecord.html')
