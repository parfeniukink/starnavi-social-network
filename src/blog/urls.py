from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    ArticleListCreateAPIView,
    LikeAPIView
)


app_name = 'blog'

urlpatterns = [
    path(
        "articles/",
        ArticleListCreateAPIView.as_view(),
        name="article_create"
    ),
    path(
        "articles/<int:article_id>/like/",
        LikeAPIView.as_view(),
        name="article_like"
    ),
]
