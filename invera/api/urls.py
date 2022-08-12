
from django.urls import path
from api.views import *

from .routers import router

app_name= "api"

urlpatterns = [
    #View
    path('task/list/', TaskApiView.as_view(), name="taskapi_list"),
    path('task/completedlist/', TaskCompletedApiView.as_view(), name="taskapi_list_completed"),
    
    #User List
    path('userlist/', UserList.as_view(), name="user_list"),
    


]

#routers
urlpatterns += router.urls