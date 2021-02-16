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

class CreateUserForm(UserCreationForm):
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
            'correo': EmailInput(attrs={
                'type': 'email',
                'placeholder': 'tuCorreo@mail.cl',
                'class':'form-control',
                'id':'correo'
            }),
            'rut': TextInput(attrs={
                'placeholder':'Rut sin puntos y con guion medio (12345678-9)',
                'class':'form-control input-lg',
                'id':'rut'
            }),
            'username': TextInput(attrs={
                'class':'form-control',
                'placeholder':'username',
                'id':'username'
            }),
            'nombres': TextInput(attrs={
                'class':'form-control',
                'id':'nombres'
            }),
            'apellidos': TextInput(attrs={
                'class':'form-control',
                'id':'apellidos'
            }),
            'password1': PasswordInput(attrs={
                'type':'password',
                'class':'form-control',
                'id':'password1',
            }),
            'password2': PasswordInput(attrs={
                'type':'password',
                'class':'form-control',
                'id': 'password2',
            }),
            'user_administrador': CheckboxInput(attrs={
                'type':'radio'
            }),
            'estado':TextInput(attrs={
                'hidden':True
            })
        }
        labels = {
            'username':'Cuenta de usuario'
        }
        icons = {
            'rut':'far fa-times-circle'
        }




class FormResetPassword(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = (
            'password1',
            'password2',
        )
        widgets = {
            'password1': PasswordInput(attrs={
                'input_type':'password',
                'class':'form-control',
                'id':'password1'
            }),
            'password2': PasswordInput(attrs={
                'input_type': 'password',
                'class': 'form-control',
                'id':'password2'
            }),
        }



    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Ambas contraseñas deben ser iguales')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
