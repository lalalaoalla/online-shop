from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'products/index.html')

def catalogue(request):
    return render(request, 'products/catalogue.html')

def about(request):
    return render(request,'about.html')