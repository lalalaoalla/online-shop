from django.contrib.auth.forms import AuthenticationForm
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