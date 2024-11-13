from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import AgregarAlCarritoView, VerCarritoView, EliminarDelCarritoView, ComprarView, ConfirmacionCompraView

urlpatterns = [
    # Un ejemplo de vista básica
    #path('', views.index, name='index'),
    path('carrito/', VerCarritoView.as_view(), name='ver_carrito'),
    path('comprar/', ComprarView.as_view(), name='comprar'),
    path('compra-exitosa/', ConfirmacionCompraView.as_view(), name='confirmacion_compra'),
    path('agregar/<int:producto_id>/', AgregarAlCarritoView.as_view(), name='agregar_al_carrito'),
    path('carrito/eliminar/<int:item_id>/', EliminarDelCarritoView.as_view(), name='eliminar_del_carrito'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)