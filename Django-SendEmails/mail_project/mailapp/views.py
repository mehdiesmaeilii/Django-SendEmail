from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(request):
    send_mail('hey this is from home view','hey this the body of the mail','mahdi.smaeily.5474@gmail.com',[]#this[]is where you should write people emails you want to send) 
              )
    return render(request,'home.html')