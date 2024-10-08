from django.contrib import admin
from .models import Categoria, Subcategoria, Producto, Imagen, Comentario

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')

class ImagenAdmin(admin.ModelAdmin):
    list_display = ('url', 'descripcion')

class ImagenInline(admin.TabularInline):
    model = Producto.imagenes.through  # Usar el modelo de relación many-to-many
    extra = 1  # Número de formularios adicionales que se mostrarán para agregar imágenes

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'subcategoria', 'esta_activo', 'fecha_creacion', 'get_imagenes')
    search_fields = ('nombre', 'categoria__nombre', 'subcategoria__nombre')
    list_filter = ('categoria', 'subcategoria', 'esta_activo')
    inlines = [ImagenInline]  # Añadir el inline para manejar imágenes

    def get_imagenes(self, obj):
        return ", ".join([img.descripcion for img in obj.imagenes.all()])  # Obtener descripciones de imágenes
    get_imagenes.short_description = 'Imágenes'  # Título para la columna

    def has_add_permission(self, request):
        return request.user.is_superuser  

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

# Registra los modelos en el admin
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)
admin.site.register(Imagen, ImagenAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Comentario)