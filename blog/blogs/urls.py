"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    #path('', views.index, name='index'),
    path('', views.blogposts, name='index'),
    path('/<int:blogpost_id', views.blogpost, name='blogpost'),
]
