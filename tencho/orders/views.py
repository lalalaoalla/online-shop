from django.shortcuts import render, HttpResponseRedirect
from .models import Basket
from products.models import Product,Size 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse
from django.http import JsonResponse
#from .serializers import BasketSerializer

# Create your views here.

def cart(request):
    context = {
        'baskets': Basket.objects.filter(user=request.user, is_active=True)
    }
    return render(request, 'orders/cart.html', context)

#обработчики событий
def basket_add(request):
    return_dict = dict()
    data = request.POST
    product_id = data.get("product_id")
    quantity = int(data.get("quantity"))
    size = data.get("size")
    if (size=="XS"):
        cost = int(data.get("cost"))
    else: 
        if (size=="S"):
            cost = int(int(data.get("cost"))*1.05)
        if (size == "M"):
            cost = int(int(data.get("cost"))*1.1)
        if (size=="L"):
            cost = int(int(data.get("cost"))*1.15)
        if (size=="XL"):
            cost = int(int(data.get("cost"))*1.20)
    quantity_price=int(quantity*cost)

    new_product= Basket.objects.create(user=request.user, product_id=product_id, quantity=quantity, size=size, price=cost,quantity_price=quantity_price)
    return JsonResponse(return_dict)
    #return HttpResponseRedirect(reverse('orders:order'))

def basket_delete(request):
    return_dict = dict()
    
    data = request.POST

    basket_id = data.get("basket_id")
    print(basket_id)
    is_del = Basket.objects.filter(id=basket_id).update(is_active=False)
    print(is_del)
    return_dict['success'] = True if is_del else False
    return HttpResponseRedirect(reverse('orders:order'))
    #return JsonResponse(return_dict)
    

