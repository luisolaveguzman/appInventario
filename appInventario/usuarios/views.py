from builtins import object

from django.forms import ModelForm, EmailInput
from django.shortcuts import render, redirect

# Create your views here.
from usuarios.forms import UsuarioForm, createUserForm
from usuarios.models import Usuarios

"""
def usuarios(request):
    num_usuarios = Usuarios.objects.count()
    num_usuarios_activos = Usuarios.objects.filter(estado__exact='Activo').count() #filtro exacto
    #num_usuarios_activos = Usuarios.objects.filter(estado__icontains='Activo').count() #filtro por subcadena sin distringuir minusculas de mayusculas
    #num_usuarios_activos = Usuarios.objects.filter(estado__icontains='Activo')[:5] #este ultimo parametro traera los primeros 5 regitros
    usuarios = Usuarios.objects.order_by('id')
    return render(request, 'usuarios/usuarios.html', {'num_usuarios': num_usuarios, 'usuarios':usuarios, 'num_usuarios_activos':num_usuarios_activos})
"""

def usuarios(request):
    num_usuarios = Usuarios.objects.count()
    num_usuarios_activos = Usuarios.objects.filter(estado__icontains=True).count()
    num_usuarios_bloqueados = Usuarios.objects.filter(estado__icontains=False).count()
    usuarios = Usuarios.objects.order_by('id')
    return render(request, 'usuarios/usuarios.html', {'usuarios':usuarios, 'num_usuarios':num_usuarios, 'num_usuarios_activos':num_usuarios_activos, 'num_usuarios_bloqueados':num_usuarios_bloqueados })

def crearUsuario(request):
    if request.method == 'POST':
        #print(request.POST)
        formaUsuario = createUserForm(request.POST)
        if formaUsuario.is_valid():
            formaUsuario.save()
            return redirect('usuarios')
    else:
        formaUsuario = createUserForm()
    return render(request, 'usuarios/crearUsuario.html', {'formaUsuario':formaUsuario})