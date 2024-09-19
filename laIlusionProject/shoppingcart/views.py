from django.shortcuts import render

# Create your views here.
# shoppingcart/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the shoppingcart app.")
