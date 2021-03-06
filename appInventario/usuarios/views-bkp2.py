import json
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, View

# Create your views here.
from usuarios.forms import UsuarioForm, CreateUserForm, FormResetPassword
from usuarios.models import Usuarios, validarRut


class ListUsuarios(View):
    model = Usuarios
    template_name = 'usuarios/usuarios.html'

    num_usuarios = Usuarios.objects.count()
    num_usuarios_activos = Usuarios.objects.filter(estado__icontains=True).count()
    num_usuarios_bloqueados = Usuarios.objects.filter(estado__icontains=False).count()

    def get_queryset(self):
        return self.model.objects.order_by('id')

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['listUsuarios'] = self.get_queryset()
        contexto['num_usuarios'] = self.num_usuarios
        contexto['num_usuarios_activos'] = self.num_usuarios_activos
        contexto['num_usuarios_bloqueados'] = self.num_usuarios_bloqueados
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
        contexto['num_usuarios'] = self.num_usuarios
        contexto['num_usuarios_activos'] = self.num_usuarios_activos
        contexto['num_usuarios_bloqueados'] = self.num_usuarios_bloqueados

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


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            nuevo_usuario = Usuarios(
                rut = form.cleaned_data.get('rut'),
                username = form.cleaned_data.get('username'),
                nombres = form.cleaned_data.get('nombres'),
                apellidos = form.cleaned_data.get('apellidos'),
                correo = form.cleaned_data.get('correo'),
                user_administrador = form.cleaned_data.get('user_administrador'),
            )
            print(validarRut(nuevo_usuario.rut))
            #print(form)
            if validarRut(nuevo_usuario.rut):
                nuevo_usuario.set_password(form.cleaned_data.get('password1'))
                nuevo_usuario.save()
                return redirect(self.success_url)
                #print(validarRut(nuevo_usuario.rut))
            else:
                return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form':form})

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

