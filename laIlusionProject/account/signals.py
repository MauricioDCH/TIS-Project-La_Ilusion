from django.db.models.signals import post_save
from django.dispatch import receiver
from shoppingcart.models import Carrito
from .models import Account

@receiver(post_save, sender=Account)
def crear_carrito_automáticamente(sender, instance, created, **kwargs):
    if created:
        # Se crea un carrito asociado al usuario si el usuario ha sido creado
        Carrito.objects.create(usuario=instance)
