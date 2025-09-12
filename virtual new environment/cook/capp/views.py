from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")
def calendar(request):
    return render(request,"calendar.html")
def chefs(request):
    return render(request,"chefs.html")
def contacts(request):
    return render(request,"contacts.html")
def courses(request):
    return render(request,"courses.html")
def recipes(request):
    return render(request,"recipes.html")

