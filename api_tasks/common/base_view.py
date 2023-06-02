from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api_tasks.models import Tasks
from api_tasks.serializers import TasksSerializer


class BaseView(ModelViewSet):
    queryset = Tasks.objects
    permission_classes = [IsAuthenticated]
    serializer_class = TasksSerializer
    filter_backends = []

    def get_queryset(self):
        request = self.request.query_params.dict()
        filterdict = {}

        if request.get('created_at'):
            filterdict['created_at__date'] = request.get('created_at')
        if request.get('title'):
            filterdict['title__contains'] = request.get('title')

        filterdict['owner'] = self.request.user.id
        return self.queryset.filter(**filterdict).order_by('-id')