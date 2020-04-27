from django.shortcuts import render

# Create your views here.

# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})