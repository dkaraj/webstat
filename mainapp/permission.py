from rest_framework.permissions import BasePermission

from django_project import settings


class Check_API_KEY_Auth(BasePermission):
    def has_permission(self, request, view):
        api_key_secret = request.META.get('HTTP_API_KEY')
        return api_key_secret == settings.API_KEY_SECRET