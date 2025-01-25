# Generated by Django 5.1.5 on 2025-01-25 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_order_created_at_alter_order_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 17, 25, 7, 683845)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 17, 25, 7, 683879)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 17, 25, 7, 684733)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 17, 25, 7, 684751)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 17, 25, 7, 683064)),
        ),
    ]
