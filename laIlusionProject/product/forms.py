from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto', 'calificacion']  # Incluye el campo de calificación
        widgets = {
            'texto': forms.Textarea(attrs={'placeholder': 'Escribe tu comentario aquí...'}),
            'calificacion': forms.Select(choices=[(i, str(i)) for i in range(1, 6)])  # Selección de calificación del 1 al 5
        }
