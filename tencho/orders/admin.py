from django.contrib import admin
from .models import Status, Basket
# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class BasketAdmin(admin.ModelAdmin):
    search_fields=['user','product','size']

    class Meta:
        model = Basket

admin.site.register(Basket,BasketAdmin)



