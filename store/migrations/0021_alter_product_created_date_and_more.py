# Generated by Django 5.1.5 on 2025-01-25 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_product_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 17, 21, 11, 403240)),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 17, 21, 11, 403279)),
        ),
        migrations.AlterField(
            model_name='variation',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 17, 21, 11, 404025)),
        ),
    ]
