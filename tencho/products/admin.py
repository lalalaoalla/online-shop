from django.contrib import admin
from .models import *

# Register your models here.

class CategoryProductAdmin(admin.ModelAdmin):
    list_display=['name']

    class Meta:
        model= CategoryProducts

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','cost', 'category']
    list_filter=['name', 'category',]
    search_fields=['name', 'category']

    class Meta:
        model=Product

admin.site.register(CategoryProducts,CategoryProductAdmin)
admin.site.register(Product,ProductAdmin)