"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    # path('', views.index, name='index'),
    path('', views.blogposts, name='index'),
    # Page for adding new blogpost
    path('new_post/', views.new_post, name='new_post'),
]
