from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from datetime import datetime


class UserManage(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        now = datetime.now
        user = self.model(username=username, email=self.normalize_email(email), create_time=now)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a superuser
        """
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractUser):

    username = models.CharField(max_length=32, verbose_name='用户名', unique=True)
    email = models.EmailField(max_length=64, verbose_name='邮箱', unique=True)
    password = models.CharField(max_length=128, verbose_name='密码')
    profile = models.TextField(max_length=200, verbose_name='简介', blank=True, null=True)
    image = models.ImageField(max_length=200, upload_to='avatar/%Y/%m/%d', default='default.png', verbose_name='用户头像')
    au = models.IntegerField(default=0, verbose_name='用户活跃度')

    topic_num = models.IntegerField(default=0, verbose_name='文章数')
    visit_num = models.IntegerField(default=0, verbose_name='访问量')
    comment_num = models.IntegerField(default=0, verbose_name='总评论数')

    is_active = models.BooleanField(default=True)

    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
    update_time = models.DateTimeField(verbose_name='修改时间', blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name

    def is_email_verified(self):
        return self.email_verified

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def calculate_au(self):
        self.au = self.topic_num * 5 + self.visit_num * 1 + self.comment_num * 1
        return self.au

    def __str__(self):
        return self.username


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m/%d', max_length=100, verbose_name='轮播图')
    url = models.URLField(max_length=200, verbose_name='访问地址')
    rank = models.IntegerField(default=100, verbose_name='顺序')
    create_time = models.DateField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='修改时间', blank=True, null=True)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title









