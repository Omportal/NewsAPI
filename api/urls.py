from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsList.as_view()),
    path('news/<int:pk>/', views.NewsRetrieveUpdate.as_view()),
    path('news/<int:pk>/delete/', views.NewsRetrieveDestroy.as_view()),
    path('news/<int:pk>/comments/', views.CommentsList.as_view()),
    path('news/comments/<int:pk>/', views.CommentsRetrieveUpdate.as_view()),
    path('news/comments/<int:pk>/delete', views.CommentsRetrieveDestroy.as_view()),
    path('news/<int:pk>/like/', views.LikesCreate.as_view()),
    path('signup/', views.signup),
    path('login/', views.login),
]
