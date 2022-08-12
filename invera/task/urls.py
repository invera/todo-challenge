
from django.urls import path

from task.views import *


urlpatterns = [
   
    path('', view_task, name="Tasksss"),

    
    path("view_task/", view_task, name="ViewTask"),
    path("view_all_task/", view_all_task, name="ViewAllTask"),
    path("search-task/", search_task, name="SearchTask"),
    path('task-detail/<pk>', DetailTask.as_view(), name = "TaskDetail"),
    #path("create-task/", FormTaskView.index, name= "CreateTask"),
    #path("save-task/", FormTaskView.create_task, name= "SaveTask")
    
    


]