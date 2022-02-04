from django.conf import settings
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from mediticApp.models.historias_clinicas import HistoriasClinicas
from mediticApp.models.pacientes import Pacientes
from mediticApp.serializers.historias_clinicasSerializers import HistoriasClinicasSerializer
from rest_framework import generics
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response

class HistoriaClinicaDetailView(generics.RetrieveAPIView):
    queryset = HistoriasClinicas.objects.all()
    serializer_class = HistoriasClinicasSerializer
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        tokenBackend.decode(token, verify = False)

        paciente = Pacientes.objects.filter(dni = request.data['dni']).first()

        historiasFiltradas = HistoriasClinicas.objects.filter(idPaciente = paciente.idPaciente).order_by('-fechaAtencion')
        serializer = HistoriasClinicasSerializer(historiasFiltradas, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class HistoriaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoriasClinicas.objects.all() #conjunto de datos
    serializer_class = HistoriasClinicasSerializer #que srializador vas a usar