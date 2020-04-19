from django.contrib import admin

# Register your models here.

from .models import Rental, Payment

class RentalAdmin(admin.ModelAdmin):

    list_display = ('customer', 'return_date', 'staff')
    fieldsets = (
        ('Rental Dates', {'fields': ('retal_date', 'return_date')}),
        ('Rental Details', {'fields': ('inventory','customer')}),
        ('Staff Details', {'fields': ('staff','last_update')}),
    )

class PaymentAdmin(admin.ModelAdmin):

    list_display = ('customer', 'amount', 'staff' ,'rental')
    fieldsets = (
        ('Payment Detail', {'fields': ('customer', 'amount',)}),
        ('Payment Dates', {'fields': ('payment_date',)}),
        ('Staff Details', {'fields': ('staff','rental')}),
    )

admin.site.register(Rental, RentalAdmin)
admin.site.register(Payment, PaymentAdmin)