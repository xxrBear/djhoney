from django.db import models


class User(models.Model):
    nickname = models.CharField(verbose_name='昵称', max_length=128)
    password = models.CharField(verbose_name='密码', max_length=128)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField(verbose_name='修改时间', auto_now_add=True)

    def __str__(self):
        return '<%s:%s>' % (self.nickname, self.id)

    class Meta:
        db_table = 'user'
        abstract = False
        verbose_name = '用户'
        verbose_name_plural = verbose_name  # 不加的话admin后台会加上s
