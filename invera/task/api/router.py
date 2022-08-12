from rest_framework.routers import DefaultRouter

from task.api.views import TaskApiViewSet


router_task= DefaultRouter()

router_task.register(prefix='task', basename='task', viewset=TaskApiViewSet)
