from django.shortcuts import render

# Create your views here.
# order/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the order app.")
