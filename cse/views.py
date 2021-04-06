from django.shortcuts import render
from django.shortcuts import redirect
import json
import requests


headers = {"Authorization": "Bearer ya29.a0AfH6SMDocF56q1ihTzPj98e2gezJ8Gp0pS1CrxkgQGMv6ZJlq7gd9_ypLYutSOvnhuRp7A3eXfDhCtOZFbsC0QwOW1myw2PJdsGa6UhZ5RR-1ONxGCCSQBASuqVX5kIxOsKRh-ZsOalcg4pPNGFUGnTjbcy7"}
def home(request):
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
                'name':'First',
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
                'name':'Second',
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
                'name':'Third',
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
                'name':'Fourth',
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
    if request.method == 'POST':
        res = request.POST
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
        print(type(files))
        r = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=headers,
            files=files
        )
        print(r.text)

    return render(request , 'docs.html')
