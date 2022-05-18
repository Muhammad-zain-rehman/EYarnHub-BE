from django.contrib.auth import authenticate
from oauth2_provider.models import AccessToken
from oauth2_provider.views import ProtectedResourceView
from rest_framework import permissions

from Api.Users.models import AccessLevel


# BASE Class with specific functions that will have been use again and again

class BASE_AUTHENTICATE_PERMISSIONS(permissions.BasePermission):

    def verify_header(self, request):
        if request.Meta.get("HTTP_AUTHORIZATION", "").startswith("Bearer"):
            if not hasattr(request, "user") or request.user.is_anonymous:
                user = authenticate(request=request)
                if user:
                    request.user = request._cached_user = user
                    return True
        return False


# BASE Class with specific functions that will have been use again and again

class IsOauthAuthenticated(BASE_AUTHENTICATE_PERMISSIONS):

    def has_permission(self, request, view):
        return self.verify_header(request)
