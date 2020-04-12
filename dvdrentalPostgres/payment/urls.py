from django.urls import include, path
from .views import *

try:
    urlpatterns = [
        path('brute_amount_income/', get_brute_amout_of_income, name='income'),
        path('income_from_specific_movie/', get_money_got_by_movie, name='income_by_movie'),
    ]
except:
    urlpatterns=[]