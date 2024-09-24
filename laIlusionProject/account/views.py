from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import UserRegisterForm, LoginForm
from .models import Account
from shoppingcart.models import Carrito

# Create your views here.

class RegisterView(CreateView):
    model = Account
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Siempre aseguramos que el campo 'adminAccount' sea False al crear un nuevo usuario
        form.instance.adminAccount = False
        messages.success(self.request, 'Tu cuenta se ha creado exitosamente.')
        
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm  # Esto debe ser form_class, no solo form
    redirect_authenticated_user = True  # Redirigir si ya están autenticados
    success_url = reverse_lazy('profile')  # Redirigir al perfil tras iniciar sesión

    def get_success_url(self):
        return self.success_url


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    login_url = 'login'  # Redirige a login si no está autenticado

class LogoutView(View):
    def post(self, request):
        logout(request)  # Cierra la sesión del usuario
        return redirect('inicio')  # Redirige a la página de inicio