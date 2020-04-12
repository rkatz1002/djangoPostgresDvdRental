from django.db import models
from staff.models import Staff

# Create your models here.
class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name 

class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_update = models.DateTimeField()
    special_features = models.TextField(blank=True, null=True)  # This field type is a guess.
    fulltext = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'film'

    def __str__(self):
        return self.title    

class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'actor'

    def __str__(self):
        return self.first_name + ' ' + self.last_name  

class FilmActor(models.Model):
    actor = models.OneToOneField(Actor, models.DO_NOTHING, primary_key=True)
    film = models.ForeignKey(Film, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'film_actor'

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'category'
    
    def __str__(self):
        return self.name

class FilmCategory(models.Model):
    film = models.OneToOneField(Film, models.DO_NOTHING, primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'film_category'



class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, models.DO_NOTHING)
    store_id = models.SmallIntegerField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'inventory'
    
    def __str__(self):
        return self.film.title