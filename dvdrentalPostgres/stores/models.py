from django.db import models
from customer.models import *
from film.models import *
from django.contrib.auth.models import AbstractBaseUser, UserManager
from datetime import datetime as dt
# Create your models here.


class Staff(AbstractBaseUser):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    email = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.SmallIntegerField()
    active = models.BooleanField()
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateTimeField()
    picture = models.BinaryField(blank=True, null=True)
    is_superuser = models.BooleanField(default=True)
    last_login = models.DateTimeField(default=dt.now())
    is_staff = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = 'staff'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.OneToOneField(Staff, models.DO_NOTHING)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'store'

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, models.DO_NOTHING)
    store_id = models.SmallIntegerField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'inventory'