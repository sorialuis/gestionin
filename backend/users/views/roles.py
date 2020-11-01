# Rol Views

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Rol
from users.serializers import (
    # RolSerializer,
    CreateRolSerializer,
    RolModelSerializer
)


# @api_view()
# def list_rols(request):
#     rols = Rol.objects.all()
#     # data = []
#     # for rol in rols:
#     #     serializer = RolSerializer(rol)
#     #     data.append(serializer.data)
#     serializer = RolSerializer(rols, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def create_rol(request):
#     # rol_name = request.data['rol']
#     # auth_lvl = request.data['auth_lvl']
#     #
#     # rol = Rol.objects.create(rol=rol_name, auth_lvl=auth_lvl)
#     #
#     # data = {
#     #     'rol_name': rol.rol,
#     #     'auth_lvl': rol.auth_lvl,
#     # }
#
#     serializer = CreateRolSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     # data = serializer.data
#     # rol = Rol.objects.all(**data)
#     rol = serializer.save()
#     return Response(RolSerializer(rol).data)


class RolAPIView(APIView):

    def get(self, request, *args, **kwargs):
        rols = Rol.objects.all()
        serializer = RolModelSerializer(rols, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CreateRolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rol = serializer.save()
        return Response(RolModelSerializer(rol).data)
