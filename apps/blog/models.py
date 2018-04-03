from django.db import models
from GeneralBlog import settings
from datetime import datetime
from django.urls.base import reverse

from DjangoUeditor.models import UEditorField


STATUS = {
    0: '发表',
    1: '草稿',
    2: '丢弃',
}

ARTICLE_FROM = {
    0: '原创',
    1: '转载',
}

IS_READ = {
    0: '未读',
    1: '已读',
}


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='类型名称')
    rank = models.IntegerField(default=0, verbose_name='排序')
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
    update_time = models.DateTimeField(verbose_name='修改时间', blank=True, null=True)

    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = verbose_name
        ordering = ['rank', '-create_time']

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='类型', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='标题')
    article_from = models.IntegerField(default=0, choices=ARTICLE_FROM.items(), verbose_name='文章来源')
    summary = models.TextField(verbose_name='摘要')
    tags = models.CharField(max_length=100, null=True, blank=True, verbose_name='标签', help_text='用逗号分隔')
    content = UEditorField(verbose_name='正文', toolbars='full', width='1000', height='300', imagePath='article/ueditor/', filePath='article/ueditor', default='')
    reading_num = models.IntegerField(default=0, verbose_name='阅读量')

    is_top = models.BooleanField(default=False, verbose_name='是否置顶')
    rank = models.IntegerField(default=0, verbose_name='排序')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name='文章状态')

    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='修改时间', blank=True, null=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('article', args=(self.en_title,))

    def get_tags(self):
        tags_list = self.tags.split(',')
        while '' in tags_list:
            tags_list.remove('')
        tags_list = tags_list[0:3]

        return tags_list

    def get_category(self):
        return self.category

    def __str__(self):
        return self.title


class Link(models.Model):
    name = models.CharField(max_length=40, verbose_name='链接名')
    url = models.URLField(max_length=40, verbose_name='链接地址')
    rank = models.IntegerField(default=0, verbose_name='排序')

    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='修改时间', blank=True, null=True)

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name








