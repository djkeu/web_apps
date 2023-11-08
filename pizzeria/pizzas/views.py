from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    """Home page for Pizzeria."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """All pizza's."""
    pizzas = Pizza.objects.order_by('id')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, topic_id):
    """Single pizza with toppings."""
    pizza = Pizza.objects.get(id=topic_id)
    toppings = pizza.entry_set
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)
