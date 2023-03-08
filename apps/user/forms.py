from django import forms

from apps.user.models import User


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        n = User.objects.filter(nickname=nickname)
        if n:
            raise forms.ValidationError('昵称: {}已存在!'.format(nickname))
        else:
            return nickname
