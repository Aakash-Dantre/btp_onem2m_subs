from django.shortcuts import render
from django.db import connection
# Create your views here.
# from rest_framework.decorators import api_view

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# def index(request):
# 	return HttpResponse("Hello, world. You're at the polls index.")

# @api_view(['POST'])
@csrf_exempt
def waterpost(request):
    response = HttpResponse()
    # print('ldksjfds')
    # print(request)
    str=(request.body).decode(encoding = 'UTF-8',errors = 'strict')
    resp=json.loads(str)
    container=resp["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ri"].split("/in-cse/")[1]
    resp=resp["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"].split("[")[1].split("]")[0]
    resp=resp.split(',')
    # print(resp)

    query="INSERT INTO water(level,nodename,container_instance) VALUES ('{}','{}','{}')".format(resp[0],resp[1],container)
    cur=connection.cursor()
    cur.execute(query)
    connection.commit()
    cur.close()

    return response