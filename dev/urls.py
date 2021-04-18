from django.urls import path 
from .views import *
urlpatterns = [
    path('dev' ,deV, name='dev' ),
    path('edit_dev/<int:id>' ,edit_dev, name='dev' ),
    
]