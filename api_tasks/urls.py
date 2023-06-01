from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_tasks.views import TasksViewSet, RegisterView

router = DefaultRouter()
router.register(r'tasks', TasksViewSet, basename="task")
register = RegisterView.as_view()

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('register/', register),
]