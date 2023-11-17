from django.shortcuts import render

from .models import BlogPost

# Create your views here.
def index(request):
    """Home page for blogs."""
    return render(request, 'blogs/index.html')

def blogposts(request):
    """Show blogposts."""
    blogposts = BlogPost.objects.all()
    blogposts = blogposts.order_by('date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/index.html', context)
