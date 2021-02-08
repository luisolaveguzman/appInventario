from builtins import object

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

# Create your views here.
from usuarios.forms import UsuarioForm, createUserForm, formResetPassword
from usuarios.models import Usuarios

class ListUsuarios(ListView):
    model = Usuarios
    template_name = 'usuarios/usuarios.html'
    context_object_name = 'listUsuarios'
    queryset = Usuarios.objects.order_by('id')

    def post(self, request, queryset, *args, **kwargs):
        queryset = request.POST.get('buscar')
        if queryset:
            queryset = Usuarios.objects.filter(
            Q(rut__icontains=queryset)|
            Q(username__icontains=queryset)|
            Q(nombres__icontains=queryset)|
            Q(apellidos__icontains=queryset)|
            Q(correo__icontains=queryset)
        )
        else:
            queryset = Usuarios.objects.order_by('id')

    # paginador
    # paginador = Paginator(usuarios, 10)
    # page = request.GET.get('page')
    # usuarios = paginador.get_page(page)


class CrearUsuario(CreateView):
    model = Usuarios
    form_class = createUserForm
    template_name = 'usuarios/crearUsuario.html'
    success_url = reverse_lazy('usuarios')

class EditarUsuario(UpdateView):
    model = Usuarios
    template_name = 'usuarios/editarUsuario.html'
    context_object_name = 'formaUsuario'
    form_class = UsuarioForm # le pasa al template el fomulario, se interpreta en el template como form
    success_url = reverse_lazy('usuarios')

class CambiarClave(UpdateView):
    model = Usuarios
    template_name = 'usuarios/cambiarClave.html'
    form_class = formResetPassword
    success_url = reverse_lazy('usuarios')

class CambiarEstadoUsuario(DeleteView):
    model = Usuarios

    def post(self, request, pk, *args, **kwargs):
        object = get_object_or_404(Usuarios, id=pk)
        if object.estado == True:
            object.estado = False
        else:
            object.estado = True
        object.save()
        return redirect('usuarios')

#def usuarios(request):
 #   num_usuarios = Usuarios.objects.count()
  #  num_usuarios_activos = Usuarios.objects.filter(estado__icontains=True).count()
    #  num_usuarios_bloqueados = Usuarios.objects.filter(estado__icontains=False).count()
    #queryset = request.POST.get('buscar')
    #if queryset:
        #    usuarios = Usuarios.objects.filter(
        #    Q(rut__icontains=queryset)|
        #    Q(username__icontains=queryset)|
        #    Q(nombres__icontains=queryset)|
        #    Q(apellidos__icontains=queryset)|
        #    Q(correo__icontains=queryset)
        #)
        #else:
        #usuarios = Usuarios.objects.order_by('id')

    #paginador
    #paginador = Paginator(usuarios, 10)
    #page = request.GET.get('page')
    #usuarios = paginador.get_page(page)

    #return render(request, 'usuarios/usuarios.html', {'usuarios':usuarios, 'num_usuarios':num_usuarios, 'num_usuarios_activos':num_usuarios_activos, 'num_usuarios_bloqueados':num_usuarios_bloqueados })


#def crearUsuario(request):
 #   if request.method == 'POST':
  #      formaUsuario = createUserForm(request.POST)
   #     if formaUsuario.is_valid():
    #        formaUsuario.save()
     #       return redirect('usuarios')
    #else:
     #   formaUsuario = createUserForm()
    #return render(request, 'usuarios/crearUsuario.html', {'formaUsuario':formaUsuario})

#def editarUsuario(request, id):
 #   usuario = get_object_or_404(Usuarios, pk=id)
   # if request.method == 'POST':
    #    formaUsuario = UsuarioForm(request.POST, instance=usuario)
     #   if formaUsuario.is_valid():
      #      formaUsuario.save()
       #     return redirect('usuarios')
    #else:
     #   formaUsuario = UsuarioForm(instance=usuario)
    #return render(request, 'usuarios/editarUsuario.html', {'formaUsuario':formaUsuario, 'usuario':usuario})

#def cambiarClave(request, id):
 #   usuario = get_object_or_404(Usuarios, pk=id)
  #  if request.method == 'POST':
   #     formaUsuario = formResetPassword(request.POST, instance=usuario)
    #    if formaUsuario.is_valid():
     #       formaUsuario.save()
      #      return redirect('usuarios')
    #else:
     #   formaUsuario = formResetPassword(instance=usuario)
    #return render(request, 'usuarios/cambiarClave.html', {'formaUsuario':formaUsuario, 'usuario':usuario})

#def cambiarEstadoUsuario(request, id):
 #   usuario = get_object_or_404(Usuarios, pk=id)
  #  if request.method == 'POST':
  #      if usuario.estado:
   #         usuario.estado = False
    #    else:
     #       usuario.estado = True
      #  usuario.save()
       # return redirect('usuarios')
    #return render(request, 'usuarios/cambiarEstadoUsuario.html', {'usuario':usuario})

