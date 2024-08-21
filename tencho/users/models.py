from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users_avatar/', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural = 'Пользователи'

class Cards(models.Model):
    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.CASCADE)
    card_number_hash = models.CharField(max_length=255, unique=True)  # Хеш номера карты
    expiry_date = models.DateField()
    card_type = models.CharField(max_length=20, choices=(
        ('visa', 'Visa'),
        ('mastercard', 'Mastercard'),
        ('mir', 'МИР'),
    ))
    class Meta:
        verbose_name = 'Карта для оплаты'
        verbose_name_plural = 'Карты для оплаты'


