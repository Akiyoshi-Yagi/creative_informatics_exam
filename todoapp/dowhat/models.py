from django.db import models
from django.utils import timezone

class Task(models.Model):


    class Meta:
        db_table = 'tasks'

    task_name = models.CharField('仕事名',max_length=15)
    task_explanation=models.TextField('説明')
    date_made=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    date_limited=models.DateTimeField('期限',default=timezone.now)
    task_status=models.BooleanField('完了した？',default=False)


class Member(models.Model):

    class Meta:
        db_table='members'

    member_name = models.CharField('お名前',max_length=15)
    mail_adress = models.CharField('メールアドレス',max_length=50)

