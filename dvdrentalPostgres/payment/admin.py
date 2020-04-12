from django.contrib import admin

# Register your models here.

from .models import Rental, Payment


admin.site.register(Rental)
admin.site.register(Payment)