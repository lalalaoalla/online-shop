from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    #list_display=['first_name','last_name', 'username', 'email']
    search_fields=['first_name', 'username']

    class Meta:
        model = User

admin.site.register(User,UserAdmin)