# Generated by Django 4.1 on 2022-08-13 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_link_alter_comments_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='link',
        ),
    ]
