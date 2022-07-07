from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        id = serializers.ReadOnlyField()
        fields = ['id', 'Job', 'Auto_Date', 'Date', 'Done']
