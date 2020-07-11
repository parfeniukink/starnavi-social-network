from django.conf.urls import url
from django.urls import path

from .views import (
    LikeActivityAPIView,
    UserActivityAPIView
)


app_name = 'analitics'

urlpatterns = [
    path('likes/', LikeActivityAPIView.as_view(), name='likes_analitic'),
    path('users/', UserActivityAPIView.as_view(), name='users_analitic'),
]
