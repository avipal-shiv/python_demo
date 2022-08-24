from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from task_app.models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    search_fields = ['title']    

admin.site.register(Task, TaskAdmin)


