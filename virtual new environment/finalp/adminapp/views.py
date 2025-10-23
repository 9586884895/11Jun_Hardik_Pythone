from django.shortcuts import render,redirect
from userapp.models import *

# Create your views here.
def admin_index(request):  # login page
    if request.method=='POST':
        if request.POST["username"]=="admin" and request.POST["password"]=="Admin@123":
            print("login sucessfully")
            return redirect("admin_dashboard")
        else:
            print("errors, login failed")
    return render(request,'admin_index.html')

def admin_dashboard(request):
    userdata=signup.objects.all()
    u=len(userdata) # length find return int value
    notesdata=note.objects.all()
    n=len(notesdata) # length find return int value
    return render(request,'admin_dashboard.html',{'userdata':u,'notesdata':n,'udata':userdata})

def admin_userdata(request):
    userdata=signup.objects.all()
    return render(request,'admin_userdata.html',{'userdata':userdata})

def admin_notesdata(request):
    notesdata=note.objects.all()      
    return render(request,'admin_notesdata.html',{'notesdata':notesdata})
