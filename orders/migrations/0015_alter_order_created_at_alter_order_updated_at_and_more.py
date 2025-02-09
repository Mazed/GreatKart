# Generated by Django 5.1.5 on 2025-01-26 04:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_alter_order_created_at_alter_order_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 26, 11, 0, 50, 362172)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 26, 11, 0, 50, 362189)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 26, 11, 0, 50, 362908)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 26, 11, 0, 50, 362924)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 26, 11, 0, 50, 361406)),
        ),
    ]
