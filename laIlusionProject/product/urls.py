from django.urls import path
from .views import ProductIndexView, DetalleProductoView

urlpatterns = [
    # Un ejemplo de vista básica
    path('', ProductIndexView.as_view(), name='product_index'),
    path('producto/<int:producto_id>/', DetalleProductoView.as_view(), name='detalle_producto'),
]