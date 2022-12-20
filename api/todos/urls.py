from django.urls import path
from api.todos.views import TodoView

urlpatterns = [
    path('todos/', TodoView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='todos'),
    path('todos/<int:pk>', TodoView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='todo_list'),
]