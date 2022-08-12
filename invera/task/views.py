from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic import View

from .forms import TaskForm
from .models import Task

# Create your views here.

def view_task(request):
    try:
        user_id= request.user.id
        task_by_user= Task.objects.filter(author=user_id)
        message= "You can only read your tasks"
                
        return render(request, "task/task.html", {"tasks":task_by_user, "msg":message})

    except request.user.id == None:
        
        return render(request, "home/home.html")


def view_all_task(request):
        task_by_user= Task.objects.all()
        return render(request, "task/task.html", {"tasks":task_by_user})


    
def search_task(request):
    if request.GET.get("name"):
        name = request.GET.get("name")
        tasks= Task.objects.filter(name_task__icontains=name).order_by('name_task') | Task.objects.filter(date__icontains=name).order_by('date')
        print(request.GET, "print seeker")

         
        return render(request, "task/result_task.html", {"task":tasks, "nombre":name} )

    else:
        return render (request, "task/search_task.html")


class DetailTask(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task/detail_task.html"

class FormTaskView(HTTPResponse):

    def index(request):
        form = TaskForm()
        return render (request, "task/create_task.html", {"form":form})
    
    def create_task(request):
        form = TaskForm()
        if form.is_valid():
            form.save()
            print(form)
            form= TaskForm()

        else:
            print("error")


        return render(request,"task/create_task.html", {"form":form})
        