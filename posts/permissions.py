from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS or
            request.user == obj.author):
            return True
        return False
