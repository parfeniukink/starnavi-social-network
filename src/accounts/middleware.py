from django.utils.timezone import now
from django.contrib.auth import get_user_model

from rest_framework_simplejwt import authentication


class SetLastVisitMiddleware:
    """Set last_visit and last_login fields to User on request"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_visit')
            print(request.user)
            get_user_model().objects.filter(id=request.user.id).update(
                last_login=now(),
                last_visit=now()
            )
        response = self.get_response(request)

        return response
