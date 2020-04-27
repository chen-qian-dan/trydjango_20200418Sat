from django.shortcuts import render
from django.views import View 

# Create your views here.

# BASE VIEW Class = VIEW 
class CourseView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'about.html'
        return render(request, template_name, {})

    # def post(request, *args, **kwargs):
    #     return render(request, 'about.html', {})  


# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})