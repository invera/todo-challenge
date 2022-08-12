from django.db import models
from django.forms import model_to_dict

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#User.username()

class Task(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    #author_name=models.CharField(default=, max_length=30)
    name_task= models.CharField(max_length=30)
    date= models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)

    class Meta:
        verbose_name= "Task"
        verbose_name_plural= "Tasks"

    def __str__(self):
        return f"{self.name_task} ({self.author.username})"
    
    #Para que la API se visualize mejor 
    def toJson(self):
        item= model_to_dict(self)
        #item["full_name"] = self.__str__()
        item["author(user)"] = self.author.username
        item["email(user)"] = self.author.email
        item["date_task"] = self.date
        return item


