"""
URL configuration for tencho project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'users'  

urlpatterns = [
    path('cabinet/',views.cabinet, name='cabinet'),
    path('cabinet_no_autorization/',views.cabinet_no_autorization, name='cabinet_no_autorization'),
    path('cabinet/data/',views.data, name='data'),
    path('cabinet/delivery/', views.delivery, name='delivery'),
    path('cabinet/users_cards/',views.users_cards, name='users_cards'),
    path('cabinet/purchases/', views.purchases, name = 'purchases'),
    path('cabinet/favorite/', views.favorite, name='favorite'),
    path('cabinet/notifications',views.notify, name='notify'),
    path('login/', views.login,name='login'),
    path('registation/', views.registration, name='registration'),
    path('logout/', views.logout_view, name='logout'),
]
