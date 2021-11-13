# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Vistas
from .views import users as users_view
from .views import profiles as profiles_view

router = DefaultRouter()
router.register(r"users", users_view.UserViewSet, basename="user")
router.register(r"profiles", profiles_view.ProfileViewSet, basename="profile")


urlpatterns = [
    path("", include(router.urls))
]
