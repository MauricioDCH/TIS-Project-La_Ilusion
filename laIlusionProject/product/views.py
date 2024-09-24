# product/views.py
from django.shortcuts import render, get_object_or_404
from django.views import View
# Create your views here.
from django.http import HttpResponse
from .models import Producto

class ProductIndexView(View):
    def get(self, request):
        # Obtener todos los productos
        productos = Producto.objects.all()

        # Crear una lista de productos con la primera imagen
        productos_con_imagen = []
        for producto in productos:
            imagenes = producto.imagenes.all()  # Usa el related_name que definiste
            primera_imagen = imagenes.first() if imagenes.exists() else None  # Obtén la primera imagen
            
            # Agregar el producto y la primera imagen a la lista
            productos_con_imagen.append({
                'producto': producto,
                'primera_imagen': primera_imagen,
            })

        # Pasar la lista de productos al template
        context = {
            'productos_con_imagen': productos_con_imagen,
        }
        return render(request, 'lista_productos.html', context)


class DetalleProductoView(View):
    def get(self, request, producto_id):
        # Obtén el producto por id_producto y todas sus imágenes
        producto = get_object_or_404(Producto, id_producto=producto_id)
        imagenes = producto.imagenes.all()  # Usa el related_name que definiste
        
        # Crear un diccionario a partir del objeto producto
        producto_dict = producto.__dict__.copy()
        producto_dict.pop('_state', None)  # Eliminamos el estado del objeto del queryset
        
        # Filtramos campos que no sean IDs ni fechas y que tengan valores no vacíos
        producto_filtrado = {campo: valor for campo, valor in producto_dict.items()
                             if valor and 'id' not in campo and 'fecha' not in campo}
        
        # Crear un nuevo diccionario donde las claves tienen guiones bajos reemplazados por espacios y están capitalizadas
        producto_dict_transformado = {}
        for campo, valor in producto_filtrado.items():
            # Reemplazar el guion bajo por un espacio y capitalizar la primera letra de cada campo
            campo_transformado = campo.replace('_', ' ').capitalize()
            producto_dict_transformado[campo_transformado] = valor
        
        # Preparar el contexto para pasar al template
        context = {
            'producto': producto,
            'producto_dict': producto_dict_transformado,  # Pasamos el diccionario transformado al contexto
            'imagenes': imagenes,
        }
        return render(request, 'detalle_producto.html', context)