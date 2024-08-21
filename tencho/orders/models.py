from django.db import models
from users.models import User
from products.models import Product, Size

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

class Basket(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.IntegerField()
    size = models.CharField(default="XS", max_length=4)
    #order_number = modelsField#надо исправить это пока просто текст чтобы не давало ошибку
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


    def __str__(self):
        return f' Корзина {self.user.last_name} {self.user.first_name}'
    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

# class Order(models.Model):
#     '''Заказы'''
#     status = models.ForeignKey(to=Status, on_delete=models.PROTECT)

#     class Meta:
#         verbose_name = 'Заказ'
#         verbose_name_plural = 'Заказы'
