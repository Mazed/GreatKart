# Generated by Django 5.1.5 on 2025-01-25 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_orderproduct_variation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 16, 17, 41, 938978)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 16, 17, 41, 938997)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2025, 1, 25, 16, 17, 41, 939899)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='updated_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2025, 1, 25, 16, 17, 41, 939930)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 16, 17, 41, 938198)),
        ),
    ]
