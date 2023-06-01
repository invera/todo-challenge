from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser

from api_tasks.common.base_view import BaseView
from api_tasks.models import User
from api_tasks.serializers import RegisterSerializer, AllTasksSerializer


class RegisterView(CreateAPIView):
    """View that handles user registrations

    Note:
        You must send a Json object with the keys described below

    Args:
        fisrt_name (str, required): First Name
        last_name (str, required): Last Name
        password (str, required): Password
        password2 (str, required): Password2
        email (str, required): Email
        username (str, required): Username

    Returns:
        Json object with the entered data
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class TasksViewSet(BaseView):
    """View that handles the CRUD of tasks

    Args:
        title (str, required): Title task
        description (str, required): Description task
        is_completed (str, optional): Set if the task was completed or not
    """
    pagination_class = PageNumberPagination

    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
    def all(self, request):
        """Method that gets all tasks. Admin users only!.

        Args:
            request (Request): request of type GET

        Returns:
            A List of objects with all existing tasks
        """
        page = self.paginate_queryset(self.queryset.all())
        serializer = AllTasksSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def perform_create(self, serializer):
        """Method that relates an owner to the task.

        Args:
            serializer (Serializer): Serialized data

        Returns:
            Json object with the entered data
        """
        serializer.save(owner=self.request.user)