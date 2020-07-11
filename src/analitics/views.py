from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serivices import get_quantity_of_likes_by_date, get_user_activity


class LikeActivityAPIView(APIView):
    """Analytics about how many likes was made"""

    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', ]

    def get(self, request) -> Response:
        """Returns quantity of likes by date"""

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        likes_by_date = get_quantity_of_likes_by_date(date_from, date_to)

        return Response(likes_by_date)


class LikeActivityAPIView(APIView):
    """Analytics about how many likes was made"""

    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', ]

    def get(self, request) -> Response:
        """Returns quantity of likes by date"""
        print(request.user)
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        likes_by_date = get_quantity_of_likes_by_date(date_from, date_to)

        return Response(likes_by_date)


class UserActivityAPIView(APIView):
    """User Analytics of last_login and last_visit"""

    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', ]

    def get(self, request) -> Response:
        """Returns users with last_login, last_visit by id"""

        users = get_user_activity()

        return Response(users)
