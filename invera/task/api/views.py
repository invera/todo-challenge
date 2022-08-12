from rest_framework.viewsets import ModelViewSet
from task.models import Task
from task.api.serializers import TaskSerializer

class TaskApiViewSet(ModelViewSet):
    serializer_class =TaskSerializer 
    queryset = Task.objects.all()