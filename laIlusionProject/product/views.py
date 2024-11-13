# product/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Avg
from django.http import HttpResponse
from .models import Producto
from .forms import ComentarioForm
from .generators.pdf_generator import PDFReporteGenerator
from .generators.excel_generator import ExcelReporteGenerator
# Create your views here.

class ProductIndexView(View):
    def get(self, request):
        # Obtener todos los productos
        productos = Producto.objects.all()

        busqueda = request.GET.get('busqueda', '')
        # Filtrar productos si se proporciona un término de búsqueda
        if busqueda:
            productos = productos.filter(nombre__icontains=busqueda)
        
        # Verificar si se debe ordenar por categoría
        ordenar_por_categoria = request.GET.get('ordenar', None)

        if ordenar_por_categoria:
            # Ordenar productos por categoría
            productos = productos.order_by('categoria__nombre')

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
            'title':'Lista de Productos - La Ilusión Pisos y Enchapes',
            'subtitle':'Lista de Productos',
            'productos_con_imagen': productos_con_imagen,
            'busqueda': busqueda,
        }
        return render(request, 'lista_productos.html', context)

@method_decorator(login_required(login_url='login'), name='post')
class DetalleProductoView(View):
    def get(self, request, producto_id):
        # Obtén el producto por id_producto y todas sus imágenes
        producto = get_object_or_404(Producto, id_producto=producto_id)
        imagenes = producto.imagenes.all()  # Usa el related_name que definiste

        # Obtener comentarios relacionados con el producto
        comentarios = producto.comentarios.all()

        # Calcular el promedio de calificaciones
        promedio_calificacion = producto.comentarios.aggregate(Avg('calificacion'))['calificacion__avg']

        # Crear un nuevo formulario de comentario
        comentario_form = ComentarioForm()

        # Crear un diccionario a partir del objeto producto
        producto_dict = producto.__dict__.copy()
        producto_dict.pop('_state', None)  # Eliminamos el estado del objeto del queryset

        # Filtramos campos que no sean IDs ni fechas y que tengan valores no vacíos
        producto_filtrado = {campo: valor for campo, valor in producto_dict.items()
                             if valor and 'id' not in campo and 'fecha' not in campo and 'activo' not in campo}

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
            'comentarios': comentarios,  # Pasamos los comentarios al contexto
            'promedio_calificacion': promedio_calificacion,  # Pasamos el promedio de calificación
            'comentario_form': comentario_form,  # Formulario para agregar comentario
        }
        return render(request, 'detalle_producto.html', context)

    def post(self, request, producto_id):
        login_url = 'login'  # Redirige a la página de login si no está autenticado
        # Obtener el producto
        producto = get_object_or_404(Producto, id_producto=producto_id)

        # Procesar el formulario de comentario
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.usuario = request.user  # Asignar el usuario autenticado
            comentario.producto = producto  # Asegurarse de asociar el comentario con el producto
            comentario.save()  # Guardar el comentario en la base de datos

            # Redirigir al detalle del producto después de añadir el comentario
            return redirect('detalle_producto', producto_id=producto_id)  
        else:
            print("Este es el error:", comentario_form.errors)  # Imprime los errores en el registro
            # Si el formulario no es válido, reconstruir el contexto completo
            imagenes = producto.imagenes.all()
            comentarios = producto.comentarios.all()
            promedio_calificacion = producto.comentarios.aggregate(Avg('calificacion'))['calificacion__avg']

            # Crear un diccionario a partir del objeto producto
            producto_dict = producto.__dict__.copy()
            producto_dict.pop('_state', None)

            # Filtrar campos
            producto_filtrado = {campo: valor for campo, valor in producto_dict.items()
                                 if valor and 'id' not in campo and 'fecha' not in campo and 'activo' not in campo}

            # Transformar el diccionario
            producto_dict_transformado = {campo.replace('_', ' ').capitalize(): valor for campo, valor in producto_filtrado.items()}

            # Crear el contexto que incluye errores del formulario
            context = {
                'producto': producto,
                'producto_dict': producto_dict_transformado,
                'imagenes': imagenes,
                'comentarios': comentarios,
                'promedio_calificacion': promedio_calificacion,
                'comentario_form': comentario_form,  # Incluir el formulario con errores
            }
            return render(request, 'detalle_producto.html', context)

class GenerarReporteView(View):
    """Clase basada en vista que genera un reporte según el formato especificado (PDF o Excel)."""
    
    def get(self, request, formato):
        """Método que maneja la solicitud GET para generar el reporte."""
        
        # Obtener todos los productos de la base de datos
        productos = Producto.objects.all()

        if formato == 'pdf':
            generador = PDFReporteGenerator()
            generador.generar_reporte(productos)
            with open("reporte_productos.pdf", "rb") as f:
                response = HttpResponse(f.read(), content_type="application/pdf")
                response['Content-Disposition'] = 'inline; filename="reporte_productos.pdf"'
                return response
            
        elif formato == 'excel':
            generador = ExcelReporteGenerator()
            generador.generar_reporte(productos)
            with open("reporte_productos.xlsx", "rb") as f:
                response = HttpResponse(f.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                response['Content-Disposition'] = 'inline; filename="reporte_productos.xlsx"'
                return response
        else:
            return HttpResponse("Formato no soportado", status=400)