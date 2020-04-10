from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Language)
admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(FilmActor)
admin.site.register(Category)
admin.site.register(FilmCategory)