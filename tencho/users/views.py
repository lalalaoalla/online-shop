from django.shortcuts import render

# Create your views here.

def cabinet(request):
    return render(request,'users/cabinet.html')

def login(request):
    return render(request,'users/login.html')

def registration(request):
    return render(request, 'users/registration.html')