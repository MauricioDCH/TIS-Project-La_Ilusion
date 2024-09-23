from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, RegisterView, ProfileView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # URL para enviar correo de recuperación de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    
    # URL que muestra el mensaje de éxito después de enviar el correo
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    
    # URL para el enlace enviado en el correo (para restablecer la contraseña)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    
    # URL de éxito después de restablecer la contraseña
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]