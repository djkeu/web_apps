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

def pizza(request, pizza_id):
    """Single pizza with toppings."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-id')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)
