from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField('昵称', max_length=100, blank=True)
    created_time = models.DateTimeField('创建时间', default=datetime.now)
    last_mod_time = models.DateTimeField('修改时间', default=datetime.now)

    def __str__(self):
        return '<%s:%s>' % (self.nickname, self.id)

    class Meta:
        db_table = 'user'
        abstract = False
