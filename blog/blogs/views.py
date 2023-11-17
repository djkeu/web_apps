from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogForm

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

def post(request, post_id):
    """Single blog post."""
    post = BlogPost.objects.get(id=post_id)
    #posts = posts.order_by('-date_added')
    context = {'posts': post}
    return render(request, 'blogs/blogpost.html', context)

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
            return redirect('blogs:index')
        
    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)
    title = post.title

    if request.method != 'POST':
        # Initial request, pre-fill form with current data
        form = BlogForm(instance=post)
    else:
        # POST data submitted, process data
        form = BlogForm(instance=post,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post.id)
        
    context = {'post': post, 'title': title, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
