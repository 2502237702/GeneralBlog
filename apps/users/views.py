from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth import login, logout, authenticate
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin


from users.models import UserProfile
from .forms import LoginForm, RegisterForm, ChangeUserImageForm, PasswordChangeForm


class LoginView(View):
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            if user is not None:
                login(request, user)
                return HttpResponsePermanentRedirect(request.session['LoginForm'])
        else:
            logout(request)
            # print(login_form.errors)
            return render(request, 'users/login.html', {'errors': login_form.errors})

    def get(self, request):
        login_form = LoginForm()
        user = None
        request.session['LoginForm'] = request.META.get('HTTP_REFERER', '/')
        return render(request, 'users/login.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('index'))


class RegisterView(View):
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            if user is not None:
                user = authenticate(
                    username=register_form.cleaned_data['username'],
                    password=register_form.cleaned_data['password'])
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            logout(request)
            return render(request, 'users/register.html', {'errors': register_form.errors})

    def get(self, request):
        register_form = RegisterForm()
        user = None
        return render(request, 'users/register.html')


class PasswordView(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            data = form.clean()
            if user.check_password(data["old_password"]):
                user.set_password(data["password"])
                user.save()
                messages.success(request, "新密码设置成功！请重新登录")
                logout(request)
                return HttpResponseRedirect(reverse("login"))
            else:
                messages.error(request, '当前密码输入错误')
                return render(request, "users/password.html", {'errors': form.errors})

    def get(self, request):
        form = PasswordChangeForm()
        return render(request, "users/password.html")


class UpdateImageView(LoginRequiredMixin, View):
    def post(self, request):
        form = ChangeUserImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            user = request.user
            user.image = image
            user.save()
            return HttpResponseRedirect(reverse('index'))

    def get(self, request):
        form = ChangeUserImageForm()
        return render(request, 'users/changeuserimage.html', {'form': form})














