from django.shortcuts import render
from django.db import connection
from staff.models import *
from django.forms.models import model_to_dict

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def get_all_staff(request):
    staff_members = Staff.objects.all()
    res = []
    for member in staff_members:
        res.append(model_to_dict(member))
    return Response(res,status=200)