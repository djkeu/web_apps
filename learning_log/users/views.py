from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register new user."""
    if request.method != 'POST':
        # Blank registration form
        form = UserCreationForm()
    else:
        # Process form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log in new user, redirect to home page
            login(request, new_user)
            return redirect('learning_logs:index')
        
    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
