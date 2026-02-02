# tasks/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

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

# Form View for creating tasks.
def task_form(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'tasks/task_form.html', context)

# Form View for updating tasks.
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    context = {'form': form, 'task': task}
    return render(request, 'tasks/update_task.html', context)

# Delete Task View.
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    context = {'task': task}
    return render(request, 'tasks/task_confirm_delete.html', context)