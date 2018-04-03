#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 18:19
# @Author  : LiuShaoheng


from django.urls import re_path, include
from users.views import LoginView, LogoutView, PasswordView, UpdateImageView, RegisterView


urlpatterns = [

    re_path('^login/$', LoginView.as_view(), name='login'),
    re_path('^logout/$', LogoutView.as_view(), name='logout'),
    re_path('^register/$', RegisterView.as_view(), name='register'),
    re_path('^password/$', PasswordView.as_view(), name='password'),
    re_path('^updateimage/$', UpdateImageView.as_view(), name='updateimage'),

]









