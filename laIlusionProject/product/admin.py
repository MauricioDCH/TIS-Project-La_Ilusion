from django.contrib import admin
from .models import Categoria, Subcategoria, Producto, Imagen
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')

class ImagenAdmin(admin.ModelAdmin):
    list_display = ('url', 'descripcion')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'subcategoria', 'esta_activo', 'fecha_creacion')
    search_fields = ('nombre', 'categoria__nombre', 'subcategoria__nombre')
    list_filter = ('categoria', 'subcategoria', 'esta_activo')
    
    # Solo permite a los superusuarios agregar productos
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