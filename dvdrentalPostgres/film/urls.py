from .views import *
from django.urls import include, path

urlpatterns = [
    path('get_movies_categories/<int:film_id>/', get_movies_categories, name='income_by_movie'),
    path('specific_movie_renters/<int:film_id>/', get_specifc_movie_renters, name='movie_renters'),
]