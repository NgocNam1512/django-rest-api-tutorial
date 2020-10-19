from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only owners of an object to edit it
    """

    def has_owner_permission(self, request, view, obj):
        # Read permission are allow to request,
        # so we'll always allow GET, HEAD, or OPTIONS request.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user