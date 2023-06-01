from django.contrib import admin

from api_tasks.models import Tasks, User


@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_completed', 'owner', 'created_at', 'updated_at')
    search_fields = ('title', 'created_at', 'owner')
    ordering = ('-created_at',)
    list_per_page = 25

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'username', 'is_staff')
    search_fields = ('email', 'username')