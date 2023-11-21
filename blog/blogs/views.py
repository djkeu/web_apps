from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogForm

# Create your views here.
def index(request):
    """Home page for blogs."""
    return render(request, 'blogs/index.html')

@login_required
def blogposts(request):
    """Show blogposts."""
    blogposts = BlogPost.objects.all()
    blogposts = blogposts.order_by('-date_added')

    context = {'blogposts': blogposts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        # No data submitted; create blank form
        form = BlogForm()

    else:
        # POST data submitted;  process data
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')
        
    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)
    title = post.title
    if post.owner != request.user:
        # raise Http404  # Create different template to handle 404
        return redirect('blogs:index')

    if request.method != 'POST':
        # Initial request, pre-fill form with current data
        form = BlogForm(instance=post)
    else:
        # POST data submitted, process data
        form = BlogForm(instance=post,data=request.POST)
        if form.is_valid():
            form.save()
            # return redirect('blogs:post', post_id=post.id)
            return redirect('blogs:index')
        
    context = {'post': post, 'title': title, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
