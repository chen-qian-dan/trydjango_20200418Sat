from django.contrib import admin
# . means models.py and admin.py are on the same directory level. 
# this kind of import called 'relative import'.
from .models import Product

# Register your models here.

admin.site.register(Product)
