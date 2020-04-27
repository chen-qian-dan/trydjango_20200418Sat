from django.urls import path 
from .views import (
    CourseView, 
    #my_fbv
)

app_name = 'courses'
urlpatterns = [
    path('', CourseView.as_view(), name='courses-list'), 
    #path('', my_fbv, name='courses-list'), 

]