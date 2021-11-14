# Django REST Framework
from rest_framework import serializers

# Models
from todo.users.models import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        model = Profile
        fields = (
            'id',
            'first_name', 'last_name',
            'country', 'biografy',
            'picture', 'picture',
            'tasks_finalize', 'tasks_pending',
            'tasks_created'
        )

        read_only_fields = (
            'id', 'tasks_finalize', 'tasks_pending',
            'tasks_created'
        )

        depth = 0

    def update(self, instance, data):
        """Cambios al perfil"""

        if instance.picture != data.get('picture', False):
            instance.picture.delete()
            instance.picture = data.get('picture')
            instance.save()

        super(ProfileModelSerializer, self).update(instance, data)

        return instance
