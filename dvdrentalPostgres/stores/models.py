from django.db import models
from customer.models import Address
from datetime import datetime as dt
from staff.models import Staff

class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.OneToOneField(Staff, models.DO_NOTHING)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'store'
    
    def __str__(self):
        return self.manager_staff
