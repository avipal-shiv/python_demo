from django.contrib import admin
from django.urls import include, path

from . import views

app_name='myaccount_app'

urlpatterns = [
    path('myaccount/', views.myaccount, name='myaccount'),
    
]
