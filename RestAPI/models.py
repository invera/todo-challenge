from django.db import models

# Create your models here.


class Task(models.Model):
    Job = models.CharField(max_length=250)
    Auto_Date = models.DateTimeField(auto_now=True)  # For data consistency
    Date = models.CharField(max_length=10)  # For filtering
    Done = models.BooleanField()
