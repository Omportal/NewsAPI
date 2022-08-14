from rest_framework import serializers
from news.models import News, Comments, Likes


class CommentsSerializer(serializers.ModelSerializer):
    comment_date = serializers.DateTimeField(format="%Y-%m-%d  %H:%M:%S", read_only=True)
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


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    published_date = serializers.DateTimeField(format="%Y-%m-%d  %H:%M:%S", read_only=True)
    comment = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source='author.username')
    likes = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'url', 'title', 'description', 'author', 'published_date', 'likes', 'comments_count', 'comment']

    def get_comments_count(self, obj):
        queryset = obj.comment.select_related("news").count()
        return queryset

    def get_likes(self, obj):
        queryset = Likes.objects.filter(likes_to=obj.id).count()
        return queryset

    def get_comment(self, obj):
        queryset = obj.comment.all().select_related("comment_author")[:10]
        request = self.context.get('request')
        return CommentsSerializer(queryset, many=True, context={'request': request}).data
