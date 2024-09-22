from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import LoginForm

# Create your views here.
# account/views.py
from django.http import HttpResponse

# def index(request):
#    return HttpResponse("Hello, this is the account app.")


class CustomLoginView(LoginView):
    template_name = "login.html"
    form = LoginForm