from django import forms
from .models import Task
from django.contrib.auth.models import User


class TaskForm(forms.Form):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(
                attrs={
                    "type":"date"
                }
            )
        }
