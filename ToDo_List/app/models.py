from django.db import models
from django.contrib.auth. models import User

class Task(models.Model):
    title = models.CharField(max_length=50) 
    content = models.TextField(max_length=500)
    deadline = models.DateTimeField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(('finished'), default=False)
 
    class Meta:
        verbose_name='task'
        verbose_name_plural='tasks'

    def __str__(self):
        return self.title
    




