from django.db import models

# Create your models here.

class Status(models.Model):
    '''Статусы нашего заказа'''
    name = models.CharField(max_length=16)
    is_avtive = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)#дата добавления заказа
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name
    class Meta:
        verbose_name='Статус заказа'
        verbose_name_plural = 'Статусы заказа'
