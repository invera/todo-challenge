# Django REST Framework
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed

# Serializers
from todo.users.serializers import ProfileModelSerializer

# Models
from todo.users.models import Profile

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from todo.users.permissions import IsThisOwner
from rest_framework.permissions import IsAuthenticated


class ProfileViewSet(viewsets.ModelViewSet):

    serializer_class = ProfileModelSerializer
    permissions = [IsAuthenticated, IsThisOwner]

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('first_name', 'last_name')
    ordering_fields = ('first_name', 'last_name')
    ordering = ()
    filterset_fields = ('first_name', 'last_name')

    def get_queryset(self):
        queryset = Profile.objects.all()
        queryset = queryset.filter(user=self.request.user, is_active=True)
        return queryset

    def destroy(self, request, pk=None):
        raise MethodNotAllowed('DELETE')

    def create(self, request, pk=None):
        raise MethodNotAllowed('CREATE')
