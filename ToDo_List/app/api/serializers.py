from rest_framework.serializers import ModelSerializer
from app.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','title', 'content', 'created','deadline','author','finished')
        read_only_fields = ('created',)


