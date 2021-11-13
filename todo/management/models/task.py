# Django
from django.db import models

# Utils
from todo.utils.models import FunctionAbstractModel


class Task(FunctionAbstractModel):
    """ Modelo de Tarea

    Extiende de FunctionAbstractModel para las metricas
    """

    title = models.CharField(
        "Titulo",
        max_length=50
    )

    description = models.TextField(
        'Descripcion',
        max_length=500,
        blank=True,
        null=True
    )

    date_to_finish = models.DateTimeField(
        'Fecha a cumplir',
        blank=True,
        null=True
    )

    is_finalize = models.BooleanField(
        'Finalizado?',
        default=False,
        blank=True
    )

    COLOR_OPTIONS = (
        ('C1', '#f22c2b'),
        ('C2', '#71db7a'),
        ('C3', '#395fd0'),
    )

    color = models.CharField(
        'Color',
        default='C2',
        max_length=2,
        choices=COLOR_OPTIONS,
        blank=True,
    )

    PRIORITY_OPTIONS = (
        ('P1', 'Muy importante'),
        ('P2', 'Medianamente importante'),
        ('P3', 'Poco importante'),
    )

    priority = models.CharField(
        'Prioridad',
        default='P2',
        max_length=2,
        choices=PRIORITY_OPTIONS,
        blank=True,
    )

    def __str__(self):
        """Regresa el nombre de Taske"""
        return self.title
