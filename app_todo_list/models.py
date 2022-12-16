from django.db import models
from django.utils import timezone


class ToDo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField()
    todo_create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{0},{1},{2},{3}'.format(self.title, self.description, self.completed, self.todo_create_date.strftime('%d-%m-%Y'))
