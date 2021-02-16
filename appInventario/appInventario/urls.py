"""appInventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from usuarios.views import CambiarEstadoUsuario, CambiarClave, ListUsuarios, EditarUsuario, CrearUsuario, \
    EliminarUsuario
from webapp.views import TableroView, Login, logoutUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(TableroView.as_view()), name='tablero'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('usuarios', login_required(ListUsuarios.as_view()), name='usuarios'),
    #path('crearUsuario', crearUsuario, name='crearUsuario'),
    path('crearUsuario', login_required(CrearUsuario.as_view()), name='crearUsuario'),
    path('editarUsuario/<int:pk>', login_required(EditarUsuario.as_view()), name='editarUsuario'),
    path('eliminarUsuario/<int:pk>', login_required(EliminarUsuario.as_view()), name='cambiarEstadoUsuario'),
    path('cambiarClave/<int:pk>', login_required(CambiarClave.as_view()), name='cambiarClave'),
    path('logout/', login_required(logoutUsuario), name='logout')
]

#URL de vistas implicitas
urlpatterns += [
    path('inicio_usuarios/',
             login_required(
                 TemplateView.as_view(
                     template_name = 'usuarios/usuarios.html'
                 )
             ), name='inicio_usuarios'),
]
