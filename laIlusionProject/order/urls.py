from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import CrearOrdenView, VerOrdenView, ListaOrdenesView, OrdenExistenteView, BorrarOrdenView

urlpatterns = [
    path('crear/', CrearOrdenView.as_view(), name='crear_orden'),
    path('<int:orden_id>/', VerOrdenView.as_view(), name='ver_orden'),
    path('mis-ordenes/', ListaOrdenesView.as_view(), name='mis_ordenes'),
    path('orden_existente/', OrdenExistenteView.as_view(), name='orden_existente'),
    path('borrar/<int:orden_id>/', BorrarOrdenView.as_view(), name='borrar_orden'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)