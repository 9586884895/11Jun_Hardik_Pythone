from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout
import random
from django.core.mail import send_mail
from finalp import settings

# Create your views here.

def index(request):
    user=request.session.get("user")
    return render(request,'index.html',{'user':user})
def Addnotes(request):
    return render(request,'Addnotes.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def profile(request):
    return render(request,'profile.html')

def login(request):
    msg=""
    if request.method=="POST":
        email=request.POST['email']
        pas=request.POST['password']
        user=signup.objects.filter(email=email,password=pas)
        if user: #true
            print("login sucessfully")
            msg="Login Sucessfully!"
            request.session["user"]=email
            return redirect('/')
        else:
            print("Error! login failed..")
            msg="Error! login failed.."
    return render(request,'login.html',{'msg':msg})

def usersignup(request):
    msg=""
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
            form.save()
            msg="Signup sucessfully!"

            # otp sending code...
            otp=random.randint(111111,999999)
            sub="your one time password"
            message=f"Dear User!\n\nThanks for register our service!\n\For account verification, Your one time password is {otp}.\n\nThanks & Regards\nGourmet cooking class\n+91 9586884895 | hardik.isavani@gmail.com"
            from_email=settings.EMAIL_HOST_USER
            to_email=[request.POST["email"]]
            send_mail(subject=sub,message=message,from_email=from_email,recipient_list=to_email)
            print("email send sucessfully")
            return redirect('otpverify')
        else:
            print(form.errors)
            msg="error!Something Went wrong..."
    return render(request,'signup.html',{'msg':msg})

def userlogout(request):
    logout(request)
    return redirect('/')

def otpverify(request):
    return render(request,'otpverify.html')

