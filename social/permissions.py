from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    """
    Custom permission to only allow authenticated users with the 'manager' role.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == "manager"
