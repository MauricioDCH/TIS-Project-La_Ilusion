# Generated by Django 5.1 on 2024-09-23 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_remove_account_creditcard"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="address",
        ),
        migrations.RemoveField(
            model_name="account",
            name="city",
        ),
    ]
