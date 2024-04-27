from django.shortcuts import render, redirect
from home.models import Task
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages


# Create your views here.
def home(request):
    allTasks = Task.objects.all()
    context = {'allTasks':allTasks}
    if request.method == "POST":
        taskTitle = request.POST['taskTitle']
        taskDes = request.POST['taskDes']
        res = Task(taskTitle=taskTitle, taskDes=taskDes)
        res.save()
        
        messages.success(request, f"Task added successfully")
        return render(request, "home.html",context) 
    return render(request, "home.html", context)

def task(request):
    return render(request, "addTask.html")
 