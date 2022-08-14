from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register(r'news', views.NewsViewSet)

urlpatterns = [
    path('news/<int:news_pk>/comments/', views.CommentsList.as_view()),
    path('news/<int:news_pk>/comment/<int:pk>/', views.CommentsRetrieveUpdate.as_view()),
    path('news/<int:news_pk>/comment/<int:pk>/delete', views.CommentsRetrieveDestroy.as_view()),
    path('news/<int:pk>/like/', views.LikesCreate.as_view()),
    path('auth/signup/', views.signup),
    path('auth/login/', views.login),
]
urlpatterns += [
    path("", include(routers.urls)),
]
