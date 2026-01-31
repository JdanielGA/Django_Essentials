# tasks/views.py
from django.shortcuts import render
from .models import Task

# Lists view to display all tasks.
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)

# Detail Task View.
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {'task': task}
    return render(request, 'tasks/task_details.html', context)
