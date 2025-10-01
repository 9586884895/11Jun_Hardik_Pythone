from django.shortcuts import render,redirect

# Create your views here.
def admin_index(request):
    return render(request,'admin_index.html')
def admin_dashboard(request):
    return render(request,'admin_dashboard.html')
