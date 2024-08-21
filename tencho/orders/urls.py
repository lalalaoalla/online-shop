from django.urls import path

from . import views
from .views import basket_add

app_name = 'orders'  

urlpatterns = [
    path('',views.cart, name='order'),
    #path('baskets/add/<int:product_id>/',, name='basket_add'),
    #api
    path('basket/add/',basket_add,name='basket_add'),
    #path('',views.about, name='about'),
    #path('catalogue/',include('products.urls'), namespace='catalogue')
]