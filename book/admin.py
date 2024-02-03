from django.contrib import admin

from .models import Book

myModels = [Book]  # iterable list
admin.site.register(myModels)