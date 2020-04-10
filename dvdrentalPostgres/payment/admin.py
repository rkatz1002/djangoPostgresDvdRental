from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Staff)
admin.site.register(Store)
admin.site.register(Inventory)
admin.site.register(Rental)
admin.site.register(Payment)