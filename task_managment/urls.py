from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('user.urls')),
    path('api/v1/', include('task.urls')),
]