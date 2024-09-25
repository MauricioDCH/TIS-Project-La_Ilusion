# forms.py
from django import forms
from .models import ProductoInventario

class ReducirCantidadForm(forms.Form):
    producto = forms.ModelChoiceField(queryset=ProductoInventario.objects.all(), label='Seleccionar Producto')
    cantidad_a_reducir = forms.IntegerField(label='Cantidad a Reducir', min_value=1)
