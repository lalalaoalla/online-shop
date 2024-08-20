from rest_framework import generics
from .models import Product, Size
from orders.models import Basket
from users.models import User
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
import requests

# Create your views here.
#отображение страниц
def index(request):
    response = requests.get('http://127.0.0.1:8001/api/v1/productlist_index/')
    if response.status_code == 200:  # Проверяем, был ли запрос успешным
        popular_products = response.json()  # Получаем данные в формате JSON
    else:
        popular_products = []  # Возвращаем пустой список, если запрос не удался
    
    response = requests.get('http://127.0.0.1:8001/catalogue/api/v1/productlist_index_new/')
    if response.status_code == 200:  # Проверяем, был ли запрос успешным
        new_products = response.json()  # Получаем данные в формате JSON
    else:
        new_products = []  # Возвращаем пустой список, если запрос не удался
    #popular_products = 'api/v1/productlist_index/'
    context = {
        'sizes': Size.objects.all(),
        'popular_products':popular_products,
        'new_products': new_products
    }
    return render(request,'products/index.html', context)

def catalogue(request):
    response = requests.get('http://127.0.0.1:8001/api/v1/productlist_in_catalogue/')
    if response.status_code == 200:  # Проверяем, был ли запрос успешным
        all_products = response.json()  # Получаем данные в формате JSON
    else:
        all_products = []  # Возвращаем пустой список, если запрос не удался
    
    context = {
        'sizes': Size.objects.all(),
        'all_products': all_products
    }
    return render(request, 'products/catalogue.html', context)


def about(request):
    return render(request,'about.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'sizes': Size.objects.all(),
        'product': product
    }
    return render(request, 'products/product.html', context)

#Обработчики событий
# def basket_add(request, product_id):
#     if not request.user.is_authenticated:
#         # Сохранение URL в сессии
#         request.session['next_url'] = request.META.get('HTTP_REFERER', '/') 

#         return redirect('users:login')
    

#APIViews
class ProductsAPIViews(APIView):# в общем это то, что мы получаем
    def get(self, request):
        all_products = Product.objects.order_by('created')[:12]
        serialized_products = ProductSerializer(all_products, many=True)
        return Response(serialized_products.data)
    
class ProductsAPIViewsInOneCategory(APIView):# в общем это то, что мы получаем
    def get(self, request, id):
        all_products = Product.objects.all()
        serialized_products = ProductSerializer(all_products, many=True)
        return Response(serialized_products.data)
    
class ProductsAPIViewsNews(APIView):# в общем это то, что мы получаем
    def get(self, request):
        all_products = Product.objects.order_by('-created')[:6]
        serialized_products = ProductSerializer(all_products, many=True)
        return Response(serialized_products.data)
    
class ProductsAPIViewsCataloque(APIView):# в общем это то, что мы получаем
    def get(self, request):
        all_products = Product.objects.all()
        serialized_products = ProductSerializer(all_products, many=True)
        return Response(serialized_products.data)
    


# А МОЖНО И ВОТ ТАК

# class ProductsAPIViews(APIView):# он уже говорит какой запрос пришел, а функции мы прописали сами
#     def get(self, request):
#         all_products = Product.objects.all()
#         serialized_products = ProductSerializer(all_products, many=True).data
        
#         response_data = {} 
#         for i, product in enumerate(serialized_products):
#             response_data[str(i + 1)] = product 
        
#         return Response(response_data)
    
#     def post(self, request):
#         serializer  =ProductSerializer(data=request.data)
#         serializer.is_valid(reise_exception=True)
#         serializer.save()
#         return Response({serializer.data})


#МОЖНО ТАК
# class ProductsAPIViews(generics.ListAPIView):# это у нас представление
#     queryset=Product.objects.all()# считываем все
#     serializer_class = ProductSerializer# сериализатор наш