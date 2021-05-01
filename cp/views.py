from django.shortcuts import render
from django.shortcuts import redirect
import json
import requests
from django.contrib.auth.models import User 
from django.http import HttpResponseRedirect
from .models import *
from base.models import *
from django.http import HttpResponse
# from datetime import datetime
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from pytz import timezone
from datetime import timezone as tz
import datetime
from django.conf import settings
from dateutil.parser import parse
from dotenv import dotenv_values


def get_access_token():
    config = dotenv_values("./.env")
    print(config , "^^^^^^^^^^^^^")
    token_obj = tokenStuff.objects.all()
    
    if len(token_obj) == 0:
        url = 'https://oauth2.googleapis.com/token'
        data = {
            "client_id": config['CLIENT_ID'],
            "client_secret": config['CLIENT_SECRET'],
            "refresh_token": config['REFRESH_TOKEN'],
            "grant_type": "refresh_token"
        }
        res  = requests.post(url ,  data=data)
        print(res , "&&&&&&&&&&&&&&&&&")
        obj = tokenStuff(access_token = res.json()['access_token'] , time = datetime.datetime.now() , expires_in = res.json()['expires_in'])
        obj.save()
        return res.json()['access_token']
    token_obj = token_obj[0]
    access_token = token_obj.access_token
    token_time = token_obj.time
    
    y = parse(str(token_time))

    t1 = y.astimezone(timezone('Asia/Kolkata'))

    print(token_time , "CDDDDDDDDDDDd", datetime.datetime.now().time())
    t1 = t1.replace(microsecond=0)
    t1 = t1.replace(tzinfo=None)
    print(t1 , y  , "%%%%%%%%%%%%%%%%%%%%%%")
    now = datetime.datetime.now().replace(microsecond=0)
    print((now - t1).total_seconds(), token_obj.expires_in , "&&&&&&&&&&&&&&&&&&&&&&&")
    if int((now - t1).total_seconds()) <= int(token_obj.expires_in): #by using old token
        print("Alreay exist ^^^^^^^^^^^^^^^^")
        return access_token
    else:
        url = 'https://oauth2.googleapis.com/token'
        data = {
            "client_id": config['CLIENT_ID'],
            "client_secret": config['CLIENT_SECRET'],
            "refresh_token": config['REFRESH_TOKEN'],
            "grant_type": "refresh_token"
        }
        res  = requests.post(url ,  data=data)
        print(res , "&&&&&&&&&&&&&&&&&")
        obj = tokenStuff.objects.all()[0]
        obj.time = datetime.datetime.now()
        obj.expires_in = res.json()['expires_in']
        obj.access_token = res.json()['access_token']
        obj.save()
        return res.json()['access_token']

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
            "parents":["14MBVQyZ6NtKVFHCBJMVsNRWoWFWQpntD"]
            }
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
            refresh = requests.get('https://iiitkalyani.herokuapp.com/updatecache/14MBVQyZ6NtKVFHCBJMVsNRWoWFWQpntD')
            print(r.text)
        else:
            name = res['name']
            name+=" Made Query"
            body = "My Mail Id : " + res['email']+"\n"
            body+= res['description']
            send_mail(name, body,settings.EMAIL_HOST_USER,['iiitk660@gmail.com'], fail_silently = False)
            obj  = details(name=res['name'] , email = res['email'] , description = res['description'] , date= datetime.datetime.now().date())
            obj.save()
            msg = 'Thanks For submitting Query'
    obj = cp.objects.all()
    title = []
    data = []
    question = []
    prblm = problemofday.objects.all()
    prblm = prblm[0].problem_of_the_day

    noti = notification.objects.all()
    notific = ""
    if len(noti) > 0:
        notific  = noti[0].notify
    
    print(notific, "cdslkcmdklf%%%%%%%%%%%%%%%%%")
    for objects in obj:
        title.append(objects.title)
        data.append(objects.data.split(','))
        question.append(objects.question.split(','))
    # refresh = requests.get('https://iiitkalyani.herokuapp.com/updatecache/14MBVQyZ6NtKVFHCBJMVsNRWoWFWQpntD')
    book = requests.get('https://iiitkalyani.herokuapp.com/getfiles/14MBVQyZ6NtKVFHCBJMVsNRWoWFWQpntD').json()

    
    context={
        'book':book,
        'msg':msg,
        'alldata':zip(title , data , question , obj),
        'problem':prblm,
        'notification':notific,
    }
    

    return render(request , 'cp.html' , context = context)


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
    obj = problemset.objects.all()
    prblm = problemofday.objects.all()
    prblm = prblm[0].problem_of_the_day
    obj = list(obj)
    obj.reverse()
    return render(request , 'problemset.html' , {'obj':obj , 'msg':msg , 'problem':prblm})
    
    
def clist(request):
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
    utcnow = datetime.datetime.utcnow()
    utcnext = utcnow + datetime.timedelta(days=10)
    username = 'resource'
    api_key = '431aa1f9405dea2cdf8965b6aca897557f3f4217'
    url = 'https://clist.by/api/v1/json/contest/?username='+username+'&api_key='+api_key + '&start__gt=' + utcnow.isoformat() + '&start__lt=' + utcnext.isoformat() + '&duration__lte=864000&filtered=true&order_by=start'
    res = requests.get(url)
    if res.status_code != 200:
        return HttpResponseRedirect('/cp')

    event = res.json().get('objects', [])
    name_list = ['codeforces' , 'codechef' , 'atcoder' , 'hackerearth' , 'hackerrank' , 'codingcompetitions.withgoogle' ,'topcoder' , 'binarysearch' , 'leetcode']

    duration=[]
    name=[]
    href=[]
    start_end_time=[]
    event_name = []
    pltform = []
    strt_format = "%H:%M %m-%d"
    end_format = "%H:%M"
    for data in event:
        platform = str(data['resource']['name']).split('.')[0]
        # print(platform)
        if platform  in name_list:
            pltform.append(data['resource']['name'])
            y = int(data['duration']/3600)
            z = int((data['duration'] - y*3600)/60)
            if y > 24:
                p = y
                y = int(y/24)
                dur = str("{0:0=2d}".format(y))+' days'
            else:
                dur = str("{0:0=2d}".format(y))+':'+str("{0:0=2d}".format(z))+' hr'
            duration.append(dur)
            event_name.append(data['event'])
            href.append(data['href'])
            name.append(platform)
            # icon.append(data['resource']['icon'])
            st = data['start']
            ed = data['end']
            dt_st = parse(st, fuzzy=True)
            dt_ed = parse(ed, fuzzy=True)
            st_utc = dt_st.replace(tzinfo=tz.utc)
            ed_utc = dt_ed.replace(tzinfo=tz.utc)
            st_asia = st_utc.astimezone(timezone('Asia/Kolkata'))
            ed_asia = ed_utc.astimezone(timezone('Asia/Kolkata'))
            time = st_asia.strftime(strt_format) + ' '+ed_asia.strftime(end_format)
            start_end_time.append(time)
    # print(type(event_name) , type(duration) , type(href) , type(name) ,type(icon) , type(start_end_time))
    return render(request ,'clist.html', {'all_data':zip(name , duration , start_end_time , event_name ,pltform , href) , 'msg':msg})


