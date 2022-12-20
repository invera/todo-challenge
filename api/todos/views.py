from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from api.todos.models import Todo
from api.todos.serializers import TodoSerializer


class TodoView(ModelViewSet):
    filter_backends = (SearchFilter,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    search_fields = ('name', 'description', 'created')
    ordering_fields = ['created']
    pagination_class = PageNumberPagination
    pagination_class.page_size = 8