from django.contrib import admin
from .models import Status
# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)


