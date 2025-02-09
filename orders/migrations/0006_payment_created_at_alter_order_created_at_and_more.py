# Generated by Django 5.1.5 on 2025-01-25 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_payment_created_at_alter_order_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 12, 54, 28, 364837)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 12, 54, 28, 366168)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 12, 54, 28, 366207)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 12, 54, 28, 367529)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 12, 54, 28, 367555)),
        ),
    ]
