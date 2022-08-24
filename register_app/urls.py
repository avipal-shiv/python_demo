from django.contrib import admin
from django.urls import include, path

from . import views

app_name='register_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    
]
