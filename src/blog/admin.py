from django.contrib import admin

from .models import Article, Like


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
