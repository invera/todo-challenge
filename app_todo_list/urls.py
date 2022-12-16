from django.urls import path
from .views import ListToDoGenerics, ToDoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/todo', ListToDoGenerics.as_view(), name='todo_list'),
    path('api/v1/todo/<int:id>', ToDoRetrieveUpdateDestroyAPIView.as_view(), name='todo_list_destroy'),
]
