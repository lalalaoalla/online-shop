from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth import logout

# Create your views here.

def cabinet(request):
    return render(request,'users/cabinet.html')

def cabinet_no_autorization(request):
    return render(request,'users/no_autorization_cabinet.html')

def data(request):
    if request.method == 'POST':
        form = UserProfileForm(instance = request.user,data = request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:data'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance = request.user)
    context = {'form': form}
    return render(request, 'users/tabs_cabinet/data.html', context)

def delivery(request):
    return render(request,'users/tabs_cabinet/delivery.html')

def users_cards(request):
    return render(request,'users/tabs_cabinet/users_cards.html')

def purchases(request):
    '''Покупки'''
    return render(request,'users/tabs_cabinet/purchases.html')

def favorite(request):
    return render(request, 'users/tabs_cabinet/favorite.html')

def notify(request):
    return render(request,'users/tabs_cabinet/notify.html')

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)#заполняем нашими данными форму
        if form.is_valid():#если они прошли проверку
            username = request.POST['username']#забираем наши данные
            password = request.POST['password']
              # Добавить отладку
            #начинаем аутентификацию
            user = auth.authenticate(username=username, password=password)
            if user:
                # здесь мы проверяем ну то есть если такой пользователь нашелся то происходит авторизация
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()#это просто получение формы
    context = { 'form' : form}
    return render(request,'users/login.html', context)



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))





def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'users/registration.html', context)