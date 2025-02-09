# Generated by Django 5.1.5 on 2025-01-25 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_product_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 16, 42, 34, 391279)),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 16, 42, 34, 391311)),
        ),
        migrations.AlterField(
            model_name='variation',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 25, 16, 42, 34, 391849)),
        ),
    ]
