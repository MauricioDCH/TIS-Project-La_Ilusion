from django.contrib import admin, messages
from .models import Inventario, ProductoInventario, Proveedor
from django.shortcuts import render
from .forms import ReducirCantidadForm
# Admin para ProductoInventario
class ProductoInventarioAdmin(admin.ModelAdmin):
    list_display = (
        'get_nombre',
        'get_cantidad',
        'get_unidades_de_medida',
        'get_categoria',
        'get_subcategoria',
        'get_inventario',
    )
    list_filter = ('producto__categoria', 
                   'producto__subcategoria',
                   'inventario__nombre_inventario')
    search_fields = ('producto__nombre', 
                     'producto__categoria__nombre',
                     'producto__subcategoria__nombre',
                     'inventario__nombre_inventario')
    actions = ['reducir_cantidad']

    # Métodos para acceder a los atributos del modelo Producto a través de la relación ForeignKey
    def get_nombre(self, obj):
        return obj.producto.nombre
    get_nombre.short_description = 'Nombre del Producto'

    def get_cantidad(self, obj):
        return obj.cantidad
    get_cantidad.short_description = 'Cantidad'

    def get_unidades_de_medida(self, obj):
        return obj.unidades_de_medida
    get_unidades_de_medida.short_description = 'Unidades de Medida'

    def get_categoria(self, obj):
        return obj.producto.categoria
    get_categoria.short_description = 'Categoría'

    def get_subcategoria(self, obj):
        return obj.producto.subcategoria
    get_subcategoria.short_description = 'Subcategoría'
    
    def get_inventario(self, obj):
        return obj.inventario.nombre_inventario
    get_inventario.short_description = 'Inventario'
    
    def reducir_cantidad(self, request, queryset):
        if 'apply' in request.POST:
            form = ReducirCantidadForm(request.POST)
            if form.is_valid():
                producto_inventario = form.cleaned_data['producto']
                cantidad_a_reducir = form.cleaned_data['cantidad_a_reducir']
                
                if producto_inventario.cantidad >= cantidad_a_reducir:
                    producto_inventario.cantidad -= cantidad_a_reducir
                    producto_inventario.save()
                    messages.success(request, "La cantidad se ha reducido con éxito.")
                else:
                    messages.warning(request, 
                                        f'No se puede reducir la cantidad del producto "{producto_inventario.get_nombre()}" porque solo hay {producto_inventario.cantidad} en inventario.')

                return self.response_action(request, queryset)

        else:
            form = ReducirCantidadForm()

        return render(request, 'admin/reducir_cantidad.html', {'form': form, 'queryset': queryset})

    reducir_cantidad.short_description = "Reducir Cantidad de Producto"

# Admin para Inventario
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('get_nombre_inventario', 'get_ubicacion_fisica')
    readonly_fields = ('get_nombre_inventario',)
    list_filter = ('ubicacion_fisica',)
    search_fields = ('nombre_inventario', 'ubicacion_fisica')

    # Método para mostrar el nombre del producto a través de la relación con ProductoInventario
    def get_nombre_inventario(self, obj):
        return obj.nombre_inventario
    get_nombre_inventario.short_description = 'Nombre del Inventario'
    
    def get_ubicacion_fisica(self, obj):
        return obj.ubicacion_fisica
    get_ubicacion_fisica.short_description = 'Ubicación Física'


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_contacto', 'numero_contacto')
    search_fields = ('nombre', 'nombre_contacto', 'numero_contacto')
    list_filter = ('nombre', 'nombre_contacto')
    search_fields = ('nombre', 'nombre_contacto', 'numero_contacto')
    
# Asegúrate de que esta línea aparezca solo una vez
admin.site.register(ProductoInventario, ProductoInventarioAdmin)
admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Proveedor, ProveedorAdmin)