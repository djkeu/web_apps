from django.shortcuts import render

# Create your views here.

def index(request):
    """Home page for blogs."""
    return render(request, 'logs/index.html')
