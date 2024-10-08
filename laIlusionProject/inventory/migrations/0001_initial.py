# Generated by Django 5.1 on 2024-09-24 23:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product", "0015_comentario_approved_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Inventario",
            fields=[
                ("id_inventario", models.AutoField(primary_key=True, serialize=False)),
                (
                    "nombre_inventario",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Nombre de inventario",
                    ),
                ),
                (
                    "ubicacion_fisica",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Almacén", "Almacén"),
                            ("Bodega 1", "Bodega 1"),
                            ("Bodega 2", "Bodega 2"),
                            ("Otro", "Otro"),
                        ],
                        default="Almacén",
                        max_length=100,
                        null=True,
                        verbose_name="Ubicación física del producto",
                    ),
                ),
                (
                    "notas_adicionales",
                    models.TextField(
                        blank=True, null=True, verbose_name="Notas adicionales"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Proveedor",
            fields=[
                ("id_proveedor", models.AutoField(primary_key=True, serialize=False)),
                (
                    "nombre",
                    models.CharField(
                        max_length=100, verbose_name="Nombre de proveedor"
                    ),
                ),
                (
                    "nombre_contacto",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Nombre de contacto",
                    ),
                ),
                (
                    "numero_contacto",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Número de contacto",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductoInventario",
            fields=[
                (
                    "id_producto_inventario",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("cantidad", models.PositiveIntegerField()),
                (
                    "unidades_de_medida",
                    models.CharField(max_length=20, verbose_name="Unidades de medida"),
                ),
                (
                    "metodo_de_adquisicion",
                    models.CharField(
                        choices=[
                            ("Compra", "Compra"),
                            ("Prestamo", "Prestamo"),
                            ("Intercambio", "Intercambio"),
                        ],
                        default="Compra",
                        max_length=50,
                        verbose_name="Método de adquisición",
                    ),
                ),
                (
                    "costo_adquisicion_por_unidad",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Costo de adquisición por unidad",
                    ),
                ),
                (
                    "fecha_adquisicion_inicial",
                    models.DateField(verbose_name="Fecha de adquisición inicial"),
                ),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("Disponible", "Disponible"),
                            ("Agotado", "Agotado"),
                            ("Reservado", "Reservado"),
                        ],
                        default="Disponible",
                        max_length=20,
                        verbose_name="Estado del producto",
                    ),
                ),
                (
                    "notas_internas",
                    models.TextField(
                        blank=True, null=True, verbose_name="Notas internas"
                    ),
                ),
                (
                    "inventario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productos",
                        to="inventory.inventario",
                    ),
                ),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productos_inventario",
                        to="product.producto",
                    ),
                ),
                (
                    "proveedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productos_proveedor",
                        to="inventory.proveedor",
                    ),
                ),
            ],
            options={
                "verbose_name": "Producto de Inventario",
                "verbose_name_plural": "Productos de Inventario",
            },
        ),
    ]
