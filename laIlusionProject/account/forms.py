from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Account

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    class Meta:
        model = Account
        fields = ['email', 'adminAccount', 'address', 'city', 'creditCard']
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
            self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirma tu contraseña'})


class LoginForm(AuthenticationForm):
    
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)