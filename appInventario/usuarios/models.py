from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self, rut, username, nombres, apellidos, correo, password = None):
        if not correo:
            raise ValueError('Falta correo electronico')

        usuario = self.model(
            rut = rut,
            username = username,
            correo = self.normalize_email(correo),
            nombres = nombres,
            apellidos = apellidos,
            password = password
        )
        #encriptacion de contraseña
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, rut, username, nombres, apellidos, correo, password):
        usuario = self.create_user(
            rut=rut,
            username=username,
            correo = correo,
            nombres=nombres,
            apellidos=apellidos,
            password = password
        )
        usuario.user_administrador = True
        usuario.save()
        return usuario


# Create your models here.
class Usuarios(AbstractBaseUser):
    rut = models.CharField('Rut de usuario', unique=True, max_length=20)
    username = models.CharField('Cuenta de usuario', unique=True, max_length=100)
    nombres = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    correo = models.CharField('Correo electronico', unique=True, max_length=100)
    estado = models.BooleanField(default=True)
    user_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['rut', 'nombres', 'apellidos', 'correo']

    def __str__(self):
        return f'Usuario {self.rut} {self.username} {self.nombres} {self.apellidos} {self.correo}'

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.user_administrador
