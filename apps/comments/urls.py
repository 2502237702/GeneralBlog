#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 18:19
# @Author  : LiuShaoheng


from django.urls import re_path, include
from comments.views import CommentView

urlpatterns = [
    re_path('^comment/(?P<article_id>\d+)/$', CommentView.as_view(), name='comment-view'),
]









