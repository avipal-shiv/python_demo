
from django import forms
from register_app.models import *

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.validators import validators

def check_email(value):
    if not value.isalpha():

        raise forms.ValidationError('Enter valid email')


import re
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class UserForm(forms.ModelForm):
    username = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder':'Username*', 'class':'form-control'}))
    email = forms.EmailField(required=True, max_length=150, widget=forms.TextInput(
        attrs={'placeholder': 'Email ID*', 'class':'form-control'}))
    password = forms.CharField(required=True, max_length=100, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password*','class':'form-control'}))
    confirm_password = forms.CharField(required=True, max_length=100, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password*','class':'form-control'}))
    first_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'First Name','class':'form-control'}))
    last_name = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Last Name','class':'form-control'}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        mt = validate_email(email)
        if User.objects.filter(email=self.cleaned_data.get("email")).exists():
            raise forms.ValidationError('Email already exist')
        if mt:
            pass
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        MIN_LENGHT = 8
        if len(password) < MIN_LENGHT:
            raise forms.ValidationError("Password should have alleast 8 digit")
        """if password and confirm_password and password.isdigit():
            raise forms.ValidationError('Password should not all numeric')      
            """
        """if (password and confirm_password) and (password != confirm_password):
            raise forms.ValidationError('Password mismatch' )"""
        return password
    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Password mismatch')
        return confirm_password    

    class Meta:
        model = User
        fields = ('username','email', 'password', 'confirm_password', 'first_name', 'last_name')


class RegisterForm(forms.ModelForm):    

    mobile = forms.CharField(required=False, max_length=100,
                             widget=forms.TextInput(attrs={'placeholder': 'Mobile','class':'form-control'}))
    address = forms.CharField(required=False, max_length=100,
                              widget=forms.TextInput(attrs={'placeholder': 'Address','class':'form-control'}))  
    
    
   

    class Meta:
        model = Register
        fields = ("mobile", "address")


class LoginForm(forms.ModelForm):

    username = forms.EmailField(required=True, max_length=150,
                             widget=forms.TextInput
                             (attrs={'placeholder': 'Username*'}))

    password = forms.CharField(required=True, max_length=100,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password*', 'class':'p7 w95'}))

    class Meta:
        model = User
        fields = {"username", "password"}

