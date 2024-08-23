from django.contrib import admin
from .models import *

# Register your models here.

class CategoryProductAdmin(admin.ModelAdmin):
    list_display=['name', 'code']

    class Meta:
        model= CategoryProducts

class SizeAdmin(admin.ModelAdmin):
    list_display=['name']

    class Meta:
        model= Size

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','cost', 'category']
    list_filter=['category',]
    search_fields=['name', 'category']

    class Meta:
        model=Product

admin.site.register(CategoryProducts,CategoryProductAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Product,ProductAdmin)

