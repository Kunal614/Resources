from django.shortcuts import render
from django.shortcuts import redirect
import json
import requests
from django.contrib.auth.models import User 
from django.contrib.auth import login , authenticate , logout
from django.http import HttpResponseRedirect
from .models import *
from django.http import HttpResponse
from datetime import datetime

# headers = {"Authorization": "Bearer ya29.a0AfH6SMCPUInnjHmPzT_vUgKYDt2g2cLivHp76eplwAuBktAE4arb5AEyhcAa-_Lan0pdw4XEgZ5vxPiQJ7ftPSscYJaePATyEbw5YROkPTrZnIQAf_twrsd9Y_31gPBMYJuMgitdJiXjkqwZm9WPT8LUZG0V"}

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
def cse(request):
    msg = ''
    if request.method == 'POST':
        res = request.POST
        msg = ''
        if res['type'] == 'query':
            print(request.POST , "&&&&&&&&&7")
            msg = "Thanks for submitting query"
        
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




def first_sem(request):
    print(request.user.is_authenticated , "cdcddcc" , request.user.username)
    msg = ''
    if request.method == 'POST':
        msg = "Thanks for submitting query"
    sub = ['ec1', 'c-c++' , 'linear_algebra' , 'physics' , 'english']
    return render(request , 'sem.html' , {'msg':msg , 'sub':sub})

def second_sem(request):
    msg = ''
    if request.method == 'POST':
        msg = "Thanks for submitting query"
    sub = ['ec2', 'dsa1' , 'discrete_maths' , 'probablity_stats' , 'econimocs']
    return render(request , 'sem.html' , {'msg':msg , 'sub':sub})

def third_sem(request):
    msg = ''
    if request.method == 'POST':
        msg = "Thanks for submitting query"
    sub = ['dsa2', 'calculus' , 'python' , 'automata_theory' , 'COA' ,'psychology']
    return render(request , 'sem.html' , {'msg':msg , 'sub':sub})

def fourth_sem(request):
    msg = ''
    if request.method == 'POST':
        msg = "Thanks for submitting query"
    sub = ['ec3', 'data-science' , 'os' , 'java']
    return render(request , 'sem.html' , {'msg':msg , 'sub':sub})

def fifth_sem(request):
    msg = ''
    if request.method == 'POST':
        msg = "Thanks for submitting query"
    sub = ['ai', 'compiler_design' , 'processor_controler' , 'computer_graphics' , 'business_management']
    return render(request , 'sem.html' , {'msg':msg , 'sub':sub})

def sixth_sem(request):
    msg = ''
    if request.method == 'POST':
        msg = "Thanks for submitting query"
    sub = ['ml', 'computer_networking','dbms' , 'computer_vision' , 'cognitive_science' ]
    return render(request , 'sem.html' , {'msg':msg , 'sub':sub})
   

def seventh_sem(request):
    msg = ''
    if request.method == 'POST':
        msg = "Thanks for submitting query"
    sub = ['ec', 'c-c++' , 'linear_algebra' , 'physics' , 'english']
    return render(request , 'sem.html' , {'msg':msg , 'sub':sub})
   

def eight_sem(request):
    msg = ''
    if request.method == 'POST':
        msg = "Thanks for submitting query"
    sub = ['ec', 'c-c++' , 'linear_algebra' , 'physics' , 'english']
    return render(request , 'sem.html' , {'msg':msg , 'sub':sub})
   


def ec1(request):
    msg = ''
    if request.method == 'POST':

        res = request.POST
        print(res)
        if res['type'] == 'doc':
            file = request.FILES.get('name' , False)
            print(res , file)
            file_name = str(file)
            infile = request.FILES["name"].read()

            if res['doc'] == 'books':
                para = {
                "name": str(file_name),
                "parents":["1Mf3RLjcdplr7r00R12Ep1AgGFGotnP8s"]
                }
            else: 
                para = {
                "name": str(file_name),
                "parents":["10xG9XWg_HjDZj6g9_LDFAofeES9hjerp"]
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
            msg = "Thanks for submitting query"


    #book
    print(msg)
   
    
    # book = requests.get(' http://6cf7a3821881.ngrok.io/getfiles/1Mf3RLjcdplr7r00R12Ep1AgGFGotnP8s').json()
    
       
    # copy = requests.get(' http://6cf7a3821881.ngrok.io/getfiles/10xG9XWg_HjDZj6g9_LDFAofeES9hjerp').json()
    
    
    # if len(book) > 0 and len(copy)> 0:
    #     context={
    #         'book':book,
    #         'copy':copy,
    #         'msg':msg
    #     }
    # elif len(book) > 0:
    #     context={
    #         'book':book,
    #         'msg':msg
    #     }
    # elif len(copy)>0:
    #     context={
    #         'copy':copy,
    #         'msg':msg
    #     }

    return render(request , 'docs.html')

