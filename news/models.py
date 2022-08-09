from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class Comments(models.Model):
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, )
    news = models.ForeignKey(News, related_name='comment', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.comment_text


class Likes(models.Model):
    likes_to = models.PositiveIntegerField()
    likes_from = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Likes'

    def __str__(self):
        return f"{self.likes_to} от {self.likes_from}"
