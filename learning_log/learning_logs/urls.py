"""Defines url patterns for learning_logs."""

from django.urls import path
from . import views  # import views.py

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index')  # def index() in views.py
]
