from rest_framework.serializers import ModelSerializer
from task.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model= Task
        fields= ['author', 'name_task', 'date', 'completed']