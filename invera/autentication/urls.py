from django.urls import path

from autentication.views import *



urlpatterns = [
   
    path('', home, name="Home"),
    path("register/",RegisterUser.as_view(), name= "Autentication"),
    path("session_out/", session_out, name="SessionOut"),
    path("log/", log, name="Log"),

    
    


]
