from rest_framework import serializers

from .models import Article, Like


class ArticleSerializer(serializers.ModelSerializer):
    """Article model serializer"""
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Article
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    """Like model serializer"""

    class Meta:
        model = Like
        fields = '__all__'

    def save_or_delete(self):
        """Save if like not in DB or delete if exist"""

        user_id = self.data['user']
        article_id = self.data['article']

        like = Like.objects.filter(article__id=article_id, user__id=user_id)

        if like:
            like.delete()
        else:
            Like.objects.create(
                user_id=user_id,
                article_id=article_id
            )
