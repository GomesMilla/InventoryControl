from django.db import models
from django.contrib.auth.models import( BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.urls import reverse


from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel, TitleSlugDescriptionModel, ActivatorModel


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

class Country(TitleSlugDescriptionModel,TimeStampedModel,ActivatorModel, models.Model):

    """
        Models para cadastro de países do mundo.
        Atríbutos da classe title, description, status, activate_date, deactivate_date, created, modified
        slug
    """

    def slugify_function(self, content):
        """
            This function will be used to slugify
            the title (default `populate_from` field)
        """
        return content.replace('_', '-').lower()

    class Meta:
        verbose_name = "Country"
        verbose_name_plural="Countries"
        ordering = ['title']
        app_label = 'Users'

    def __str__(self):
        return str(self.title)


class User(AbstractBaseUser,PermissionsMixin):

    """
        Models para cadastro de pessoas com a reescrita do model user padrão do Django
    """

    STATUS_GENERO = [
        ("FEMININO", "Feminino"),
        ("MASCULINO", "Masculino"),
        ("OUTRO", "Outro"),
    ]

    ESCOLARIDADE = [
        ("EFI", "Ensino fundamental incompleto"),
        ("EFC", "Ensino fundamental completo"),
        ("EMI", "Ensino médio incompleto"),
        ("EMC", "Ensino médio completo"),
        ("ESI", "Ensino superior incompleto"),
        ("ESC", "Ensino superior completo"),
    ]


    name = models.CharField('Nome completo', max_length=60)
    country = models.ForeignKey("Pais", on_delete=models.CASCADE, related_name="PaisUsuario", blank=True, null=True)
    escolaridade = models.CharField('Escolaridade', max_length=3, choices=ESCOLARIDADE, blank=True, null=True)
    genero = models.CharField('Genero', max_length=10, choices=STATUS_GENERO, blank=True, null=True)
    email = models.EmailField('E-mail', unique=True)
    telefoneCelular = models.CharField('Número de telefone', max_length=19, unique=True)
    cpf = models.CharField(verbose_name='CPF', max_length=14, unique=True)
    dataDascimento = models.DateField('Data de nascimento', auto_now=False, auto_now_add=False, blank=True, null=True)
    cep = models.CharField('CEP', max_length=11, blank=True, null=True)
    estado = models.CharField('Estado',max_length=30, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=194, blank=True, null=True)
    bairro = models.CharField('Bairro',max_length=194, blank=True, null=True)
    logradouro = models.CharField('Logradouro', max_length=194, blank=True, null=True)
    numero = models.CharField('Número da residencia', max_length=194, blank=True, null=True)
    idGroup = models.IntegerField(verbose_name = 'Id do grupo', default = 5)
    dataCadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)
    dataDesativacao = models.DateField('Data de nascimento', blank=True, null=True)
    is_active = models.BooleanField(verbose_name="Usuário está ativo",default=True)
    is_staff  = models.BooleanField(verbose_name="Usuário é da equipe de desenvolvimento",default= False)
    is_superuser = models.BooleanField(verbose_name= "Usuário é um superusuario",default=False)

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ['nome', 'telefoneCelular', 'cpf']

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural="Pessoas"
        ordering = ['nome']
        app_label = 'Usuarios'

    def __str__(self):
        return str(self.nome)