from django.urls import path 
# from .views import home ,  first_sem , ec1 , second_sem , third_sem , fourth_sem , fifth_sem , sixth_sem , seventh_sem , eight_sem , Login , Logout , cP
from .views import *

urlpatterns = [
    path('cp' ,cP, name='cp' ),
    path('edit/<int:id>' ,edit, name='edit' ),
    path('problemset' ,problemsets, name='problemset' ),
    path('clist' , clist , name='clist'),
    path('addCpRecord',addCpRecord , name='addcprecord'),
    # path('pr' , pr, name='pr')
    
]