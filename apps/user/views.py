from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from apps.user.forms import UserModelForm
from apps.user.models import User


class LoginView(View):
    """登录视图"""
    pass


class RegisterView(View):
    """注册视图"""

    def post(self, request, *args, **kwargs):
        form = UserModelForm(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
            return HttpResponse('注册成功')
        else:
            return HttpResponse('注册失败')
