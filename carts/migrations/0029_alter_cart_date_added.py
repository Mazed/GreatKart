# Generated by Django 5.1.5 on 2025-01-25 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0028_alter_cart_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 16, 17, 41, 931168)),
        ),
    ]
