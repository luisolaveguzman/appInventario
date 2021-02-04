from django import forms
from django.forms import ModelForm, EmailInput

from usuarios.models import Usuarios


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
        widgets = {
            'correo': EmailInput(attrs={'type': 'email'})
        }
"""
class UsuarioForm(forms.Form):
    rut = forms.CharField(label='Rut', widget=forms.TextInput(attrs={'placeholder':'Ejemplo: 12345678-8'}))
    nombre = forms.CharField(label='Nombre')
    apePat = forms.CharField(label='Apellido Paterno')
    apeMat = forms.CharField(label='Apellido Materno')
    correo = forms.CharField(label='Correo electronico', widget=forms.TextInput(attrs={'placeholder':'tuCorreo@mail.cl'}))
    estado = forms.CharField()
"""