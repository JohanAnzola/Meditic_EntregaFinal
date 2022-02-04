from django.db import models
from .pacientes import Pacientes
from .usuarios_medicos import UsuariosMedicos

class HistoriasClinicas(models.Model):
    idHistoriaClinica = models.AutoField(primary_key=True)
    idMedico = models.ForeignKey(UsuariosMedicos, related_name = 'medico', on_delete = models.RESTRICT, )
    idPaciente = models.ForeignKey(Pacientes, related_name = 'paciente', on_delete = models.RESTRICT)
    fechaAtencion = models.DateTimeField(auto_now = True)
    motivoConsulta = models.CharField(max_length = 256)
    medicamentosFormulados = models.CharField(max_length = 256)