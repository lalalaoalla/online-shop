from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from .models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя' 
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль' 
    }))
    class Meta:# ну м ытут если что указываем с кем мы работаем
        model = User
        fields = ['username', 'password']



class UserRegistrationForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите фамилию' 
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя' 
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя' 
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите электронную почту' 
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль' 
    }))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password']