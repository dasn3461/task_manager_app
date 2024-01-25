from django.contrib import admin
from .models import Task, Photo

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'create_date', 'due_date', 'priority', 'completed', 'user')
    list_filter = ('priority', 'completed', 'user')
    search_fields = ('title', 'description')
    date_hierarchy = 'create_date'
    ordering = ('priority', 'due_date')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('task', 'image')
    search_fields = ('task__title',)

