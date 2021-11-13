# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Permite el acceso del objeto solo al dueño o al admin"""
    message = '1101: Solo el administrador de la cuenta tiene permiso para ejecutar esta accion'

    def has_object_permission(self, request, view, obj):
        """Checkea que el usuario sea igual al objeto o que sea admin"""
        user = request.user
        return user == obj


class IsThisOwner(BasePermission):
    """Permite el acceso del objeto solo al usuario del perfil y al admin"""
    message = '1102: Solo el usuario del perfil o el admin de la cuenta pueden ejecutar esta accion'

    def has_object_permission(self, request, view, obj):
        """Checkea que el usuario sea igual al objeto"""
        user = request.user
        return user == obj.user


class IsStaffUser(BasePermission):
    """Permiso para los usuarios que son staff"""
    message = '1107: Solo el staff puede usar esta funcion'

    def has_permission(self, request, view):
        """Solo le damos permiso al admin"""
        user = request.user
        return user.is_staff
