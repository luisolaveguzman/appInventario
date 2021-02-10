from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, View

# Create your views here.
from usuarios.forms import UsuarioForm, CreateUserForm, FormResetPassword
from usuarios.models import Usuarios

class ListUsuarios(View):
    model = Usuarios
    template_name = 'usuarios/usuarios.html'

    def get_queryset(self):
        return self.model.objects.order_by('id')

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['listUsuarios'] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
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
        contexto = {}
        contexto['listUsuarios'] = queryset
            
        return render(request, self.template_name, contexto)

    # paginador
    # paginador = Paginator(usuarios, 10)
    # page = request.GET.get('page')
    # usuarios = paginador.get_page(page)


class CrearUsuario(CreateView):
    model = Usuarios
    form_class = CreateUserForm
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
    form_class = FormResetPassword
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

