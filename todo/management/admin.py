# Django
from django.contrib import admin

# Models
from todo.management.models import (Task)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Admin de Task"""

    list_display = ('title', 'date_to_finish', 'is_finalize', 'description', 'priority', 'color')
    search_filter = ('title', 'description')
    list_filter = ('created', 'modified', 'date_to_finish', 'is_finalize', 'priority', 'color')
