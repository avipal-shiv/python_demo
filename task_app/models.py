from django.db import models

from register_app.models import * 
from django.contrib.auth.models import User


class Task(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null=True, verbose_name='Member')
  title = models.CharField(max_length=150, blank = True, null=True)
  description = models.TextField(max_length=300, blank = True )

  def __str__(self):    
    return self.title
  

  class Meta:
     db_table = "tbl_task"
     verbose_name="Task List"