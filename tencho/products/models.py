from django.db import models
from django.conf import settings


# Create your models here.

class CategoryProducts(models.Model):
    name=models.CharField(max_length=128,unique=True)
    code=models.CharField(max_length=128, default='empty')

    class Meta: 
        verbose_name='Категория'
        verbose_name_plural='Категории'
    
    def __str__(self):
        return self.name
    
class Size(models.Model):
    name=models.CharField(max_length=12)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'
    
class Product(models.Model):
    #ВНИМАНИЕ on_delete указывает, что произойдет, если поле КАТЕГОРИЯ будет удалено
    name=models.CharField(max_length=128)
    cost=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(CategoryProducts,on_delete=models.CASCADE)#тоже будет удален
    description=models.TextField()
    image=models.ImageField(upload_to='products_images/')
    is_active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)

    def get_image_url(self):
           """Возвращает полный URL изображения с учетом MEDIA_URL."""
           if self.image:
               return f"{settings.MEDIA_URL}{self.image.name}"
           return None

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self):
        return '%s %s' % (self.category, self.name)

