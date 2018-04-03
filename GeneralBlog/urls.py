"""GeneralBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf.urls import static
from GeneralBlog.settings import MEDIA_ROOT
import xadmin

urlpatterns = [

    path('admin/', admin.site.urls),
    re_path('^xadmin/', xadmin.site.urls),
    re_path('^ueditor/', include('DjangoUeditor.urls')),
    re_path('^captcha', include('captcha.urls')),

    re_path('^', include('blog.urls')),
    re_path('^', include('users.urls')),
    re_path('^', include('comments.urls')),
    re_path('^', include('search.urls')),

    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT})

]
