# Generated by Django 5.1.5 on 2025-01-17 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0011_alter_cart_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]
