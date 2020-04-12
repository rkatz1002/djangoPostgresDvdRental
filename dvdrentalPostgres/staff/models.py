import django.db.models as models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from datetime import datetime as dt



class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'country'
    def __str__(self):
        return self.country

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'city'
    def __str__(self):
        return self.city

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

    def __str__(self):
        return self.address


class StaffUserManager(BaseUserManager):
    def create_user(self, username, password, email, first_name, last_name):
        
        if not username or not password:
            raise ValueError('Users missing username or password')

        user = self.model(
            username=username,
            first_name=first_name,
            password=make_password(password),
            email=email,
            last_name = last_name,
            store_id=1,
            active=True,
            last_login=dt.now()
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email, first_name, last_name):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.save(using=self._db)
        return user

class Staff(AbstractBaseUser):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, models.DO_NOTHING, default=1)
    email = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.SmallIntegerField()
    active = models.BooleanField()
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    last_login = models.DateTimeField(db_column='last_update')
    picture = models.BinaryField(blank=True, null=True)
    is_staff = models.BooleanField(default=True)

    objects = StaffUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name', 'email']

    def __str__(self):
        if self.first_name != None:
            return self.first_name + ' ' + self.last_name
        else:
            return self.username
    
    def has_module_perms(self, is_staff):
        return True

    def has_perm(self, is_staff):
        return True

    class Meta:
        db_table = 'staff'

