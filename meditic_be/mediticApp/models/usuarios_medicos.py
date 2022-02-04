from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, ccMedico, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not ccMedico:
            raise ValueError('Users must have an username')
        usuarioMedico = self.model(ccMedico = ccMedico)
        usuarioMedico.set_password(password)
        usuarioMedico.save(using = self._db)
        return usuarioMedico


    def create_superuser(self, ccMedico, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        usuarioMedico = self.create_user(
            ccMedico=ccMedico,
            password=password,
        )
        usuarioMedico.is_admin = True
        usuarioMedico.save(using=self._db)
        return usuarioMedico


class UsuariosMedicos(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    ccMedico = models.CharField('CcMedico', max_length = 30, unique = True)
    password = models.CharField('Password', max_length = 256)
    nombre = models.CharField('Name', max_length = 50)
    email = models.EmailField('Email', max_length = 100)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)


    objects = UserManager()
    USERNAME_FIELD = 'ccMedico'