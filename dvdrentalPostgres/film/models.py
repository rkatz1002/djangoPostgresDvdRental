from django.db import models

# Create your models here.
class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'language'

class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_update = models.DateTimeField()
    special_features = models.TextField(blank=True, null=True)  # This field type is a guess.
    fulltext = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film'

class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'actor'

class FilmActor(models.Model):
    actor = models.OneToOneField(Actor, models.DO_NOTHING, primary_key=True)
    film = models.ForeignKey(Film, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_actor'
        unique_together = (('actor', 'film'),)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category'

class FilmCategory(models.Model):
    film = models.OneToOneField(Film, models.DO_NOTHING, primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_category'
        unique_together = (('film', 'category'),)




