# product/views.py
from django.shortcuts import render
from django.views import View
# Create your views here.
from django.http import HttpResponse
from .models import Producto

class ProductIndexView(View):
    template_name = 'index.html'
    
    def get(self, request):
        viewData = {}
        viewData["title"] = "Productos - La Ilusión Pisos y EnchapesOnline Store"
        viewData["subtitle"] = "Lista de productos"
        viewData["products"] = Producto.objects.all()
        
        return render(request, self.template_name, viewData)
    