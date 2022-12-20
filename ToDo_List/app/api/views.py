from rest_framework.viewsets import ModelViewSet
from app.models import Task
from app.api.serializers import TaskSerializer
from rest_framework import filters


class TaskApiViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']
