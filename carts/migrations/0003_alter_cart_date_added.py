# Generated by Django 5.1.5 on 2025-01-17 23:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cartitem_variations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_added',
            field=models.DateField(verbose_name=datetime.date(2025, 1, 18)),
        ),
    ]
