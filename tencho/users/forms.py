from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
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

class UserProfileForm(UserChangeForm):
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'image', 'username','email', 'address']


class UserRegistrationForm(UserCreationForm):
    # first_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': 'Введите фамилию' 
    # }))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': 'Введите имя' 
    # }))
    # username = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': 'Введите имя пользователя' 
    # }))
    # email = forms.CharField(widget=forms.EmailInput(attrs={
    #     'placeholder': 'Введите электронную почту' 
    # }))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'placeholder': 'Введите пароль' 
    # }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email']
    
    # def __init__(self, *args, *kwargs):
    #     super().__init__(*args, *kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Field('first_name', css_class='form-control', placeholder='Фамилия'),
    #         Field('last_name', css_class='form-control', placeholder='Имя'),
    #         Field('username', css_class='form-control', placeholder='Имя пользователя'),
    #         Field('email', css_class='form-control', placeholder='Электронная почта'),
    #         Field('password', css_class='form-control', placeholder='Пароль'),
    #         Submit('submit', 'Зарегистрироваться', css_class='btn btn-primary')
    #     )