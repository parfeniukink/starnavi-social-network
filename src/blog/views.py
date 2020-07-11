from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Article, Like
from .serializers import ArticleSerializer, LikeSerializer


class ArticleListCreateAPIView(ListCreateAPIView):
    """Article ListCreateAPIView"""

    permission_classes = [IsAuthenticated, ]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class LikeAPIView(APIView):
    """Like/dislike API"""

    permission_classes = [IsAuthenticated, ]
    http_method_names = ['post', ]

    def post(self, request) -> Response:
        """Commit or delete from DB user's post like"""

        data = {}

        data['user'] = request.user.id
        data['article'] = request.data['article_id']

        serializer = LikeSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save_or_delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
