from django.shortcuts import render
from .models import Task

def task_listing(request):
  tasks = Task.objects.all().order_by('-due_date')
  return render(
    request, 
    template_name = 'tasks.html',
    context = {
      'title': 'Liste des tâches',
      'tasks': tasks
    }
  )