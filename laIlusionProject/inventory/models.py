from django.db import models
from product.models import Producto

# Modelo Proveedor
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre de proveedor", null=False, blank=False)
    nombre_contacto = models.CharField(max_length=100, verbose_name="Nombre de contacto", null=True, blank=True)
    numero_contacto = models.CharField(max_length=100, verbose_name="Número de contacto", null=True, blank=True)

    def __str__(self):
        return self.nombre


# Modelo ProductoInventario
class ProductoInventario(models.Model):
    id_producto_inventario = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="productos_inventario")
    inventario = models.ForeignKey('Inventario', on_delete=models.CASCADE, related_name="productos")
    cantidad = models.PositiveIntegerField()
    unidades_de_medida = models.CharField(max_length=20, verbose_name="Unidades de medida")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos_proveedor', null=False, blank=False)
    metodo_de_adquisicion = models.CharField(max_length=50, choices=[
        ('Compra', 'Compra'),
        ('Prestamo', 'Prestamo'),
        ('Intercambio', 'Intercambio')
    ], default='Compra', verbose_name="Método de adquisición", null=False, blank=False)
    costo_adquisicion_por_unidad = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo de adquisición por unidad", null=False, blank=False)
    fecha_adquisicion_inicial = models.DateField(verbose_name="Fecha de adquisición inicial", null=False, blank=False)
    estado = models.CharField(max_length=20, choices=[
        ('Disponible', 'Disponible'), 
        ('Agotado', 'Agotado'),
        ('Reservado', 'Reservado')
    ], default='Disponible', verbose_name="Estado del producto", null=False, blank=False)
    notas_internas = models.TextField(blank=True, null=True, verbose_name='Notas internas')

    @property
    def cantidad_stock(self):
        # Retornamos la cantidad del producto en este inventario
        return self.cantidad

    class Meta:
        verbose_name = "Producto de Inventario"
        verbose_name_plural = "Productos de Inventario"

    def __str__(self):
        return f'{self.producto} en {self.inventario}'


# Modelo Inventario
class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    nombre_inventario = models.CharField(max_length=100, verbose_name="Nombre de inventario", null=True, blank=True)
    ubicacion_fisica = models.CharField(max_length=100, blank=True, null=True, choices=[
            ('Almacén', 'Almacén'),
            ('Bodega 1', 'Bodega 1'),
            ('Bodega 2', 'Bodega 2'),
            ('Otro', 'Otro')
        ], default='Almacén', verbose_name='Ubicación física del producto')
    notas_adicionales = models.TextField(blank=True, null=True, verbose_name='Notas adicionales')

    def productos_en_inventario(self):
        """Retorna todos los productos asociados a este inventario."""
        return self.productos.all()

    def __str__(self):
        return self.nombre_inventario if self.nombre_inventario else f'Inventario {self.id_inventario}'
