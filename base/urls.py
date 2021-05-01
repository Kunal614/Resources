from django.urls import path 
from .views import *
from django.views.decorators.cache import cache_page
urlpatterns = [
   
    path('',home, name='home'),
    path('login' , Login  , name='login'),
    path('logout' , Logout , name='logout'),
]
