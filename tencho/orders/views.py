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

def basket_add(request):
    return_dict = dict()
    #session_key = request.session.session_key
    print (request.POST)
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

    is_delete = data.get("is_delete")

    if is_delete == 'true':
        Basket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product= Basket.objects.create(user=request.user, product_id=product_id, quantity=quantity, size=size, price=cost,quantity_price=quantity_price)
    return JsonResponse(return_dict)
    #return HttpResponseRedirect(reverse('orders:order'))

