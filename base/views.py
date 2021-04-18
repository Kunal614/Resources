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

# Create your views here.

def home(request):
    return render(request , 'home.html')



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
        send = '/'+send.split('?')[0]
        if user == None:
            return HttpResponseRedirect(send+"?res=0")
        else: 
            return HttpResponseRedirect(send+"?res=1")

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')