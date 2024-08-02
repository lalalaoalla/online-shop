from django.db import models

# Create your models here.

class CategoryProducts(models.Model):
    name=models.CharField(max_length=128,unique=True)

    class Meta: 
        verbose_name='Категория'
        verbose_name_plural='Категории'
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    #ВНИМАНИЕ on_delete указывает, что произойдет, если поле КАТЕГОРИЯ будет удалено
    name=models.CharField(max_length=128)
    cost=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(CategoryProducts,on_delete=models.CASCADE)#тоже будет удален
    description=models.TextField()
    image=models.ImageField()
    is_active=models.BooleanField(default=True)
    created=models.DateTimeField()
    updated=models.DateTimeField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self):
        return '%s %s %s' % (self.category, self.name, self.cost)

