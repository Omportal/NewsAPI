from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, \
    RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from .serializers import NewsSerializer, CommentsSerializer, LikesSerializer
from news.models import News, Comments, Likes
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .permission import SelfCommentsOrCommentsSelfNews, IsAuthor


class NewsList(ListCreateAPIView):
    serializer_class = NewsSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return News.objects.all().order_by('-published_date')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NewsRetrieveUpdate(RetrieveUpdateAPIView):
    serializer_class = NewsSerializer
    permission_classes = [IsAuthor, permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]

    def get_queryset(self):
        return News.objects.all()


class NewsRetrieveDestroy(RetrieveDestroyAPIView):
    serializer_class = NewsSerializer
    permission_classes = [IsAuthor, permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        return News.objects.all()


class CommentsList(ListCreateAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        comments = Comments.objects.filter(news_id=self.kwargs['pk'])
        return comments

    def perform_create(self, serializer):
        serializer.save(comment_author=self.request.user, news_id=self.kwargs['pk'])


class CommentsRetrieveUpdate(RetrieveUpdateAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, SelfCommentsOrCommentsSelfNews,
                          permissions.IsAdminUser]

    def get_queryset(self):
        return Comments.objects.all()


class CommentsRetrieveDestroy(RetrieveDestroyAPIView):
    serializer_class = CommentsSerializer

    permission_classes = [permissions.IsAuthenticated, SelfCommentsOrCommentsSelfNews, permissions.IsAdminUser]

    def get_queryset(self):
        return Comments.objects.all()


class LikesCreate(CreateAPIView):
    serializer_class = LikesSerializer
    permissions = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Likes.objects.all()

    def perform_create(self, serializer):
        serializer.save(likes_from=self.request.user, likes_to=self.kwargs['pk'])


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({'error': 'username taken. choose another username'}, status=400)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error': 'unable to login. check username and password'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
