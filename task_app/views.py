from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from task_app.models import *
from task_app.forms import *

from django.contrib import messages

@login_required(login_url='/login')
def addtask(request):  
  resobject = Register.objects.get(user_id=request.user.id)  
  if request.method =='POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      try:
        task = form.save()
        task.user_id = request.user.id
        task.save()
        messages.success(request,'Task has been added successfully') 
        return redirect('/tasklist')
      except:
        pass
    else:
      form = TaskForm(request.POST)
      return render(request,'add_task.html',{'form':form })    
  else:
    form = TaskForm()
    return render(request,'add_task.html',{'form':form })

def tasklist(request):
    listdata = Task.objects.filter(user_id=request.user.id)  
    return render(request, 'task_list.html', {'listdata':listdata})

def alltasklist(request):
    listdata = Task.objects.all()  
    return render(request, 'all_task_list.html', {'listdata':listdata})    

def taskdelete(request, tid):
   
    listdata = Task.objects.filter(user_id=request.user.id,id=tid)  
    listdata.delete()
    messages.success(request,'Task has been deleted successfully')    
    return redirect('/tasklist')  

def taskupdate(request,tid):
    listdata = Task.objects.get(user_id=request.user.id, id=tid)  
    return render(request, 'task_list.html', {'listdata':listdata})
       
@login_required(login_url='/login')
def taskupdate(request,tid):
    my_record = Task.objects.get(id=tid)
    if request.method == "POST":
        task_form = TaskEditForm(request.POST or None, instance = my_record)
        
        if task_form.is_valid():            
            task_form.save()
            messages.success(request, 'Your Task has been updated successfully.') 
            return HttpResponseRedirect("/tasklist")
        else:
            messages.error(request, 'Please fill mandatory fields')
            return HttpResponseRedirect("/addtask") 
              
    else:
        task_form = TaskEditForm(instance = my_record)        

    context = { 'form' :task_form, }
    return render(request, 'edit_task.html', context)
   