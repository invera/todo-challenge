from django.contrib.auth.models import AbstractUser
from django.db import models

from api_tasks.common.base_model import Base


class User(AbstractUser):

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tasks(Base):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
