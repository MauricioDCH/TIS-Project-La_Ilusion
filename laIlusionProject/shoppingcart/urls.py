from django.urls import path
from . import views

urlpatterns = [
    # Un ejemplo de vista básica
    #path('', views.index, name='index'),
    path('agregar/<int:producto_id>/', views.AgregarAlCarritoView.as_view(), name='agregar_al_carrito'),
    path('carrito/', views.VerCarritoView.as_view(), name='ver_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.EliminarDelCarritoView.as_view(), name='eliminar_del_carrito'),

]
