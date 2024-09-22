from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.views import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Account

# Create your views here.

class RegisterView(CreateView):
    model = Account
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, 'Tu cuenta se ha creado exitosamente.')
        return super().form_valid(form)
    #fields = ['email', 'password', 'adminAccount', 'address', 'city', 'creditCard']

    
class CustomLoginView(LoginView):
    template_name = "login.html"
    form = LoginForm