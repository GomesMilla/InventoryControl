from django.db import models
from django.contrib.auth.models import( BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.urls import reverse


class UsuarioManager(BaseUserManager):

    def create_user(self,email,password=None):
        usuario = self.model(email = email)
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)
        
        usuario.save()        
        return usuario
    
    def create_superuser(self,email,password):
        usuario = self.create_user(email = email, password = password)
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()
        return 

class Country(models.Model):

    """
        Models para cadastro de países do mundo
    """

    name = models.CharField('Nome do país', max_length=194)
    acronym = models.CharField('Sigla do país', max_length=10)
    dataCadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)

    class Meta:
        verbose_name = "País"
        verbose_name_plural="Países"
        ordering = ['nome']
        app_label = 'Usuarios'

    def __str__(self):
        return str(self.nome)