from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import ToDo
from .serializers import ToDoSerializer


class ListToDoGenerics(generics.ListAPIView, generics.ListCreateAPIView):
    """ View created by class from generic rest_framework.
    GET, POST
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'title', 'description', 'completed', 'todo_create_date']
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ View created by class from generic rest_framework overwriting default methods.
    DELETE, PUT
    """
    queryset = ToDo.objects.all()
    lookup_field = 'id'
    serializer_class = ToDoSerializer

    def delete(self, request, *args, **kwargs):
        try:
            get_id = request.data.get('id', None)
            response = super().delete(request, *args, **kwargs)

            if response.status_code == 204:
                from django.core.cache import cache
                cache.delete("{}".format(get_id))
                return response

        except Exception as e:
            return Response({
                "Message ": "Failed"
            })

    def patch(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            mydata = response.data

            from django.core.cache import cache
            cache.set("ID :{}".format(mydata.get('id', None)), {
                      'title': mydata['title'],
                      'description': mydata['description'],
                      'completed': mydata['completed']})

            return response
