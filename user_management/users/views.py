from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been added successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserForm()
    
    return render(request, 'index.html', {'form': form})
