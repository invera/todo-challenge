from django.conf.urls import include, url
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from task.views import TaskViewSet

task_list = TaskViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
task_detail = TaskViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
task_search = TaskViewSet.as_view({
    'get': 'list'
})



urlpatterns = format_suffix_patterns([
    path('tareas/', task_list, name='tareas-list'),
    re_path('^tareas/(?P<guid>[A-Fa-f0-9]{64})', task_detail, name='tareas-detail'),
    re_path('^tareas/search/(?P<dateFrom>(?:20)[0-9]{2}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-9])|(?:(?!02)(?:0[1-9]|1[0-2])-(?:30))|(?:(?:0[13578]|1[02])-31)))/(?P<dateTo>(?:20)[0-9]{2}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-9])|(?:(?!02)(?:0[1-9]|1[0-2])-(?:30))|(?:(?:0[13578]|1[02])-31)))/(?P<text>\w+)', task_search, name='tareas-search'),    
    re_path('^tareas/search/(?P<dateFrom>(?:20)[0-9]{2}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-9])|(?:(?!02)(?:0[1-9]|1[0-2])-(?:30))|(?:(?:0[13578]|1[02])-31)))/(?P<dateTo>(?:20)[0-9]{2}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-9])|(?:(?!02)(?:0[1-9]|1[0-2])-(?:30))|(?:(?:0[13578]|1[02])-31)))', task_search, name='tareas-search'),    
    re_path('^tareas/search/(?P<text>\w+)', task_search, name='tareas-search'),       
])




