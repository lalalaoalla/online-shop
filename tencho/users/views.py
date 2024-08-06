from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import UserLoginForm
from django.contrib import auth
from django.urls import reverse
# Create your views here.

def cabinet(request):
    return render(request,'users/cabinet.html')

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)#заполняем нашими данными форму
        if form.is_valid():#если они прошли проверку
            username = request.POST['username']#забираем наши данные
            password = request.POST['password']
            #начинаем аутентификацию
            user = auth.authenticate(username=username, password=password)
            if user:
                # здесь мы проверяем ну то есть если такой пользователь нашелся то происходит авторизация
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print('Данные не валидны')
    else:
        form = UserLoginForm()#это просто получение формы
    context = { 'form' : form}
    return render(request,'users/login.html', context)

def registration(request):
    return render(request, 'users/registration.html')