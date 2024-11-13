from django.contrib import admin
from .models import Orden
# Register your models here.

class OrdenAdmin(admin.ModelAdmin):
    list_display = ('orderNumber', 'orderDate', 'totalAmount', 'status', 'usuario')
    list_filter = ('status', 'usuario')
    search_fields = ('orderNumber', 'usuario__username')  # Puedes buscar por el nombre de usuario

admin.site.register(Orden, OrdenAdmin)
