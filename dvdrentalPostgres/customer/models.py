from django.db import models

# Create your models here.


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'country'

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'city'

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey(City, models.DO_NOTHING)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'address'

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store_id = models.SmallIntegerField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    activebool = models.BooleanField()
    create_date = models.DateField()
    last_update = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'customer'

