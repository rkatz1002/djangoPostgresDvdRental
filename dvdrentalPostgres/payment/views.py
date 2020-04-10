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