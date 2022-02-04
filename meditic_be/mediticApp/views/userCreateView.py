
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from mediticApp.serializers.usuarios_medicosSerializers import UsuariosMedicosSerializer

class UserCreateView(views.APIView):
   def post(self, request, *args, **kwargs):
      serializer = UsuariosMedicosSerializer(data = request.data)
      serializer.is_valid(raise_exception = True)
      serializer.save()
 
      tokenData = {"ccMedico":request.data["ccMedico"],
                  "password":request.data["password"]}
      tokenSerializer = TokenObtainPairSerializer(data=tokenData)
      tokenSerializer.is_valid(raise_exception=True)
 
      return Response(tokenSerializer.validated_data, status = status.HTTP_201_CREATED)