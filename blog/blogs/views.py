from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def index(request):
    return render(request, 'blogs/index.html')

# ToDo: def blog()

def blogpost(request, blogpost_id):
    """Show all blogposts."""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    blogposts = blogpost.blogpost_set.order_by('-date_added')
    context = {'blogpost': blogpost, 'blogposts': blogposts}
    return render(request, 'blogs/blogposts.html', context)
