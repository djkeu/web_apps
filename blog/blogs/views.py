from django.shortcuts import render

# Create your views here.

def index(request):
    """Home page for blogs."""
    return render(request, 'blogs/index.html')

def blogposts(request):
    """Page for all blogposts."""
    return render(request, 'blogposts/html')
