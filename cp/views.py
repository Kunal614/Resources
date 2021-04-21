from django.shortcuts import render
from django.shortcuts import redirect
import json
import requests
from django.contrib.auth.models import User 
from django.http import HttpResponseRedirect
from .models import *
from django.http import HttpResponse
# from datetime import datetime
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from pytz import timezone
from datetime import timezone as tz
import datetime
from dateutil.parser import parse
def get_access_token():
    url = 'https://oauth2.googleapis.com/token'
    data = {
        "client_id": "1091937598228-5aan4ts4lm6u28r38q29926b81jatcts.apps.googleusercontent.com",
        "client_secret": "ZkzCCfgnau4hEhaH__PYflke",
        "refresh_token": "1//04vfemCPfDdMICgYIARAAGAQSNwF-L9IrHy8vb_Pzgf6eV6wZyf7mVaHDkZCF_AJnsGFDgyjtwuv28D34Z7TcJW7YK2uZzIQSusU",
        "grant_type": "refresh_token"
    }

    res  = requests.post(url ,  data=data)
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
    obj = list(obj)
    obj.reverse()
    return render(request , 'problemset.html' , {'obj':obj , 'msg':'' , 'problem':prblm})
    
    
def clist(request):
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
    return render(request ,'clist.html', {'all_data':zip(name , duration , start_end_time , event_name ,pltform , href) , 'msg':''})


    