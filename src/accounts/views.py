from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class CreateUserAPIView(APIView):
    def post(self, request) -> Response:
        user = request.data
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
