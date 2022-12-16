from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = (
            'id',
            'title',
            'description',
            'completed',
            'todo_create_date',
        )
