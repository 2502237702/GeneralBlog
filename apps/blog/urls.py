#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 18:19
# @Author  : LiuShaoheng


from django.urls import path, re_path, include
from blog.views import IndexView, ArticleDetailView, CategoryView, TagView, ArticleEdit


urlpatterns = [

    re_path('^$', IndexView.as_view(), name='index'),
    re_path('^article/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name='article-view'),
    re_path('^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-view'),
    re_path('^tag/(?P<tag>\d+)/$', TagView.as_view(), name='tag-view'),
    re_path('^article_edit/$', ArticleEdit, name='edit'),

]









