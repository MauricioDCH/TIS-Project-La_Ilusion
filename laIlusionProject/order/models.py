from django.db import models
from django.conf import settings
from shoppingcart.models import Carrito
from django.core.mail import send_mail

class Orden(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSED', 'Processed'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    orderNumber = models.AutoField(primary_key=True, unique=True)
    orderDate = models.DateTimeField(auto_now_add=True)
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shoppingCart = models.ForeignKey(Carrito, on_delete=models.CASCADE)  # Un carrito puede tener múltiples órdenes
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=-1)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_status = Orden.objects.get(pk=self.pk).status
            if old_status != self.status and self.status == 'PROCESSED':
                send_mail(
                    'Tu orden ha sido procesada',
                    f'Tu orden {self.orderNumber} ha sido procesada.',
                    'from@example.com',
                    [self.usuario.email],
                    fail_silently=False,
                )
        super().save(*args, **kwargs)
