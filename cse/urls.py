
from django.urls import path 
# from .views import home ,  first_sem , ec1 , second_sem , third_sem , fourth_sem , fifth_sem , sixth_sem , seventh_sem , eight_sem , Login , Logout , cP
from .views import *
urlpatterns = [
    path('',home , name='home'),
    # path('first_year' ,first_year , name='first_year' ),
    # path('second_year' ,second_year , name='second_year' ),
    # path('third_year' ,third_year , name='third_year' ),
    # path('fourth_year' ,fourth_year , name='fourth_year' ),
    path('login' , Login  , name='login'),
    path('logout' , Logout , name='logout'),
    path('first_sem' ,first_sem , name='first_sem' ),
    path('second_sem' ,second_sem , name='second_sem' ),
    path('third_sem' ,third_sem , name='third_sem' ),
    path('fourth_sem' ,fourth_sem , name='fourth_sem' ),
    path('fifth_sem' ,fifth_sem , name='fifth_sem' ),
    path('sixth_sem' ,sixth_sem , name='sixth_sem' ),
    path('seventh_sem' ,seventh_sem , name='seventh_sem' ),
    path('eight_sem' ,eight_sem , name='eight_sem' ),
    path('ec1' ,ec1 , name='ec1' ),
    path('cp' ,cP, name='cp' ),
    path('edit/<int:id>' ,edit, name='edit' ),
    path('dev' ,deV, name='dev' ),
    path('problemset' ,problemsets, name='problemset' ),
]
