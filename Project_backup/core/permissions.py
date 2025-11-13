# core/permissions.py
from rest_framework import permissions

class IsAdminInventaris(permissions.BasePermission):
    """
    Custom permission to only allow users in 'Admin Inventaris' group.
    """
    message = "Hanya Admin Inventaris yang diizinkan mengakses endpoint ini."

    def has_permission(self, request, view):
        # Cek jika user terotentikasi DAN 
        # termasuk dalam grup 'Admin Inventaris'
        return request.user and \
               request.user.is_authenticated and \
               request.user.groups.filter(name='Admin Inventaris').exists()