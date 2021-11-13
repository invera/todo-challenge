# Django
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Tasks
from todo.taskapp.tasks import send_confirmation_email

# Models
from todo.users.models import User, Profile

# Utils
from todo.utils.authenticate import get_tokens_for_user


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'id',
            'username',
            'email',
            'phone_number',
        )
        read_only_fields = (
            'id',
        )


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.
    Funcionamiento del login de usuario
    """

    username = serializers.CharField(min_length=2)
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['username'], password=data['password'])

        if not user:
            raise serializers.ValidationError(
                '1001: Error al iniciar sesion, credenciales invalidas'
            )
        if not user.is_verified:
            raise serializers.ValidationError(
                '1002: Error al iniciar sesion, el usuario necesita ser activado'
            )

        self.context['user'] = user

        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token = get_tokens_for_user(self.context['user'])

        return self.context['user'], token


class UserSignUpSerializer(serializers.Serializer):

    """User sign up serializer.
    Funcionamiento de la creacion de cuenta y usuario, con sus validadores
    """
    # User
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)

    # Profile
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    # Phone number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = serializers.CharField(validators=[phone_regex], required=False)

    def create(self, data):
        """Creacion de la cuenta principal y usuario admin"""

        # User
        user = User.objects.create_user(
            email=data['email'],
            username=data['username'],
            password=data['password'],
            is_verified=True,
            phone_number=data['phone_number']
        )

        # Mandamos el email de verificacion
        send_confirmation_email.delay(user_pk=user.pk, password=data['password'])

        Profile.objects.create(user=user, first_name=data['first_name'], last_name=data['last_name'])

        return user


class ChangePasswordSerializer(serializers.Serializer):
    """Serializer del cambio de contraseña."""

    old_password = serializers.CharField()
    new_password = serializers.CharField(min_length=8)
    new_password_confirmation = serializers.CharField(min_length=8)

    def validate_old_password(self, data):
        """Validamos la contraseña vieja/actual"""
        user = self.context['request'].user
        if not user.check_password(data):
            raise serializers.ValidationError('1020: La contraseña que indico no es la correcta')

        return data

    def validate(self, data):
        """Validamos las nuevas contraseñas"""
        passw = data['new_password']
        passw_conf = data['new_password_confirmation']

        if passw != passw_conf:
            raise serializers.ValidationError('1021: Las contraseñas no concuerdan')

        self.context['password'] = data['new_password']
        return data

    def save(self):
        """Update user's verified status."""
        user = self.context['request'].user
        user.set_password(self.context['password'])
        user.save()

        return self.context['password']
