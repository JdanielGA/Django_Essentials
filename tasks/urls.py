# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('<int:task_id>/', views.task_detail, name='task_details'),
    path('new/', views.task_form, name='task_form'),
    path('<int:task_id>/edit/', views.task_update, name='task_update'),
]