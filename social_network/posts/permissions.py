from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, platform_user):
        if request.user:
            return platform_user == request.user
        return False


class IsAccountOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, platform_user):
        if request.user:
            return (platform_user == request.user) or request.user.is_staff
        return False


class IsAccountOwnerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, platform_user):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user:
            return (platform_user == request.user) or request.user.is_staff
        return False


class IsAccountOwnerOrAdminOrReadOnlyAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request, view, platform_user):
        if request.user:
            if request.method in permissions.SAFE_METHODS and is_authenticated(request.user):
                return True
            return (platform_user == request.user) or request.user.is_staff
        return False
