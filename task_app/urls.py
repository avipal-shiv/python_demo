from django.contrib import admin
from django.urls import include, path

from . import views

app_name='task_app'

urlpatterns = [
    path('addtask/', views.addtask, name='addtask'),
    path('tasklist/', views.tasklist, name='tasklist'),
    path('alltasklist/', views.alltasklist, name='alltasklist'),    
    path('taskdelete/<int:tid>', views.taskdelete, name='taskdelete'),
    path('taskupdate/<int:tid>', views.taskupdate, name='taskupdate'),
]