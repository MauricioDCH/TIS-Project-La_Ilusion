# Create your views here.
# paymentmethod/views.py
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the paymentmethod app.")

class ConfirmacionCompraView(LoginRequiredMixin, View):
    login_url = 'login'  # Redirige a la página de login si no está autenticado
    
    def get(self, request):
        return render(request, 'confirmacion_compra.html')

class ComprarAhoraView(LoginRequiredMixin, View):
    login_url = 'login'  # Redirige a la página de login si no está autenticado
    
    def get(self, request):
        return render(request, 'payment.html')