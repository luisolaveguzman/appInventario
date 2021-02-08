from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, EmailInput, TextInput, CheckboxInput, PasswordInput

from usuarios.models import Usuarios


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = [
            'rut', 'username', 'nombres', 'apellidos', 'correo', 'user_administrador']
        widgets = {
            'correo': EmailInput(
                attrs={
                    'type': 'email',
                    'placeholder':'tuCorreo@mail.cl',
                    'class':'form-control'
                }),
            'rut': TextInput(
                attrs={
                    'placeholder':'Ejemplo: 12345678-8',
                    'class':'form-control'
                }),
            'username':TextInput(attrs={'class':'form-control'}),
            'nombres':TextInput(attrs={'class':'form-control'}),
            'apellidos':TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'username':'Cuenta de usuario',
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
            'rut': TextInput(
                attrs={
                    'placeholder':'Ejemplo: 12345678-8',
                    'class':'form-control input-lg'
                }),
            'username': TextInput(attrs={'class':'form-control'}),
            'nombres': TextInput(attrs={'class':'form-control'}),
            'apellidos': TextInput(attrs={'class':'form-control'}),
            'correo': TextInput(attrs={'class':'form-control'}),
            'password1': PasswordInput(attrs={'type':'password', 'class':'form-control'}),
            'password2': PasswordInput(attrs={'type':'password', 'class':'form-control'}),
            'user_administrador': CheckboxInput(attrs={'type':'radio'})
        }


class formResetPassword(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = (
            'password1',
            'password2',
        )
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }