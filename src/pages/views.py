from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): 
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1> Hello World</h1>") # string of HTML code
    return render(request, 'home.html', {})


def contact_view(*args, **kwargs): 
    return HttpResponse("<h1> Contact Page</h1>")


def about_view(request, *args, **kwargs): 
    # 'about.html' is template
    # context is a dictionary consists of any data types. 
    my_context = {
        'my_text': 'This is about us.',
        'my_number': 123, 
        'my_list': [123, 234, 'qian']
    }
    return render(request, 'about.html', my_context)
    