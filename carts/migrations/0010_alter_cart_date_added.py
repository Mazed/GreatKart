# Generated by Django 5.1.5 on 2025-01-17 23:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_alter_cart_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_added',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime.now),
        ),
    ]
