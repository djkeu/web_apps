from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page that shows all blogs
    # path('blogs/', views.blogs, name='blogs'),
    path('blogposts/', views.blogposts, name='blogposts'),

    # Detail page for a blogpost
    # path('blogs/<int:blogpost_id>/', views.blogpost, name='blogpost'),
]
