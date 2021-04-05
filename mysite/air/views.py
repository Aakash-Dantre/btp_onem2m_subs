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
def airpost(request):
    response = HttpResponse()
    # print('ldksjfds')
    # print(request)
    str=(request.body).decode(encoding = 'UTF-8',errors = 'strict')
    resp=json.loads(str)
    container=resp["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ri"].split("/in-cse/")[1]
    resp=resp["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"].split("[")[1].split("]")[0]
    resp=resp.split(',')
    # print(resp)

    query="INSERT INTO air(timestamp,pm25,pm10,temperature,humidity,co,nh2,nh3,aqi,aql,aqimp,datainterval,nodename,container_instance) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format('sdf',resp[1],resp[2],resp[3],resp[4],resp[5],resp[6],resp[7],resp[8],resp[9],resp[10],resp[11],resp[12],container)
    cur=connection.cursor()
    cur.execute(query)
    connection.commit()
    cur.close()

    return response