# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('url/task/', views.task_view, name='task_view'),
]
