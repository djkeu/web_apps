from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Blog posts
    path('blogposts/', views.blogposts, name='blogposts'),
]