from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, CreateAPIView, \
    RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from .serializers import NewsSerializer, CommentsSerializer, LikesSerializer
from news.models import News, Comments, Likes
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .permission import SelfCommentsOrCommentsSelfNews, IsAuthorOrAdmin, IsAuthorCommentOrAdmin


class NewsList(ListCreateAPIView):
    """Получаем список всех новостей с пагинацией"""
    serializer_class = NewsSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return News.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NewsRetrieveUpdate(RetrieveUpdateAPIView):
    """Получаем одну новость со списком комментариев,изменить её могут только автор или админ"""
    serializer_class = NewsSerializer
    permission_classes = [IsAuthorOrAdmin]

    def get_queryset(self):
        return News.objects.all()


class NewsRetrieveDestroy(RetrieveDestroyAPIView):
    """Удаляем новость ,только автор или админ"""
    serializer_class = NewsSerializer
    permission_classes = [IsAuthorOrAdmin]

    def get_queryset(self):
        return News.objects.all()


class CommentsList(ListCreateAPIView):
    """Получаем список всех комментариев к новости,авторизованные юзеры могут создавать комментарии"""
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        comments = Comments.objects.filter(news_id=self.kwargs['pk'])
        return comments

    def perform_create(self, serializer):
        serializer.save(comment_author=self.request.user, news_id=self.kwargs['pk'])


class CommentsRetrieveUpdate(RetrieveUpdateAPIView):
    """Получем один комментарий ,изменить могут только автор или админ"""
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthorCommentOrAdmin]

    def get_queryset(self):
        return Comments.objects.all()


class CommentsRetrieveDestroy(RetrieveDestroyAPIView):
    """Удаляем комментарий ,только для автора или или админа, или, если комментарий к новости автора"""
    serializer_class = CommentsSerializer

    permission_classes = [SelfCommentsOrCommentsSelfNews]

    def get_queryset(self):
        return Comments.objects.all()


class LikesCreate(CreateAPIView):
    """Ставим лайк по POST запросу ,PK новости в URL адресе
        Проверка чтобы нельзя было поставить два лайка от одного юзера одной новости.
    """
    serializer_class = LikesSerializer
    permissions = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Likes.objects.all()

    def perform_create(self, serializer):
        likes_data = Likes.objects.filter(likes_from=self.request.user, likes_to=self.kwargs['pk'])
        if not likes_data:
            serializer.save(likes_from=self.request.user, likes_to=self.kwargs['pk'])


@csrf_exempt
def signup(request):
    """Метод для регистрации нового юзера"""
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
    return JsonResponse({'error': 'enter username and password'}, status=201)


@csrf_exempt
def login(request):
    """Логинимся ,проверка наличие токена в базе данных"""
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
    return JsonResponse({'error': 'enter username and password'}, status=201)
