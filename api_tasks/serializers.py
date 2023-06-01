from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api_tasks.models import Tasks, User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user

class TasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'created_at', 'is_completed']
        extra_kwargs = {'owner': {'required': False, 'write_only': False}}


class AllTasksSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'created_at', 'is_completed', 'owner']
