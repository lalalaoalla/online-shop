from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'products/index.html')

def catalogue(request):
    return render(request, 'products/catalogue.html')

def about(request):
    return render(request,'about.html')

def product_detail(request, id):
    return render(request, 'products/product.html')

class ProductsAPIViews(APIView):# в общем это то, что мы получаем
    def get(self, request):
        all_products = Product.objects.all()
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