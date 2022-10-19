from rest_framework import permissions


class IsCreatedBy(permissions.BasePermission):
    message = 'Only user who created the selection could delete it.'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
