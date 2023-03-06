from datetime import datetime

from django.db import models


class User(models.Model):
    nickname = models.CharField('昵称', max_length=100, blank=True)
    created_time = models.DateTimeField('创建时间', default=datetime.now)
    last_mod_time = models.DateTimeField('修改时间', default=datetime.now)
    source = models.CharField("创建来源", max_length=100, blank=True)

    class Meta:
        db_table = 'user'
