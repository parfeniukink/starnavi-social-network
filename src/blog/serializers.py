from rest_framework import serializers

from .models import Article, Like


class ArticleSerializer(serializers.ModelSerializer):
    """Article model serializer"""

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

        # TODO: Finish
        # self.data = {'user': 1, 'article': 2}
        pass
