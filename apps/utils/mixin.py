#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/24 11:24
# @Author  : LiuShaoheng


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)













