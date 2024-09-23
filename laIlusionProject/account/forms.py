from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Account

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico'
        })
    )

    class Meta:
        model = Account
        fields = ['email']  # Solo mostramos el campo email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Personalizamos los campos de contraseña con placeholders y clases CSS
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirma tu contraseña'
        })
        
        # Limpiamos cualquier campo extraño que pudiera heredar
        if 'password_based_authentication' in self.fields:
            del self.fields['password_based_authentication']

        # Agregamos estilos a todos los campos
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'autofocus': True, 
        'class': 'form-control',  # Clase Bootstrap
        'placeholder': 'Introduce tu email'  # Placeholder opcional
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',  # Clase Bootstrap
        'placeholder': 'Introduce tu contraseña'  # Placeholder opcional
    }))