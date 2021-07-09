
from django.urls import path 
from .views import *
urlpatterns = [
    path('cse',cse , name='cse'),
    path('sub' ,sub , name='subject' ),
    path('sem',sem , name='sem'),
    path('addCseRecord' , addCseRecord , name= 'addCseRecord')
  
]
