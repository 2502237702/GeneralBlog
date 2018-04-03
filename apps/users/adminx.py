#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 22:17
# @Author  : LiuShaoheng


import xadmin
from xadmin import views

from .models import Banner, UserProfile, UserManage
from blog.models import Article, Category, Link
from comments.models import Comment


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "博客后台管理"
    site_footer = "2502237702个人开发"
    menu_style = 'accordion'

    def get_site_menu(self):
        return (
            {'title': '博客管理', 'icon': 'fa fa-pencil-square', 'menus': (
                {'title': '轮播管理', 'url': self.get_model_url(Banner, 'changelist')},
                {'title': '文章类型', 'url': self.get_model_url(Category, 'changelist')},
                {'title': '文章管理', 'url': self.get_model_url(Article, 'changelist')},
            )},

            {'title': '用户管理', 'icon': 'fa fa-user', 'menus': (
                {'title': '友情链接', 'url': self.get_model_url(Link, 'changelist')},
                {'title': '用户详情', 'url': self.get_model_url(UserProfile, 'changelist')},
            )},

            {'title': '评论管理', 'icon': 'fa fa-comments', 'menus': (
                {'title': '评论详情', 'url': self.get_model_url(Comment, 'changelist')},
            )},

        )


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'rank', 'create_time']
    search_fields = ['title', 'image', 'url', 'rank']
    list_filter = ['title', 'image', 'url', 'rank', 'create_time']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Banner, BannerAdmin)












