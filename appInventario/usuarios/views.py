import json
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import request, HttpResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.core.serializers import serialize #permite convertir los formatos
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, View, TemplateView

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
        if request.is_ajax():
            data = serialize('json', self.get_queryset()) #formato final y consulta actual
            #convierte una serie de elementos a json, si no se le pasa una lista da un error
            #se puede convertir a lista envolviendo la respuesta  en [],
            return HttpResponse(data, 'application/json')
        else:
            #return render(request, self.template_name, self.get_context_data())
            return redirect('inicio_usuarios')


        contexto = {}
        contexto['listUsuarios'] = queryset
        contexto['num_usuarios'] = self.num_usuarios
        contexto['num_usuarios_activos'] = self.num_usuarios_activos
        contexto['num_usuarios_bloqueados'] = self.num_usuarios_bloqueados

        return render(request, self.template_name, contexto)

class CrearUsuario(CreateView):
    model = Usuarios
    form_class = CreateUserForm
    template_name = 'usuarios/crearUsuario.html'
    success_url = reverse_lazy('usuarios')
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
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
                nuevo_usuario.set_password(form.cleaned_data.get('password1'))
                nuevo_usuario.save()
                mensaje = f'Usuario registrado correctamente'
                error = 'Sin errores'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'Error al registrar usuario'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('/inicio_usuarios')

class EditarUsuario(UpdateView):
    model = Usuarios
    template_name = 'usuarios/editarUsuario.html'
    form_class = UsuarioForm
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'Usuario actualizado correctamente'
                error = 'Sin errores'
                response = JsonResponse({'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'Error al actualizar usuario'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('/inicio_usuarios')

class CambiarClave(UpdateView):
    model = Usuarios
    template_name = 'usuarios/cambiarClave.html'
    form_class = FormResetPassword
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'Contraseña actualizada de forma exitosa'
                response = JsonResponse({'mensaje':mensaje})
                response.status_code = 201
                return response
            else:
                mensaje = f'Error al actualizar la clave'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('/inicio_usuarios')

class EliminarUsuario(DeleteView):
    model = Usuarios
    success_url = reverse_lazy('usuarios')


class CambiarEstadoUsuario(DeleteView):
    def post(self, request, pk, *args, **kwargs):
        object = get_object_or_404(Usuarios, id=pk)
        if object.estado == True:
            object.estado = False
        else:
            object.estado = True
        object.save()
        return redirect('usuarios')

