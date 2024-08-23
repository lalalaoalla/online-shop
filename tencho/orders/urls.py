from django.urls import path

from . import views
from .views import basket_add, basket_delete

app_name = 'orders'  

urlpatterns = [
    path('',views.cart, name='order'),
    #path('baskets/add/<int:product_id>/',, name='basket_add'),
    #api
    path('basket/add/',basket_add,name='basket_add'),
    path('basket/delete/',basket_delete,name="basket_delete")
    #path('',views.about, name='about'),
    #path('catalogue/',include('products.urls'), namespace='catalogue')
]