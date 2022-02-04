from django.conf import settings
from rest_framework import status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from mediticApp.serializers.historias_clinicasSerializers import HistoriasClinicasSerializer
from mediticApp.models.usuarios_medicos import UsuariosMedicos
from mediticApp.models.pacientes import Pacientes

class Historias_clinicasCreateView(views.APIView):
    
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
      token = request.META.get('HTTP_AUTHORIZATION')[7:]
      tokenBackend = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
      tokenBackend.decode(token, verify = False)

      request.data['idMedico'] = UsuariosMedicos.objects.get(ccMedico = request.data['ccMedico']).id
      request.data['idPaciente'] = Pacientes.objects.get(dni = request.data['dniPaciente']).idPaciente
      
      request.data.pop('ccMedico')
      request.data.pop('dniPaciente')

      #idMedico e idPaciente
      serializer = HistoriasClinicasSerializer(data = request.data)
      serializer.is_valid(raise_exception = True)
      serializer.save()
 
      return Response(status = status.HTTP_201_CREATED)