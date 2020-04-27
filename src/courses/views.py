from django.shortcuts import render, get_object_or_404 
from django.views import View 

from .forms import CourseModelForm
from .models import Course 
# Create your views here.

# BASE VIEW Class = VIEW 

class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    def get(self, request, *args, **kwargs):
        form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)


class CourseView(View): # make CourseView acts for both about and detail view
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

    # def post(request, *args, **kwargs):
    #     return render(request, 'about.html', {})  


# class CourseDetailView(View):
#     def get(self, request, *args, **kwargs):
#         template_name = 'about.html'
#         return render(request, template_name, {})


# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})