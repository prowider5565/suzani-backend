from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from rest_framework import status


class IsCustomer(BasePermission):
    """
    Custom permission to only allow authenticated users with the 'customer' role.
    """

    def has_permission(self, request, view):
        if request.method == "POST":
            role = request.data.get("role", None)
        else:
            role = getattr(request.user, "role", None)

        if role is None:
            # Return 403 when 'role' is not provided
            raise PermissionDenied(detail={"error": "Key `role` is not provided!"})

        if role.lower() == "manager":
            # Return 403 when the role is not 'client'
            raise PermissionDenied(
                detail={
                    "error": "Registering manager users is not allowed on client side!"
                }
            )

        return True
