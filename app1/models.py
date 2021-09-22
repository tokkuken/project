from django.db import models

class database(models.Model):
    username = models.CharField('ユーザ名', max_length=255)
    password = models.CharField('パスワード', max_length=255)
    answer = models.CharField('回答', max_length=255)
    score = models.IntegerField('スコア')
    course = models.IntegerField('コース')

    def __str__(self):
        return self.username