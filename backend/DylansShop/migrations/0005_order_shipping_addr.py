# Generated by Django 4.0.1 on 2022-02-09 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DylansShop', '0004_basket_product_image_product_price_order_basketitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_addr',
            field=models.TextField(default=''),
        ),
    ]
