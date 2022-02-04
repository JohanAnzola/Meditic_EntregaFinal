from mediticApp.models import Pacientes
from rest_framework import serializers

class PacientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pacientes
        fields = ['idPaciente', 'dni','nombres','apellidos','edad','entidad','telefono','correo','enfermedades','alergias']
    
    def to_representation(self, obj):
        pacientes = Pacientes.objects.filter(dni = obj.dni)

        return {
            "id": pacientes.idPaciente,
            "dni": pacientes.dni,
            "nombres": pacientes.nombres,
            "apellidos": pacientes.apellidos,
            "edad": pacientes.edad,
            "entidad": pacientes.entidad,
            "telefono": pacientes.telefono,
            "correo": pacientes.correo,
            "enfermedades": pacientes.enfermedades,
            "alergias": pacientes.alergias,
        }
    
    
        