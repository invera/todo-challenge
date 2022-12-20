from django.http import HttpResponse

from django.contrib.admin.models import LogEntry
    
def index(request):
    return HttpResponse(LogEntry.objects.all())