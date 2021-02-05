from builtins import object

from django.forms import ModelForm, EmailInput
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from usuarios.forms import UsuarioForm, createUserForm, formResetPassword
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
    if request.method == 'POST':
        if Usuarios.objects.filter(rut__icontains=request.POST['buscar']):
            usuarios = Usuarios.objects.filter(rut__icontains=request.POST['buscar'])
        elif Usuarios.objects.filter(username__icontains=request.POST['buscar']):
            usuarios = Usuarios.objects.filter(username__icontains=request.POST['buscar'])
        elif Usuarios.objects.filter(nombres__icontains=request.POST['buscar']):
            usuarios = Usuarios.objects.filter(nombres__icontains=request.POST['buscar'])
        elif Usuarios.objects.filter(apellidos__icontains=request.POST['buscar']):
            usuarios = Usuarios.objects.filter(apellidos__icontains=request.POST['buscar'])
        elif Usuarios.objects.filter(correo__icontains=request.POST['buscar']):
            usuarios = Usuarios.objects.filter(correo__icontains=request.POST['buscar'])
        else:
            usuarios = Usuarios.objects.order_by('id')
    else:
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

def editarUsuario(request, id):
    usuario = get_object_or_404(Usuarios, pk=id)
    if request.method == 'POST':
        formaUsuario = UsuarioForm(request.POST, instance=usuario)
        if formaUsuario.is_valid():
            formaUsuario.save()
            return redirect('usuarios')
    else:
        formaUsuario = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/editarUsuario.html', {'formaUsuario':formaUsuario, 'usuario':usuario})

def cambiarClave(request, id):
    usuario = get_object_or_404(Usuarios, pk=id)
    if request.method == 'POST':
        formaUsuario = formResetPassword(request.POST, instance=usuario)
        if formaUsuario.is_valid():
            formaUsuario.save()
            return redirect('usuarios')
    else:
        formaUsuario = formResetPassword(instance=usuario)
    return render(request, 'usuarios/cambiarClave.html', {'formaUsuario':formaUsuario, 'usuario':usuario})

def cambiarEstadoUsuario(request, id):
    usuario = get_object_or_404(Usuarios, pk=id)
    if request.method == 'POST':
        if usuario.estado:
            usuario.estado = False
        else:
            usuario.estado = True
        usuario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/cambiarEstadoUsuario.html', {'usuario':usuario})

