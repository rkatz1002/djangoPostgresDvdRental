from django.shortcuts import render
from django.shortcuts import render
from django.db import connection

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


@api_view(['GET'])
def get_brute_amout_of_income(request):

    raw_query = """
        SELECT SUM(public.payment.amount) FROM public.payment;
    """
    
    with connection.cursor() as cursor:
        cursor.execute(raw_query)
        rows = dictfetchall(cursor)        

    return Response({'data':rows},status=200)


@api_view(['POST'])
def get_money_got_by_movie(request):

    film_id = request.data['film_id']

    raw_query = """
        SELECT SUM(public.payment.amount) FROM payment
        INNER JOIN rental
        ON payment.rental_id = rental.rental_id
        INNER JOIN inventory
        ON inventory.inventory_id = rental.inventory_id
        INNER JOIN film
        ON inventory.film_id = film.film_id
        WHERE film.film_id = %d
    """%int(film_id)
    
    with connection.cursor() as cursor:
        cursor.execute(raw_query)
        rows = dictfetchall(cursor)        

    return Response({'data':rows},status=200)