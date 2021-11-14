# Django REST Framework
from rest_framework import viewsets

# Serializers
from todo.management.serializers import TaskModelSerializer

# Models
from todo.management.models import Task

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from todo.users.permissions import IsThisOwner
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskModelSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('title', 'date_to_finish', 'is_finalize', 'description')
    ordering_fields = ('title', 'date_to_finish', 'is_finalize', 'description', 'priority', 'color')
    ordering = ()
    filterset_fields = ('title', 'date_to_finish', 'is_finalize', 'description', 'created', 'priority', 'color')

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated, ]
        if self.action in ['update', 'partial_update', 'destroy', 'retrieve']:
            permissions.append(IsThisOwner)
        return [permission() for permission in permissions]

    def get_queryset(self):
        """Devolvemos el queryset modificado"""
        queryset = Task.objects.all()
        queryset = queryset.filter(user=self.request.user, is_active=True)
        return queryset
