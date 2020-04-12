from django.contrib import admin

# Register your models here.

from .models import Language, Film, Actor, Category, Inventory

admin.site.register(Language)
admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Inventory)