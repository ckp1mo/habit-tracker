from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверка является ли пользователь автором объекта"""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
