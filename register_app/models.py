from django.db import models
from django.contrib.auth.models import User
import datetime


class Register(models.Model):  
  user = models.OneToOneField(User,on_delete=models.CASCADE)    
  gender = models.CharField(max_length=10,choices=[('Male','Male'),('Female','Female')],default='Female')  
  address  = models.CharField(max_length=150, blank=True)
  mobile  = models.CharField(max_length=50, blank=True)  
  reg_date  = models.DateField(default = datetime.date.today, null=True)
  status = models.CharField(max_length=2, choices=[('1','Active'),('2','Deactive')],default=2)
    
  class Meta:
     db_table = "tb_register"
     verbose_name = "User Profile Info"
     verbose_name_plural = "User Profile Info"
