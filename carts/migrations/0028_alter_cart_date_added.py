# Generated by Django 5.1.5 on 2025-01-25 06:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0027_alter_cart_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 13, 51, 33, 733276)),
        ),
    ]
