from django.contrib import admin

from .models import Song

myModels = [Song]  # iterable list
admin.site.register(myModels)