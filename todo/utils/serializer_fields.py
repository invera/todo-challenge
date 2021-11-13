# Django REST Framework
from rest_framework import serializers


class CompleteNameUser(serializers.StringRelatedField):
    def to_representation(self, value):
        complete_name = value.profile.first_name + ' ' + value.profile.last_name
        return complete_name
