from rest_framework import permissions


class IsHouseholdUser(permissions.BasePermission):
    """Check if user is a household user."""
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'HOUSEHOLD'


class IsInstitutionUser(permissions.BasePermission):
    """Check if user is an institution user."""
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'INSTITUTION'
