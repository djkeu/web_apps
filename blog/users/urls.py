"""Url patterns for users."""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Auth urls
    path('', include('django.contrib.auth.urls')),
]