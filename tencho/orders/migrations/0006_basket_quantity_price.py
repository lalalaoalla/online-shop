# Generated by Django 5.0.6 on 2024-08-22 09:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0005_alter_basket_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="basket",
            name="quantity_price",
            field=models.IntegerField(default=1),
        ),
    ]
