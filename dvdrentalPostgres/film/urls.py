from .views import get_specifc_movie_renters
from django.urls import include, path

urlpatterns = [
    path('specific_movie_renters/<int:film_id>/', get_specifc_movie_renters, name='movie_renters'),
]