from django.shortcuts import render

# Create your views here.
def index(request):
    """Home page for meal planner."""
    return render(request, 'meal_planner/index.html')
