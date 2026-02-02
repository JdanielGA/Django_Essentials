# tasks/forms.py
from django import forms
from .models import Task

# Form for creating and updating Task instances.
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']