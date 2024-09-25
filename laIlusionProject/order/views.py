from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from .models import Orden
from shoppingcart.models import Carrito
from django.views.generic import DetailView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin



class CrearOrdenView(View):
    def post(self, request):
        # Obtener el carrito del usuario
        carrito = get_object_or_404(Carrito, usuario=request.user)

        if not carrito.items.exists():
            return redirect('ver_carrito')

        # Crear la orden
        orden = Orden.objects.create(
            shoppingCart=carrito,
            totalAmount=0,  
            usuario=request.user,
        )

        print(carrito.items.all())
        # Calcular el total de la orden
        total = sum(item.cantidad * item.producto.precio for item in carrito.items.all())
        orden.totalAmount = total
        orden.save()

        # Vaciar el carrito después de generar la orden
        carrito.items.all().delete()

        return redirect('ver_orden', orden_id=orden.orderNumber)
    
class VerOrdenView(DetailView):
    model = Orden
    template_name = 'ver_orden.html'
    context_object_name = 'orden'

    def get_object(self):
        # Asegurarse de que el usuario solo pueda ver sus propias órdenes
        return get_object_or_404(Orden, pk=self.kwargs['orden_id'], usuario=self.request.user)
    


class ListaOrdenesView(LoginRequiredMixin, ListView):
    model = Orden
    template_name = 'mis_ordenes.html'  # Plantilla que vamos a crear
    context_object_name = 'ordenes'  # Nombre que usaremos en el template

    def get_queryset(self):
        # Devolver solo las órdenes del usuario autenticado
        return Orden.objects.filter(usuario=self.request.user).order_by('-orderDate')