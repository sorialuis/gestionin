from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_active and
            request.user.rol == 'admin'
        )


class IsSupervisor(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_active and
            request.user.rol == 'supervisor'
        )