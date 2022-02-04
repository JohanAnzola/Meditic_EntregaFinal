from mediticApp.models import UsuariosMedicos
from rest_framework import serializers

class UsuariosMedicosSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsuariosMedicos
        fields = ['id', 'ccMedico','password','nombre','email']
    
    def to_representation(self, obj):
        medico = UsuariosMedicos.objects.get(ccMedico=obj.ccMedico)
         
        return {
            'CC.': medico.ccMedico,            
            'Nombre': medico.nombre,
            'Email': medico.email,
        }
