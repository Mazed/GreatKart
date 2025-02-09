# Generated by Django 5.1.5 on 2025-01-27 08:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_alter_order_created_at_alter_order_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 27, 15, 0, 9, 807687)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 27, 15, 0, 9, 807698)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 27, 15, 0, 9, 808229)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 27, 15, 0, 9, 808240)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 27, 15, 0, 9, 807040)),
        ),
    ]
