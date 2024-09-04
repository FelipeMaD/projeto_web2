from rest_framework import permissions

class IsInSpecificGroup(permissions.BasePermission):
    vips = 'vips'
    def has_permission (self, request, view):
        return request.user.groups.filter(name=self.vips).exists()
    
