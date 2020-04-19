from django import forms
from django.contrib import admin
from .models import * 

class StoreAdmin(admin.ModelAdmin):

    list_display = ('manager_staff', 'address', 'last_update')
    fieldsets = (
        ('Store Location', {'fields': ('address',)}),
        ('Detalhes', {'fields': ('manager_staff','last_update')}),
    )

admin.site.register(Store, StoreAdmin)