from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(max_length=250, null=False, default='')
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    
    def __str__(self):
        return self.name