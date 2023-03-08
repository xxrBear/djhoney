from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from apps.user.forms import UserRegisterForm
from apps.user.models import User


class LoginView(View):
    """登录视图"""

    @staticmethod
    def get(request):
        return render(request, template_name='login.html')


class RegisterView(View):
    """注册视图"""

    @staticmethod
    def get(request):
        return render(request, template_name='register.html')

    @staticmethod
    def post(request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
            return HttpResponse('注册成功')
        else:
            return HttpResponse(form.errors)
