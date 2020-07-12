from django.conf import settings
from django.db import models


class Article(models.Model):
    """Article model"""

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    title = models.CharField(max_length=50)
    body = models.TextField()

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    """Article like model"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    article = models.ForeignKey(
        "Article",
        on_delete=models.CASCADE
    )

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user} | {self.article}"
