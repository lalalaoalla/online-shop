from django.urls import path

from . import views

app_name = 'orders'  

urlpatterns = [
    path('',views.cart, name='order'),
    #path('',views.about, name='about'),
    #path('catalogue/',include('products.urls'), namespace='catalogue')
]