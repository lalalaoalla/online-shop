from rest_framework import serializers
from .models import Product
# по факту задача сериализатора - конвертировать то, что мы получили, в json формат

# # А МОЖНО И ТАК(БАЗОВО ВСЕ)
# # class ProductModel:
# #     def __init__(self, name, cost, category, description, image):
# #         self.name = name
# #         self.cost  = cost
# #         self.category = category
# #         self.description = description
# #         self.image = image



class ProductSerializer(serializers.Serializer):# это наш сериализатор(то что мы преобразуем в json)
    id = serializers.IntegerField()
    name = serializers.CharField(max_length = 128)
    cost=serializers.DecimalField(max_digits=10,decimal_places=0)
    category=serializers.CharField(max_length = 128)
    description=serializers.CharField()
    image=serializers.SerializerMethodField()# не такое стандартное поле, для того, чтобы использовать функцию get_image
    created=serializers.DateTimeField()

    def get_image(self, obj):#возвращает вместе с папкой media(а то иначе не показывало)
        if obj.image:
            return obj.image.url
        return None

   

# Здесь должны быть дальше функции с кодированием и декодировании

# #МОЖНО ТАК
# class ProductSerializer(serializers.ModelSerializer):# это наш сериализатор
#     class Meta:
#         model = Product# из какой модели
#         fields = '__all__'#какие поля отправляем в ответ
