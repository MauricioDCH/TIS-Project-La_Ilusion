from django.shortcuts import get_object_or_404, redirect
from product.models import Producto
from .models import Carrito, ItemCarrito
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

# Create your views here.

class AgregarAlCarritoView(LoginRequiredMixin, View):
    def post(self, request, producto_id):
        producto = get_object_or_404(Producto, pk = producto_id)
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)

        # Verifica si el producto ya está en el carrito
        item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)

        if not created:
            # Si el producto ya está en el carrito, aumenta la cantidad
            item.cantidad += 1
            item.save()

        return redirect('ver_carrito')  # Redirige a la vista del carrito
    

class VerCarritoView(LoginRequiredMixin, DetailView):
    model = Carrito
    template_name = 'ver_carrito.html'
    context_object_name = 'carrito'

    def get_object(self):
        # Obtiene el carrito del usuario actual
        return Carrito.objects.get(usuario=self.request.user)
    


class EliminarDelCarritoView(LoginRequiredMixin, View):
    def post(self, request, item_id):
        # Obtiene el carrito del usuario
        carrito = get_object_or_404(Carrito, usuario=request.user)
        # Busca el ítem del carrito por su ID
        item = get_object_or_404(ItemCarrito, id=item_id, carrito=carrito)
        # Elimina el ítem del carrito
        item.delete()

        # Redirige de nuevo a la vista del carrito
        return redirect('ver_carrito')