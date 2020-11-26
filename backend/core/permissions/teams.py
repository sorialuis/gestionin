from rest_framework.permissions import BasePermission


class IsInclude(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.team == obj


#
# class IsInclude(BasePermission):
#
#     # def has_permission(self, request, view):
#     def has_object_permission(self, request, view, obj):
#         # print(str(request.user.rol) == 'admin')
#         # print(request.user.rol)
#         # print('admin')
#         return bool(
#             request.user and
#             request.user.is_active and
#             str(request.user.rol) == 'admin'
#         )
#
#     def has_permission(self, request, view):
#         return bool(
#             request.user and
#             request.user.is_active and
#             str(request.user.rol) == 'admin'
#         )
