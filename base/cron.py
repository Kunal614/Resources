import requests
from django.core.mail import send_mail
from django.core.mail import EmailMessage

def req():
    send_mail('Responses', "Question added",'iiitk660@gmail.com',['papertronic272@gmail.com'], fail_silently = False)
    res = requests.get('https://rocsiiitkalyani.herokuapp.com')