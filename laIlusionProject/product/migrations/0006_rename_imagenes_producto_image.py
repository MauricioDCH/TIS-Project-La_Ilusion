# Generated by Django 5.1 on 2024-09-23 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0005_remove_producto_imag_producto_imagenes"),
    ]

    operations = [
        migrations.RenameField(
            model_name="producto",
            old_name="imagenes",
            new_name="image",
        ),
    ]
