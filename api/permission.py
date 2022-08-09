from rest_framework import permissions


class SelfCommentsOrCommentsSelfNews(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.news.author == request.user or obj.comment_author == request.user:
            return True
        return False


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False
