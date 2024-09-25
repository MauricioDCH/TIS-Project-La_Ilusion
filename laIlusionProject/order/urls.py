from django.urls import path
from .views import CrearOrdenView, VerOrdenView, ListaOrdenesView

urlpatterns = [
    path('crear/', CrearOrdenView.as_view(), name='crear_orden'),
    path('<int:orden_id>/', VerOrdenView.as_view(), name='ver_orden'),
    path('mis-ordenes/', ListaOrdenesView.as_view(), name='mis_ordenes'),
]
