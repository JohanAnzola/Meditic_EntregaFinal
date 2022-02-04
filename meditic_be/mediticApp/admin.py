from django.contrib import admin
from .models.usuarios_medicos import UsuariosMedicos
from .models.pacientes import Pacientes
from .models.historias_clinicas import HistoriasClinicas
# Register your models here.

admin.site.register(UsuariosMedicos)
admin.site.register(Pacientes)
admin.site.register(HistoriasClinicas)