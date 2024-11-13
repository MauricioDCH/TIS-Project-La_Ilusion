from django.shortcuts import get_object_or_404, render, redirect
from product.models import Producto
from .models import Carrito, ItemCarrito
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

# Vistas

class AgregarAlCarritoView(LoginRequiredMixin, View):
    login_url = 'login'  # Redirige a la página de login si no está autenticado
    
    def post(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)

        # Verifica si el producto ya está en el carrito
        item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)

        if not created:
            # Si el producto ya está en el carrito, aumenta la cantidad
            item.cantidad += 1
            item.save()

        return redirect('ver_carrito')  # Redirige a la vista del carrito
    

class VerCarritoView(LoginRequiredMixin, DetailView):
    login_url = 'login'  # Redirige a la página de login si no está autenticado
    model = Carrito
    template_name = 'ver_carrito.html'
    context_object_name = 'carrito'

    def get_object(self):
        # Obtiene el carrito del usuario actual
        return Carrito.objects.get(usuario=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carrito = self.get_object()

        # Obtener los productos en el carrito
        productos_con_imagen = []
        for item in carrito.items.all():  # Aquí usas los elementos del carrito, no todos los productos
            producto = item.producto
            imagenes = producto.imagenes.all()  # Usa el related_name que definiste
            primera_imagen = imagenes.first() if imagenes.exists() else None  # Obtén la primera imagen
            
            # Agregar el producto y la primera imagen a la lista
            productos_con_imagen.append({
                'producto': producto,
                'cantidad': item.cantidad,
                'primera_imagen': primera_imagen,
                'total_producto': item.get_total_price()  # Suponiendo que `get_total_price` devuelve el total de un producto
            })

        # Calcula el total a pagar
        total_a_pagar = sum(item.get_total_price() * item.cantidad for item in carrito.items.all())
        
        # Agrega los productos con imágenes y el total a pagar al contexto
        context['total_a_pagar'] = total_a_pagar
        context['productos_con_imagen'] = productos_con_imagen

        return context





class EliminarDelCarritoView(LoginRequiredMixin, View):
    login_url = 'login'  # Redirige a la página de login si no está autenticado
    
    def post(self, request, item_id):
        # Obtiene el carrito del usuario
        carrito = get_object_or_404(Carrito, usuario=request.user)
        # Busca el ítem del carrito por su ID
        item = get_object_or_404(ItemCarrito, id=item_id, carrito=carrito)
        # Elimina el ítem del carrito
        item.delete()

        # Redirige de nuevo a la vista del carrito
        return redirect('ver_carrito')


class ComprarView(LoginRequiredMixin, View):
    login_url = 'login'  # Redirige a la página de login si no está autenticado
    
    def post(self, request):
        return redirect('confirmacion_compra')


class ConfirmacionCompraView(LoginRequiredMixin, View):
    login_url = 'login'  # Redirige a la página de login si no está autenticado
    
    def get(self, request):
        return render(request, 'confirmacion_compra.html')
