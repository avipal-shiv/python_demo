
from django import forms
from task_app.models import *

class TaskForm(forms.ModelForm):   
    
    title = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder':'Title*', 'class':'form-control'}))
    description= forms.CharField(required=True, max_length=300, widget=forms.Textarea(attrs={'name':'body', 'rows':3, 'cols':5,'placeholder': 'Description*', 'class':'form-control'})) 


    class Meta:
        model = Task
        fields = ('title','description')

class TaskEditForm(forms.ModelForm):
    
    title = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder':'Title*', 'class':'form-control'}))
    description= forms.CharField(required=True, max_length=300, widget=forms.Textarea(attrs={'name':'body', 'rows':3, 'cols':5,'placeholder': 'Description*', 'class':'form-control'})) 


    class Meta:
        model = Task
        fields = ('title','description')
