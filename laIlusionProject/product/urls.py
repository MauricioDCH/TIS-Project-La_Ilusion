from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ProductIndexView, DetalleProductoView, GenerarReporteView

urlpatterns = [
    # Un ejemplo de vista básica
    path('', ProductIndexView.as_view(), name='product_index'),
    path('producto/<int:producto_id>/', DetalleProductoView.as_view(), name='detalle_producto'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)