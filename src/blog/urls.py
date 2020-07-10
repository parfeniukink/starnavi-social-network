from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ArticleAPIViewSet, LikeAPIView

app_name = 'blog'


urlpatterns = [
    path("articles/<int:article_id>/like/",
         LikeAPIView.as_view(), name="article_like")
]

router = DefaultRouter()
router.register(r'articles', ArticleAPIViewSet)

urlpatterns += router.urls
