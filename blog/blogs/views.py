from django.shortcuts import render

from .models import BlogPost

# Create your views here.
def index(request):
    """Home page for blogs."""
    return render(request, 'blogs/index.html')

def blogposts(request):
    """Show blogposts."""
    blogposts = BlogPost.objects.all()
    blogposts = blogposts.order_by('-date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/index.html', context)

def blogpost(request, blogpost_id):
    """Show single blogpost."""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    blogposts = blogpost.blogpost_set.order_by('-date_added')
    context ={'blogposts': blogposts, 'blogpost': blogpost}
    return render(request, 'blogs/blogpost.html', context)
