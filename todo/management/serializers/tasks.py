# Django REST Framework
from rest_framework import serializers

# Model
from todo.management.models import Task

# Utils
from todo.utils.tasks import TaskMetrics
from todo.utils.serializer_fields import CompleteNameUser


class TaskModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    user = CompleteNameUser(many=False)

    class Meta:
        """Meta class"""

        model = Task
        fields = (
            'id', 'user', 'title',
            'date_to_finish', 'is_finalize',
            'description', 'created',
            'priority', 'color'
        )

        read_only_fields = (
            'id', 'user',
            'created',
        )

    def create(self, data):
        """Creacion de la tarea"""
        # Sacamos los datos que ya tenemos en el context
        user = self.context['request'].user

        data['is_finalize'] = False

        # Creamos la tarea
        task = Task.objects.create(
            user=user,
            **data
        )

        # Puntos al perfil
        TaskMetrics(action='Create', user=user)

        return task

    def update(self, instance, data):
        """Actualizacion de la tarea"""
        # Extraemos el user del contexto y mandamos la funcion update
        user = self.context['request'].user

        new_is_finalize = data.get('is_finalize', instance.is_finalize)
        if new_is_finalize != instance.is_finalize:
            TaskMetrics(action='Update', user=user, is_finalize=new_is_finalize)

        # Actualizamos los datos normales
        super(TaskModelSerializer, self).update(instance, data)

        return instance
