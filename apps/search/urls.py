#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 18:19
# @Author  : LiuShaoheng


from django.urls import path, re_path, include
from search import views


urlpatterns = [

    re_path('^search/', views.search, name='search'),

]









