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
def get_specifc_movie_renters(request, film_id):

    film_id = int(film_id)

    raw_query = """
        SELECT first_name, last_name, email FROM public.film
        INNER JOIN public.inventory
        ON public.inventory.film_id = public.film.film_id
        INNER JOIN public.rental
        ON public.inventory.inventory_id = public.rental.inventory_id
        INNER JOIN public.customer
        ON public.customer.customer_id = public.rental.customer_id
        WHERE public.film.film_id = %s;
    """%str(film_id)
    
    with connection.cursor() as cursor:
        cursor.execute(raw_query)
        rows = dictfetchall(cursor)        

    return Response({'data':rows},status=200)
