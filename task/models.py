import datetime
import hashlib
import logging
import random

from django.db import models

logger = logging.getLogger('tarea-debug')
loggerInfo = logging.getLogger('tarea-info')

class Task(models.Model):
    guid = models.CharField(max_length=254, editable = False)
    title = models.CharField(max_length=50, null= False)
    description = models.CharField(max_length=500, null= False)
    created_date = models.DateTimeField(auto_now_add = True, null = True, blank = True)
    updated_date = models.DateTimeField(auto_now = True, null = True, blank = True)
    status = models.IntegerField(default=0, choices=((0, 'Actived'), (1, 'Finished'), (2, 'Canceled'), (3, 'Deleted')))



    class Meta:
        app_label = 'task'


    def save(self, *args, **kwargs):   
        loggerInfo.info('Save task')
        if(self.guid == '' or self.guid is None):   
            self.guid = hashlib.sha256(str(datetime.datetime.now()).encode('utf-8')).hexdigest()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
