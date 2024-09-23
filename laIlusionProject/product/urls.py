from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductIndexView

urlpatterns = [
    # Un ejemplo de vista básica
    path('', ProductIndexView.as_view(), name='product_index'),  # Página de listado de productos
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
