from django.shortcuts import render, redirect

from .models import BlogPost
from forms import BlogForm

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

def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        # No data submitted; create blank form
        form = BlogForm()

    else:
        # POST data submitted;  process data
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogposts')
        
    # Display blank or invalid form
    context = [{'form': form}]
    return render(request, 'blogs/new_topic.html', context)
