from rest_framework import permissions


class SelfCommentsOrCommentsSelfNews(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        elif obj.news.author == request.user or obj.comment_author == request.user:
            return True
        return False


class IsAuthorOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True
        return obj.author == request.user


class IsAuthorCommentOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.comment_author == request.user
