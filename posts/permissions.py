from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


class CustomPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.user == obj.author:
            return True
        return False
        # if request.user != obj.author:
        #     return Response(status=status.HTTP_403_FORBIDDEN)
        # return True
