from django.shortcuts import render, HttpResponseRedirect
from .models import Basket
from products.models import Product,Size 
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse
from django.http import JsonResponse
#from .serializers import BasketSerializer

# Create your views here.

def cart(request):
    context = {
        'baskets': Basket.objects.filter(user=request.user)
    }
    return render(request, 'orders/cart.html', context)

def basket_add(request):
    return_dict = dict()
    #session_key = request.session.session_key
    print (request.POST)
    data = request.POST
    product_id = data.get("product_id")
    quantity = data.get("quantity")
    size = data.get("size")
    cost = data.get("cost")
    new_product= Basket.objects.create(user=request.user, product_id=product_id, quantity=quantity, size=size, price=cost)
    
    
    # is_delete = data.get("is_delete")

    # if is_delete == 'true':
    #     ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    # else:
    #     
    #     if not created:
    #         print ("not created")
    #         new_product.nmb += int(nmb)
    #         new_product.save(force_update=True)
    return JsonResponse(return_dict)
    # product = Product.objects.get(id=product_id)
    # baskets = Basket.objects.filter(user=request.user, product=product)
    # if not baskets.exists():
    #     Basket.objects.create(user=request.user, product=product, quantity=1)
    #     #is_created = True
    # else:
    #     basket = baskets.first()
    #     basket.quantity += 1
    #     basket.save()
    #     #is_crated = False
    # return HttpResponseRedirect(reverse('orders:order'))

#APIViews

#class BasketAPIViews(APIView):
    
    # permission_classes = [IsAuthenticated]#типа что это идет только с авторизованными пользователями

    # def post(self, request):
    #     serializer = BasketSerializer(data=request.data)#создаем сериализатор и передаем туда данные из post запроса
    #     if serializer.is_valid():
    #         product_id = serializer.validated_data.get("product")
    #         size = serializer.validated_data.get("size")  # Добавьте получение размера
    #         quantity = serializer.validated_data.get("quantity")

    #         product = Product.objects.get(pk=product_id)  # Добавьте логику получения продукта по ID
            
    #         cart_item, created = Basket.objects.get_or_create(
    #             user=request.user,
    #             product=product,
    #             size=size  # Сохраните размер в CartItem
    #         )
    #         if not created:
    #             cart_item.quantity += quantity
    #             cart_item.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)