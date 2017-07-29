from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, platform_user):
        if request.user:
            return platform_user == request.user
        return False
