from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from .models import Orden
from shoppingcart.models import Carrito
from django.views.generic import DetailView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin



class CrearOrdenView(LoginRequiredMixin, View):
    login_url = 'login'  # Redirige a la página de login si no está autenticado
    def post(self, request):
        # Obtener el carrito del usuario (puedes usar el carrito activo o el que desees)
        carrito = get_object_or_404(Carrito, usuario=request.user)

        # Crear una nueva orden
        orden = Orden.objects.create(
            shoppingCart=carrito,
            totalAmount=0,  # Este valor se actualizará después
            usuario=request.user,
        )

        # Calcular el total de la orden
        total = sum(item.cantidad * item.producto.precio for item in carrito.items.all())
        orden.totalAmount = total
        orden.save()

        # Vaciar el carrito después de generar la orden (opcional)
        carrito.items.all().delete()

        return redirect('ver_orden', orden_id=orden.orderNumber)

    def get(self, request):
        # Renderizar el formulario para crear una nueva orden
        return render(request, 'order/crear_orden.html')

class OrdenExistenteView(LoginRequiredMixin, View):
    login_url = 'login'  # Redirige a la página de login si no está autenticado
    def get(self, request):
        # Aquí puedes mostrar un mensaje informando al usuario
        return render(request, 'orden_existente.html')
class BorrarOrdenView(LoginRequiredMixin, View):
    login_url = 'login'  # Redirige a la página de login si no está autenticado
    def post(self, request, orden_id):
        # Obtener la orden a eliminar
        orden = get_object_or_404(Orden, pk=orden_id, usuario=request.user)
        
        # Eliminar la orden
        orden.delete()

        # Redirigir a la lista de órdenes después de eliminar
        return redirect('mis_ordenes')

class VerOrdenView(LoginRequiredMixin,DetailView):
    login_url = 'login'  # Redirige a la página de login si no está autenticado
    model = Orden
    template_name = 'ver_orden.html'
    context_object_name = 'orden'

    def get_object(self):
        # Asegurarse de que el usuario solo pueda ver sus propias órdenes
        return get_object_or_404(Orden, pk=self.kwargs['orden_id'], usuario=self.request.user)

class ListaOrdenesView(LoginRequiredMixin, ListView):
    login_url = 'login'  # Redirige a la página de login si no está autenticado
    model = Orden
    template_name = 'mis_ordenes.html'  # Plantilla que vamos a crear
    context_object_name = 'ordenes'  # Nombre que usaremos en el template

    def get_queryset(self):
        # Devolver solo las órdenes del usuario autenticado
        return Orden.objects.filter(usuario=self.request.user).order_by('-orderDate')