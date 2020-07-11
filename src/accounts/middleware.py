from django.utils.timezone import now
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

from rest_framework_simplejwt import authentication


class SetLastVisitMiddleware(MiddlewareMixin):
    """Set last_visit and last_login fields to User on request"""

    def __init__(self, next_layer=None):
        """Allow next_layer to be None because old-style middlewares
        won't accept any argument
        """

        self.get_response = next_layer

    def __call__(self, request):
        """Middleware handling here"""

        response = self.get_response(request)

        # TODO: Add allowed time difference
        if request.user.is_authenticated:
            last_activity = request.session.get('last_visit')
            get_user_model().objects.filter(id=request.user.id).update(
                last_login=now(),
                last_visit=now()
            )

        return response
