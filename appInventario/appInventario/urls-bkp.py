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

from usuarios.views import CambiarEstadoUsuario, CambiarClave, ListUsuarios, EditarUsuario, CrearUsuario
from webapp.views import TableroView, Login

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', tablero, name='tablero'),
    path('', login_required(TableroView.as_view()), name='tablero'),
    path('/accounts/login/', Login.as_view(), name='login'),
    #path('usuarios', usuarios, name='usuarios'),
    path('usuarios', ListUsuarios.as_view(), name='usuarios'),
    #path('crearUsuario', crearUsuario, name='crearUsuario'),
    path('crearUsuario', CrearUsuario.as_view(), name='crearUsuario'),
    #path('editarUsuario/<int:id>', editarUsuario, name='editarUsuario'),
    path('editarUsuario/<int:pk>', EditarUsuario.as_view(), name='editarUsuario'),
    #path('cambiarEstadoUsuario/<int:id>', cambiarEstadoUsuario, name='cambiarEstadoUsuario'),
    path('cambiarEstadoUsuario/<int:pk>', CambiarEstadoUsuario.as_view(), name='cambiarEstadoUsuario'),
    #path('cambiarClave/<int:id>', cambiarClave, name='cambiarClave'),
    path('cambiarClave/<int:pk>', CambiarClave.as_view(), name='cambiarClave'),
]
