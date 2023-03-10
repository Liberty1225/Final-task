from rest_framework.permissions import BasePermission, SAFE_METHODS


class OwnerPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            (request.user and request.user.is_authenticated))

    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or
                    (request.user and
                     request.user.is_authenticated and obj.author == request.user.author
                     )
                    or (request.user and request.user.is_authenticated and request.user.is_staff))

    class IsAdminUser(BasePermission):
        def has_permission(self, request, view):
            return bool(request.user.is_authenticated is False or request.user.is_staff)

