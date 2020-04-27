from django.urls import path 
from .views import (
    CourseView, 
    CourseListView,
    CourseCreateView,
    CourseUpdateView,
    #my_fbv
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='courses-list'),
   # path('', CourseView.as_view(template_name='home'), name='courses-list'), 
    path('create/', CourseCreateView.as_view(), name='courses-create'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'),
    #path('', my_fbv, name='courses-list'), 

]