from django.contrib import admin
from django.urls import path, include

from app.api.router import router_task

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include(router_task.urls)),
    path('logs/', include('app.urls')),
]

