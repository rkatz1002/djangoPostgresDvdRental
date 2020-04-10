from django.urls import include, path
from .views import get_brute_amout_of_income

urlpatterns = [
    path('brute_amount_income/', get_brute_amout_of_income, name='income'),
]