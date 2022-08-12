
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.authtoken.models import Token
from task.models import Task
from rest_framework.views import APIView

from api.serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import status
from rest_framework.response import Response



#User
class UserList2(ListCreateAPIView):
    serializer_class =UserSerializer
    queryset = User.objects.all()
    permission_classes= [IsAuthenticated]
    authentication_class= [TokenAuthentication]




#login
class Login(FormView):
    template_name= 'login.html'
    form_class= AuthenticationForm
    success_url= reverse_lazy('api:user_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args, *kwargs)

    def form_valid(self,form):
        user = authenticate(username= form.cleaned_data['username'], password=form.cleaned_data['password'])
        token,_= Token.objects.get_or_create(user= user)
        if token:
            login(self.request, form.get_user())
            return super(Login, self).form_valid(form)

class Logout(APIView):
    def get(self, request, format= None):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            logout(request)
            return Response(status= status.HTTP_200_OK)
        else:
            return Response(status= status.HTTP_200_OK)
#Task Viewset
#----------------LIST TASKVIEWSET----------------#
    #----------------LIST TASKVIEWSET----------------#
        #----------------LIST TASKVIEWSET----------------#
class TaskViewSet(ModelViewSet):
    queryset= Task.objects.all()
    serializer_class= TaskSerializer
    filter_backends= [filters.SearchFilter]
    authentication_class= [TokenAuthentication]
    permission_classes= [IsAuthenticated]
    search_fields= ['name_task', 'date']
        #----------------LIST TASKVIEWSET----------------#
    #----------------LIST TASKVIEWSET----------------#
#----------------LIST TASKVIEWSET----------------#



#Task VOEWSSSSSS
    #----------------LIST TASK----------------#

class TaskApiView(ListAPIView):
    serializer_class =TaskSerializer 
    queryset = Task.objects.all()
    
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticated]

class TaskCompletedApiView(ListAPIView):
    serializer_class =TaskSerializer
    queryset = Task.objects.all()
    
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        #true 1 false 0
        return Task.objects.filter(completed__icontains=1)




        

    

    
