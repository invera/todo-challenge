from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import TaskSerializer
from .models import Task

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter]
    search_fields = ['Job', 'Date']
