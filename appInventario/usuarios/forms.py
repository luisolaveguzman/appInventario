from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, EmailInput, TextInput

from usuarios.models import Usuarios


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['rut', 'username', 'nombres', 'apellidos', 'correo', 'user_administrador']
        widgets = {
            'correo': EmailInput(attrs={'type': 'email', 'placeholder':'tuCorreo@mail.cl'}),
            'rut': TextInput(attrs={'placeholder':'Ejemplo: 12345678-8'})
        }

class createUserForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = (
            'rut',
            'username',
            'nombres',
            'apellidos',
            'correo',
            'password1',
            'password2',
            'user_administrador',
        )
        widgets = {
            'correo': EmailInput(attrs={'type': 'email', 'placeholder': 'tuCorreo@mail.cl'}),
            'rut': TextInput(attrs={'placeholder': 'Ejemplo: 12345678-8'})
        }
