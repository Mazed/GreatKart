# Generated by Django 5.1.4 on 2024-12-25 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_options_alter_account_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={},
        ),
        migrations.AlterModelManagers(
            name='account',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='account',
            name='user_permissions',
        ),
    ]
