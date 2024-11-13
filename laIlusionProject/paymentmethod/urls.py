from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import ConfirmacionCompraView, ComprarAhoraView

urlpatterns = [
    # Un ejemplo de vista básica
    path('', views.index, name='index'),
    path('comprar/', ComprarAhoraView.as_view(), name='comprar_ahora'),
    path('compra-exitosa/', ConfirmacionCompraView.as_view(), name='confirmacion_compra'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)