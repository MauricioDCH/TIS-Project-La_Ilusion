from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from .models import Categoria, Subcategoria, Producto, Imagen, Comentario
from .generators.excel_generator import ExcelReporteGenerator  # Asegúrate de tener este módulo
from .generators.pdf_generator import PDFReporteGenerator  # Asegúrate de tener este módulo

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')

class ImagenAdmin(admin.ModelAdmin):
    list_display = ('url', 'descripcion')

class ImagenInline(admin.TabularInline):
    model = Producto.imagenes.through  # Usar el modelo de relación many-to-many
    extra = 1  # Número de formularios adicionales para agregar imágenes

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'subcategoria', 'esta_activo', 'fecha_creacion', 'get_imagenes')
    search_fields = ('nombre', 'categoria__nombre', 'subcategoria__nombre')
    list_filter = ('categoria', 'subcategoria', 'esta_activo')
    inlines = [ImagenInline]  # Inline para manejar imágenes

    # Obtiene y muestra las descripciones de las imágenes
    def get_imagenes(self, obj):
        return ", ".join([img.descripcion for img in obj.imagenes.all()])
    get_imagenes.short_description = 'Imágenes'

    # Restringe permisos de añadir, cambiar y eliminar a solo superusuarios
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    # Genera reporte en Excel solo si el usuario es administrador
    def generar_reporte_excel(self, request):
        if not request.user.is_superuser:
            return HttpResponse("Acceso denegado: solo los administradores pueden generar este reporte.")

        productos = Producto.objects.all()
        excel_generator = ExcelReporteGenerator()
        excel_generator.generar_reporte(productos)
        with open("reporte_productos.xlsx", "rb") as f:
            response = HttpResponse(f.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = 'inline; filename="reporte_productos.xlsx"'
            return response
        
        return HttpResponse("Reporte en Excel generado exitosamente.")

    # Genera reporte en PDF solo si el usuario es administrador
    def generar_reporte_pdf(self, request):
        if not request.user.is_superuser:
            return HttpResponse("Acceso denegado: solo los administradores pueden generar este reporte.")

        productos = Producto.objects.all()
        pdf_generator = PDFReporteGenerator()
        pdf_generator.generar_reporte(productos)
        with open("reporte_productos.pdf", "rb") as f:
            response = HttpResponse(f.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename="reporte_productos.pdf"'
            return response
        
        return HttpResponse("Reporte en PDF generado exitosamente.")

    # Configura URLs para la generación de reportes
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("generar-reporte-excel/", self.admin_site.admin_view(self.generar_reporte_excel), name="generar-reporte-excel"),
            path("generar-reporte-pdf/", self.admin_site.admin_view(self.generar_reporte_pdf), name="generar-reporte-pdf"),
        ]
        return custom_urls + urls

    # Agrega botones en la interfaz de administración para los reportes
    change_list_template = "admin/producto_change_list.html"

# Registra los modelos en el admin
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)
admin.site.register(Imagen, ImagenAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Comentario)
