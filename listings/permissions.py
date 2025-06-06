from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение для редактирования объекта только владельцу
    """

    def has_object_permission(self, request, view, obj):
        print(obj.owner, request.user)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

    def has_permission(self, request, view):
        print(request.user)
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated
