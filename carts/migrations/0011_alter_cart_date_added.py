# Generated by Django 5.1.5 on 2025-01-17 23:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0010_alter_cart_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_added',
            field=models.DateTimeField(verbose_name=datetime.datetime(2025, 1, 18, 6, 21, 29, 257171)),
        ),
    ]
