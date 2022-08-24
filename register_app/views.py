from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.urls import path,reverse
from register_app.models import *
from register_app.forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as dj_login,logout
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.conf import settings



def register(request):
  
  if request.user.is_authenticated:
    return HttpResponseRedirect('myaccount/')
  
  registered = False
  
  if request.method == 'POST':
    print(request.POST)
    user_form = UserForm(data=request.POST)    
    profile_form = RegisterForm(data=request.POST)   
    if user_form.is_valid() :
      try:
        email = request.POST['email']       
        password = request.POST['password']
        user = user_form.save()
        user.set_password(user.password)
        user.username = request.POST['username']
        user.is_active = True
        user.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()        
        registered = True      
       
        messages.success(request, 'Your registration has been successfully.')      
        return HttpResponseRedirect('/register')
      except Exception as e:
        print(e)
  else:
    profile_form = RegisterForm()
    user_form = UserForm()      
  return render(request,'register.html', {'reg_form':profile_form, 'user_form':user_form, 'registered':registered, 'register_flag':True})   


def login(request):
  if request.user.is_authenticated:
    return HttpResponseRedirect('myaccount')
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user:
      if user.is_active:
        dj_login(request, user)
        request.session['username'] = request.POST.get('username')   
        return HttpResponseRedirect('/myaccount')
        
    else:
      messages.error(request,"Invalid login details given")
      return HttpResponseRedirect("/login")
      #return HttpResponse("Invalid login details given")
  else:
    form = LoginForm()
    
    return render(request, 'login.html', {'form':form, 'login_flag':True})

def user_logout(request):
  logout(request)
  form = LoginForm()
  messages.success(request,"Logout successfully")  
  return render(request, 'login.html', {'form':form,})

