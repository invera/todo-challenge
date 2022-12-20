from .models import Task
from django.contrib import admin

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created','deadline')
    ordering = ('author', 'created')
    search_fields = ('content',)
    date_hierarchy = 'created'
    list_filter = ('finished',)

admin.site.site_header = "Invera Task"
admin.site.register(Task, TaskAdmin)

