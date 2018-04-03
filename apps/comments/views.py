import datetime
import logging

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View

from comments.models import Comment
from blog.models import Article


logger = logging.getLogger(__name__)


class CommentView(View):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        text = self.request.POST.get('comment', '')
        if not user.is_authenticated():
            logger.error(
                '[CommentView]当前用户非活动用户：[{}]'.format(user.username)
            )
            request.session['LoginForm'] = request.META.get('HTTP_REFERER', '/')
            return render(request, 'users/login.html')

        article_id = self.kwargs.get('article_id', '')
        article = Article.objects.get(id=article_id)

        # 保存评论
        parent = None
        if text.startswith('@['):
            import ast
            parent_str = text[1:text.find(':')]
            parent_id = ast.literal_eval(parent_str)[1]
            text = text[text.find(':') + 2:]
            try:
                parent = Comment.objects.get(pk=parent_id)
                info = '{}回复了你在 {} 的评论'.format(
                    user.username,
                    parent.article.title,
                )

            except Comment.DoesNotExist:
                logger.error('[CommentView]评论引用错误:%s' % parent_str)
                return HttpResponse('请勿修改评论代码！', status=403)

        if not text:
            logger.error('[CommentView]当前用户输入空评论：[{}]'.format(user.username))
            return HttpResponse('请输入评论内容！', status=403)
        comment = Comment.objects.create(
            user=user,
            article=article,
            text=text,
            parent=parent,
        )

        try:
            img = '/media/' + comment.user.image
        except Exception as e:
            img = "/media/default.jpg"

        print_comment = '<p>评论：{}</p>'.format(text)
        if parent:
            print_comment = '<div class=\"comment-quote\">\
                                <p>\
                                    <a>@{}</a>\
                                    {}\
                                </p>\
                            </div>'.format(
                parent.user.username,
                parent.text,
            ) + print_comment

        # 返回当前评论
        html = "<li>\
                    <div class=\"comment-tx\">\
                        <img src={} width=\"40\" style=\"border-radius: 50%;\"></img>\
                    </div>\
                    <div class=\"comment-content\">\
                        <a><h1>{}</h1></a>\
                        {}\
                        <p>{}</p>\
                    </div>\
                </li>".format(
            img,
            comment.user.username,
            print_comment,
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        user.comment_num += 1
        user.save()
        return redirect('article-view', article_id=article_id)






