from django.forms import ModelForm
from .models import Member,Task


class MemberForm (ModelForm):
    class Meta:
        model=Member
        fields=['member_name','mail_adress']


class TaskForm (ModelForm):
    class Meta:
        model=Task
        fields=['task_name','task_explanation','date_limited','task_status']

