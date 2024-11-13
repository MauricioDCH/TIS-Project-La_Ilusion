from django.db import models
from product.models import Producto
from laIlusionProject import settings
# Create your models here.
class Carrito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Carrito de {self.usuario}"
    
    # Modelo de ItemCarrito (relaciona el carrito con productos)
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

    # Método para calcular el precio total de los productos en este item
    def get_total_price(self):
        return self.cantidad * self.producto.precio