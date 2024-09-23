from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView

urlpatterns = [
	path('', HomePageView.as_view(), name='inicio'),
	path('about/', AboutPageView.as_view(), name='nosotros'),
    path('contact/', ContactPageView.as_view(), name='contactenos'),
]