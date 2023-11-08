"""Define URL patterns for pizzas."""
from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all pizza's
    path('pizzas/', views.pizzas, name='pizzas'),
    # Details of a single pizza
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]
