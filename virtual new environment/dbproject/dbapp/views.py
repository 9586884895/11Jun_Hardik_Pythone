from django.shortcuts import render
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
