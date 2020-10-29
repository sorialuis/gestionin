# User Views

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import User
from users.models import Rol


@api_view()
def list_users(request):
    usuarios = User.objects.all()
    data = []
    for usuario in usuarios:
        data.append({
            'dni': usuario.dni,
            'rol': usuario.rol,
        })
    return Response(data)


@api_view()
def list_rols(request):
    rols = Rol.objects.all()
    data= []
    for rol in rols:
        data.append({
            'id': rol.id,
            'rol': rol.rol,
            'auth_lvl': rol.auth_lvl,
        })
    return Response(data)

@api_view(['POST'])
def create_rol(request):
    rol_name = request.data['rol']
    auth_lvl = request.data['auth_lvl']

    rol = Rol.objects.create(rol=rol_name, auth_lvl=auth_lvl)

    data = {
        'rol_name': rol.rol,
        'auth_lvl': rol.auth_lvl,
    }
    return Response(data)
