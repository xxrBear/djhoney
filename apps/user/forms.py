from django import forms
from django.contrib.auth.hashers import make_password

from apps.user.models import User


class UserRegisterForm(forms.Form):
    nickname = forms.CharField()
    password = forms.CharField()

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        n = User.objects.filter(nickname=nickname)
        if n:
            raise forms.ValidationError('昵称: {}已存在!'.format(nickname))
        else:
            return nickname

    def clean_password(self):
        p1 = self.data.get('password')
        p2 = self.data.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('两次密码不一致!')
        else:
            return make_password(p1)
