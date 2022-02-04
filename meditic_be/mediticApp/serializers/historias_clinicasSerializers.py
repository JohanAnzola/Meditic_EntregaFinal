from rest_framework import serializers
from mediticApp.models.historias_clinicas import HistoriasClinicas
from mediticApp.models.pacientes import Pacientes
from mediticApp.models.usuarios_medicos import UsuariosMedicos

class HistoriasClinicasSerializer(serializers.ModelSerializer):

       class Meta: 
               model = HistoriasClinicas
               fields = ['idHistoriaClinica', 'idMedico', 'idPaciente','fechaAtencion', 'motivoConsulta', 'medicamentosFormulados']


       def to_representation(self, obj):
              historia = HistoriasClinicas.objects.get(idHistoriaClinica = obj.idHistoriaClinica)
              medico = UsuariosMedicos.objects.get(id = historia.idMedico.id)
              paciente = Pacientes.objects.get(idPaciente = historia.idPaciente.idPaciente)

              return {
                     'ID': historia.idHistoriaClinica,
                     'Fecha de atencion': historia.fechaAtencion,
                     'Motivo de consulta': historia.motivoConsulta,
                     'Medicamentos formulados': historia.medicamentosFormulados,
                     'Medico': {
                            'CC.': medico.ccMedico,
                            'Nombre completo': medico.nombre,
                            'Correo': medico.email,
                     },
                     'Paciente': {
                            'DNI': paciente.dni,
                            'Nombres': paciente.nombres,
                            'Apellidos': paciente.apellidos,
                            'Edad': paciente.edad,
                            'Entidad': paciente.entidad,
                            'Telefono': paciente.telefono,
                            'Correo': paciente.correo,
                            'Enfermedades': paciente.enfermedades,
                            'Alergias': paciente.alergias
                     } 
              }