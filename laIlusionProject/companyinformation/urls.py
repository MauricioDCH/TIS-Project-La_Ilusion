from django.urls import path
from . import views

urlpatterns = [
    # Un ejemplo de vista básica
    path('', views.index, name='index'),
]