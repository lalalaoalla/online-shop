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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from products.views import index, about, ProductsAPIViews, ProductsAPIViewsNews

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',index, name='index'),
    path('catalogue/',include('products.urls', namespace='catalogue')),
    path('about/', about, name='about'),
    path('users/',include('users.urls', namespace='users')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('api/v1/productlist_index/', ProductsAPIViews.as_view()),
    path('api/v1/productlist_index_new/', ProductsAPIViewsNews.as_view())
    
] \
+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
