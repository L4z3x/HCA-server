from rest_framework.permissions import BasePermission


class IsWriter(BasePermission):
    """
    Custom permission to only allow users with the 'writer' role.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and getattr(request.user, "role") == "writer"
        )


class IsAdmin(BasePermission):
    """
    Custom permission to only allow users with the 'admin' role.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the 'admin' role
        return (
            request.user
            and request.user.is_authenticated
            and getattr(request.user, "role") == "admin"
        )
