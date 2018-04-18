from django.urls import path
from . import views

urlpatterns = [
    path('member/',views.member_index,name='member_index'),
    path('member/<int:member_id>/detail/',views.member_detail,name='member_detail'),
    path('member/<int:member_id>/edit/',views.member_edit,name='member_edit'),
    path('member/add/',views.member_add,name='member_add'),
    path('member/<int:member_id>/delete/', views.member_delete, name='member_delete'),

    path('task/',views.task_index,name='task_index'),
    path('task/<int:task_id>/detail/',views.task_detail,name='task_detail'),
    path('task/<int:task_id>/edit/',views.task_edit,name='task_edit'),
    path('task/add/',views.task_add,name='task_add'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
]