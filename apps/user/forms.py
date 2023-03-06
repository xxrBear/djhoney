from django.core.exceptions import ValidationError
from django.forms import ModelForm

from apps.user.models import User


class UserModelForm(ModelForm):

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        n = User.objects.filter(nickname=nickname)
        if n:
            raise ValidationError('昵称: {}已存在!'.format(nickname))
        else:
            return nickname

    class Meta:
        model = User
        fields = ['nickname']
