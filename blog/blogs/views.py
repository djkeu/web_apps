from django.shortcuts import render

from .models import BlogPost
# Create your views here.

def index(request):
    """Home page for blogs."""
    return render(request, 'blogs/index.html')

def blogpost(request, blogpost_id):
    """Page for all blogposts."""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    blogposts = blogpost.blogpost_set.order_by('-date_added')

    context = {'blogpost': blogpost, 'blogposts': blogposts}
    return render(request, 'blogposts/html', context)
    # FixMe: blogposts not showing

