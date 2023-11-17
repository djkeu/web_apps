"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    # path('', views.index, name='index'),
    path('', views.blogposts, name='index'),
    
    # Page for single post
    path('<int:post_id>/', views.post, name='post'),
    
    # Page for adding new blogpost
    path('new_post/', views.new_post, name='new_post'),

    # Page for editing a blogpost
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]
