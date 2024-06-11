import re
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class Usuario(AbstractBaseUser, PermissionsMixin):
    username_regex = RegexValidator(
        regex= re.compile('^[\w.@+-]+$'),
        message='Informe um nome de usuário válido. '
        'Este valor deve conter apenas letras, números '
        'e os carecteres: @/./+/-/_.',
        code= 'invalid'
    )
    
    username = models.CharField(verbose_name='Usuario', max_length=15, validators=[username_regex], help_text= 'Um nome curto que será usado' + ' para identificá-lo de forma única na plataforma.')
    email = models.EmailField(verbose_name='Email', unique=True)
    
    nome = models.CharField(verbose_name='Nome', max_length=50)
    
    is_active = models.BooleanField(verbose_name='Está Ativo', default=True)
    data_registro = models.DateTimeField(verbose_name='Data de Entrada', auto_now_add=True)

    
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome or self.username
    
    def get_full_name(self):
        return f'{self.nome}'

    def get_short_name(self):
        return str(self).split('')[0]
    
