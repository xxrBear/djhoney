from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from apps.user.forms import UserRegisterForm
from apps.user.models import User


class LoginView(View):
    """登录视图"""

    def get(self, request):
        return render(request, template_name='user/login.html')


class RegisterView(View):
    """注册视图"""

    def get(self, request):
        return render(request, template_name='user/register.html')

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponse(form.errors)
