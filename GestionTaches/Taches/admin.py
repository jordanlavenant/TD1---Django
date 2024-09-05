from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
  list_display = ('name', 'description', 'created_date', 'closed', 'due_date', 'schedule_date')
  read_only = ('created_date')

admin.site.register(Task, TaskAdmin)