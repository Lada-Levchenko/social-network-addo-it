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
