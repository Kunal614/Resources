
from django.urls import path 
from .views import *
urlpatterns = [
    path('cse',cse , name='cse'),
    path('first_sem' ,first_sem , name='first_sem' ),
    path('second_sem' ,second_sem , name='second_sem' ),
    path('third_sem' ,third_sem , name='third_sem' ),
    path('fourth_sem' ,fourth_sem , name='fourth_sem' ),
    path('fifth_sem' ,fifth_sem , name='fifth_sem' ),
    path('sixth_sem' ,sixth_sem , name='sixth_sem' ),
    path('seventh_sem' ,seventh_sem , name='seventh_sem' ),
    path('eight_sem' ,eight_sem , name='eight_sem' ),
    path('ec1' ,ec1 , name='ec1' ),
  
]
