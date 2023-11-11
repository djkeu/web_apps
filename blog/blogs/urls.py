"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
url_patterns = [
    # Home page
    path('', views.index, name='index'),
]
