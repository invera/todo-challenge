from rest_framework.serializers import ModelSerializer
from task.models import Task

from django.contrib.auth.models import User

class TaskSerializer(ModelSerializer):
    class Meta:
        model= Task
        fields= ['author', 'name_task', 'date', 'completed']

    def to_representation(self, instance):
            return instance.toJson()
        


class UserSerializer(ModelSerializer):
    class Meta:
        model= User
        fields= '__all__'
        

    