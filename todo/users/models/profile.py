# Django
from django.db import models

# Utils
from todo.utils.models import UserAbstractModel


class Profile(UserAbstractModel):
    """Modelo del perfil

    El modelo del perfil contiene su data publica, como biografia, imagen y estadistica
    """

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)

    picture = models.ImageField(
        "imagen de perfil",
        upload_to="users/pictures/",
        blank=True,
        null=True
    )

    first_name = models.CharField(
        "Nombre del perfil",
        max_length=30,
    )

    last_name = models.CharField(
        "Apellido del perfil",
        max_length=30,
    )

    country = models.CharField(
        "Pais del cliente",
        max_length=50,
        blank=True,
        null=True
    )

    biografy = models.TextField('Biografia del perfil', max_length=500, blank=True)

    tasks_finalize = models.IntegerField(
        'Tareas finalizadas',
        default=0,
        blank=True
    )

    tasks_pending = models.IntegerField(
        'Tareas pendientes',
        default=0,
        blank=True
    )
    tasks_created = models.IntegerField(
        'Tareas creadas',
        default=0,
        blank=True
    )

    def __str__(self):
        """Regresa el nombre del perfil"""
        return self.first_name
