from django.contrib import admin

# Register your models here.
from usuarios.models import Usuarios

admin.site.register(Usuarios)