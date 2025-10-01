from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def index(request):
    if request.method=='POST': #true
        form=userform(request.POST)
        if form.is_valid():
            form.save()
            print("Record Inserted sucessfully")
        else:
            print(form. errors)
    return render(request,"index.html")

def showdata(request):
    data=userinfo.objects.all()
    print(data)
    return render(request,"showdata.html",{'data':data})

def update(request,id):
    uid=userinfo.objects.get(id=id)
    if request.method=='POST': #true
        form=updateform(request.POST,instance=uid)
        if form.is_valid():
            form.save()
            print("Record Updated sucessfully")
        else:
            print(form. errors)
    return render(request,'update.html',{'uid':uid})

def deletedata(request,id):
    uid=userinfo.objects.get(id=id)
    userinfo.delete(uid)
    return redirect('showdata')
