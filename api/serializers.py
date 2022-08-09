import requests
from rest_framework import serializers
from django.contrib.auth.models import User
from news.models import News, Comments, Likes


class CommentsSerializer(serializers.ModelSerializer):
    comment_date = serializers.ReadOnlyField()
    comment_author = serializers.ReadOnlyField(source='comment_author.username')
    news_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'comment_text', 'comment_date', 'news_id', 'comment_author']


class LikesSerializer(serializers.ModelSerializer):
    likes_to = serializers.ReadOnlyField()
    likes_from = serializers.CurrentUserDefault()

    class Meta:
        model = Likes

        fields = ['likes_to']


class NewsSerializer(serializers.ModelSerializer):
    published_date = serializers.ReadOnlyField()
    comment = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source='author.username')
    likes = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'author', 'published_date', 'likes', 'comments_count', 'comment']

    def get_comments_count(self, obj):
        queryset = obj.comment.select_related("news").count()
        return queryset

    def get_likes(self, obj):
        queryset = Likes.objects.filter(likes_to=obj.id).count()
        return queryset

    def get_comment(self, obj):
        queryset = obj.comment.all()[:10]
        return CommentsSerializer(queryset, many=True).data
