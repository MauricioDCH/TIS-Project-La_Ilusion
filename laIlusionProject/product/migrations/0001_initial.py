# Generated by Django 5.1 on 2024-09-22 23:47

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id_categoria",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID de la categoría",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Categoría"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comentario",
            fields=[
                (
                    "id_comentario",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID del comentario",
                    ),
                ),
                ("texto", models.TextField(verbose_name="Comentario")),
                (
                    "fecha_comentario",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha del comentario"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Imagen",
            fields=[
                (
                    "id_imagen",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID de la imagen",
                    ),
                ),
                ("url", models.URLField(verbose_name="URL de la imagen")),
                (
                    "descripcion",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Descripción"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subcategoria",
            fields=[
                (
                    "id_subcategoria",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID de la subcategoría",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(max_length=100, verbose_name="Subcategoría"),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subcategorias",
                        to="product.categoria",
                        verbose_name="Categoría",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id_producto",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID del producto",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        max_length=255, verbose_name="Nombre del producto"
                    ),
                ),
                (
                    "precio",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Precio",
                    ),
                ),
                (
                    "descripcion",
                    models.TextField(verbose_name="Descripción del producto"),
                ),
                ("uso", models.TextField(verbose_name="Uso del producto")),
                ("marca", models.CharField(max_length=100, verbose_name="Marca")),
                (
                    "calificaciones",
                    models.DecimalField(
                        decimal_places=0,
                        max_digits=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Calificación",
                    ),
                ),
                (
                    "fecha_creacion",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de creación"
                    ),
                ),
                (
                    "fecha_modificacion",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de última modificación"
                    ),
                ),
                (
                    "esta_activo",
                    models.BooleanField(default=True, verbose_name="Activo"),
                ),
                (
                    "fecha_eliminacion",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Fecha de eliminación"
                    ),
                ),
                (
                    "acabado",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Acabado"
                    ),
                ),
                (
                    "adherencia",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Adherencia"
                    ),
                ),
                (
                    "alto",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="Alto (cm)",
                    ),
                ),
                (
                    "altura_griferia",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="Altura de la grifería (cm)",
                    ),
                ),
                (
                    "ancho",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="Ancho (cm)",
                    ),
                ),
                (
                    "areas_uso",
                    models.TextField(blank=True, verbose_name="Áreas de uso"),
                ),
                (
                    "calidad",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Calidad"
                    ),
                ),
                (
                    "capacidad_descarga",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=5,
                        null=True,
                        verbose_name="Capacidad de descarga (L)",
                    ),
                ),
                (
                    "componentes",
                    models.TextField(blank=True, verbose_name="Componentes incluidos"),
                ),
                (
                    "consumo_agua",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=5,
                        null=True,
                        verbose_name="Consumo de agua (L/min)",
                    ),
                ),
                (
                    "contenido_producto",
                    models.TextField(blank=True, verbose_name="Contenido del producto"),
                ),
                (
                    "diametro_desague",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=5,
                        null=True,
                        verbose_name="Diámetro del desagüe (cm)",
                    ),
                ),
                (
                    "dimensiones",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Dimensiones"
                    ),
                ),
                (
                    "dilucion",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Dilución"
                    ),
                ),
                (
                    "espesor",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="Espesor (cm)",
                    ),
                ),
                (
                    "forma",
                    models.CharField(blank=True, max_length=255, verbose_name="Forma"),
                ),
                (
                    "formato",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Formato"
                    ),
                ),
                ("garantia", models.TextField(blank=True, verbose_name="Garantía")),
                ("incluye", models.TextField(blank=True, verbose_name="Incluye")),
                (
                    "largo",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="Largo (cm)",
                    ),
                ),
                (
                    "lavabilidad",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Lavabilidad"
                    ),
                ),
                (
                    "longitud_brazo",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="Longitud del brazo (cm)",
                    ),
                ),
                ("materiales", models.TextField(blank=True, verbose_name="Materiales")),
                (
                    "metro_por_caja",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=3,
                        null=True,
                        verbose_name="Metro por caja",
                    ),
                ),
                ("no_incluye", models.TextField(blank=True, verbose_name="No incluye")),
                (
                    "perfil_tasa",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Perfil de tasa"
                    ),
                ),
                (
                    "piezas_por_caja",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Piezas por caja"
                    ),
                ),
                (
                    "presentacion",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Presentación"
                    ),
                ),
                (
                    "productos_compatibles",
                    models.TextField(blank=True, verbose_name="Productos compatibles"),
                ),
                (
                    "profundidad_pozo",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="Profundidad del pozo (cm)",
                    ),
                ),
                (
                    "rendimiento",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="Rendimiento",
                    ),
                ),
                (
                    "sistema_accionamiento",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name="Sistema de accionamiento",
                    ),
                ),
                (
                    "sistema_descarga",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Sistema de descarga"
                    ),
                ),
                (
                    "tiempo_abierto",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=2,
                        null=True,
                        verbose_name="Tiempo abierto (min)",
                    ),
                ),
                (
                    "tiempo_secado",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=2,
                        null=True,
                        verbose_name="Tiempo de secado (min)",
                    ),
                ),
                (
                    "tiempo_emboquillar",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=2,
                        null=True,
                        verbose_name="Tiempo para emboquillar (min)",
                    ),
                ),
                (
                    "tipo_asiento",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Tipo de asiento"
                    ),
                ),
                (
                    "tipo_chorro",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Tipo de chorro"
                    ),
                ),
                (
                    "tipo_cierre",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Tipo de cierre"
                    ),
                ),
                (
                    "tipo_griferia",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Tipo de grifería"
                    ),
                ),
                (
                    "tipo_herrajes",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Tipo de herrajes"
                    ),
                ),
                (
                    "tipo_instalacion",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Tipo de instalación"
                    ),
                ),
                (
                    "tipo_lavamanos",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Tipo de lavamanos"
                    ),
                ),
                (
                    "tipo_manija",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Tipo de manija"
                    ),
                ),
                (
                    "tipo_mezclador",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Tipo de mezclador"
                    ),
                ),
                (
                    "tipo_pintura",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Tipo de pintura"
                    ),
                ),
                (
                    "tipo_regadera",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Tipo de regadera"
                    ),
                ),
                (
                    "tipo_sifon",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Tipo de sifón"
                    ),
                ),
                (
                    "tipo_tanque",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Tipo de tanque"
                    ),
                ),
                (
                    "trafico",
                    models.DecimalField(
                        blank=True,
                        decimal_places=0,
                        max_digits=2,
                        max_length=255,
                        verbose_name="Tráfico",
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productos",
                        to="product.categoria",
                        verbose_name="Categoría",
                    ),
                ),
                (
                    "comentarios",
                    models.ManyToManyField(
                        blank=True, to="product.comentario", verbose_name="Comentarios"
                    ),
                ),
                (
                    "imagenes",
                    models.ManyToManyField(
                        to="product.imagen", verbose_name="Imágenes"
                    ),
                ),
                (
                    "subcategoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productos",
                        to="product.subcategoria",
                        verbose_name="Subcategoría",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
