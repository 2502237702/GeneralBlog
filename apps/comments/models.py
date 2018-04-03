from django.db import models
from django.conf import settings
from blog.models import Article
from datetime import datetime


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='评论')
    is_removed = models.BooleanField(default=False)
    parent = models.ForeignKey(
        'self', default=None, blank=True, null=True, verbose_name='父评论', on_delete=models.CASCADE
    )
    likes_count = models.PositiveIntegerField(default=0, verbose_name='点赞数')

    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
    update_time = models.DateTimeField(verbose_name='修改时间', blank=True, null=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.article.title


