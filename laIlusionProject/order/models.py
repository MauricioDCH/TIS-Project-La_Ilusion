from django.db import models
from django.conf import settings
from shoppingcart.models import Carrito

class Orden(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSED', 'Processed'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    # Parámetros requeridos
    orderNumber = models.AutoField(primary_key=True, unique=True)
    orderDate = models.DateTimeField(auto_now_add=True)  # Fecha de creación de la orden
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Monto total de la orden
    shoppingCart = models.OneToOneField(Carrito, on_delete=models.CASCADE)  # Carrito asociado a la orden
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')  # Estado de la orden
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=-1)

    def __str__(self):
        return f"Orden {self.orderNumber} - {self.get_status_display()}"
