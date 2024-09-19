from django.shortcuts import render

# Create your views here.
# product/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the product app.")
