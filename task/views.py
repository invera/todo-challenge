import datetime
import logging
import re
from datetime import date, datetime, timedelta

from django.core.exceptions import PermissionDenied, ValidationError
from django.db.models.query_utils import Q
from django.shortcuts import render
from rest_framework import filters, renderers, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer

logger = logging.getLogger('tarea-debug')
loggerInfo = logging.getLogger('tarea-info')



class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    lookup_field = 'guid' 
    queryset = Task.objects.exclude(status = 3).order_by("-created_date")
    serializer_class = TaskSerializer    


    def get_queryset(self):
        loggerInfo.info("get_queryset")

        logger.debug(self.kwargs)        

        if self.request.method == 'DELETE':
            logger.debug("queryset for delete")
            return Task.objects.all()


        elif self.request.method == 'GET' and ('dateFrom' in self.kwargs and 'dateTo' in self.kwargs) or 'text' in self.kwargs:
            logger.debug("queryset for Search Tareas")

            dateFrom = ""
            dateTo = ""
            text = ""

            if 'dateFrom' in self.kwargs:
                dateFrom = self.kwargs['dateFrom']
                if not dateFormatControl(dateFrom):
                    dateFrom = ""

            if 'dateTo' in self.kwargs:
                dateTo = self.kwargs['dateTo']
                if not dateFormatControl(dateTo):
                    dateTo = ""

            if 'text' in self.kwargs:
                text = self.kwargs['text']          

            logger.debug("dateFrom: " + dateFrom)
            logger.debug("dateTo: " + dateTo)
            logger.debug("text: " + text)            

            if(dateFrom != '' and dateTo != ''):
                dtDateFrom = datetime.strptime(dateFrom, "%Y-%m-%d")
                dtDateTo = datetime.strptime(dateTo, "%Y-%m-%d")

                dtDateTo = dtDateTo + timedelta(days=1) - timedelta(seconds=1)

                logger.debug("dtDateFrom: " + str(dtDateFrom))
                logger.debug("dtDateTo: " + str(dtDateTo))

                if(text != ''):
                    return Task.objects.exclude(status = 3).filter(Q(title__icontains=text) | Q(description__icontains=text), created_date__range=(dtDateFrom, dtDateTo)).order_by("-created_date")
                else:
                    return Task.objects.exclude(status = 3).filter(created_date__range=(dtDateFrom, dtDateTo)).order_by("-created_date")
            
            else:
                if(text != ''):
                    return Task.objects.exclude(status = 3).filter(Q(title__icontains=text) | Q(description__icontains=text)).order_by("-created_date")
                else:
                    return Task.objects.exclude(status = 3).order_by("-created_date")            

        else:
            logger.debug("generic queryset")
            return Task.objects.exclude(status = 3).order_by("-created_date")     


    def destroy(self, request, *args, **kwargs):

        loggerInfo.info('Destroy')
        instance = self.get_object()

        if(instance.status != 3):
            logger.debug('Status != 3')
            instance.status = 3
            instance.save()
            return Response(data='delete success', status=status.HTTP_200_OK)
        
        else:
            logger.debug('Status = 3')
            return Response(data='The task was already deleted', status=status.HTTP_406_NOT_ACCEPTABLE)
            




def dateFormatControl(date):
    if re.match("[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])", date):
        logger.debug("ok format date")
        return True
    else:
        logger.debug("error in format date")
        logger.error("error in format date")
        return False


