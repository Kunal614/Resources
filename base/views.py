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
from django.views.decorators.cache import cache_page

# Create your views here.

def home(request):
    abt = about.objects.all()
    data = ''
    if len(abt) > 0:
        data = abt[0].data
    return render(request , 'home.html' , {'about':data})



def Login(request):
    if request.method == 'POST':
        res = request.POST
        print(res)
        username = res['username']
        password = res['pass']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request , user)   
        print(request.path_info) 
        send = res['url']
        y  = send.split('?')[0]
        send='/'
        print(y)
        if y =='problemset' or y== 'cp' or y == 'clist':
            send+='cp'
        if y =='year' or y== 'sem' or y == 'cse' or y == 'sub' :
            send+='cse'
        if y =='dev':
            send+='dev'
        if user == None:
            return HttpResponseRedirect(send+"?res=0")
        else: 
            return HttpResponseRedirect(send+"?res=1")

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')