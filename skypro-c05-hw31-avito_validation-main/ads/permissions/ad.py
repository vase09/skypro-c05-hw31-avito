from rest_framework import permissions

from users.models import User


class IsCreatedByOrAdminOrModerator(permissions.BasePermission):
    message = 'Only user who created the ad, amdin and moderators could modify or delete it.'

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.ADMIN or request.user.role == User.MODERATOR:
            return True
        if obj.author == request.user:
            return True
        return False
