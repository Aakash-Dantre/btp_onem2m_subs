from functions import *
import random as r
import time
import requests
from time import sleep
# from grequests import async
import grequests
import datetime
t1 = time.time()
s=1                                         ## CHANGES THE TYPE OF SERVER
it =0
ts=time.time()


url="http://127.0.0.1:8080/~/in-cse/in-name/"
auth="admin:admin"
v = []
for i in range(1):
    st = "newverticalagainagain"+str(i)
    v.append(st)
con=[]
for i in range(1):
    uri_air=url+v[i]
    nodeslist=[]
    create_ae(url,"admin:admin",v[i])
    create_cnt(uri_air,"admin:admin","node1")
    create_cnt(uri_air,"admin:admin","node2")
    create_cnt(uri_air,"admin:admin","node3")
    create_cnt(uri_air,"admin:admin","node4")
    create_cnt(uri_air,"admin:admin","node5")

    nodeslist.append(uri_air+"/node1")
    nodeslist.append(uri_air+"/node2")
    nodeslist.append(uri_air+"/node3")
    nodeslist.append(uri_air+"/node4")
    nodeslist.append(uri_air+"/node5")
    con.append(nodeslist)



def async_create_desc_cin(uri_desc_cnt,authentication, node_description, desc_cin_labels="", data_format="json"):

    headers = {
        'X-M2M-Origin': authentication,
        'Content-type': 'application/{};ty=4'.format(data_format)}

    body = {
        "m2m:cin": {
            "cnf":"application/json",
            "con":node_description,
            "lbl":desc_cin_labels,
            "test":"failed",
        }
    }

    # action_item = grequests.post(uri_desc_cnt, json=body, headers=headers,hooks = {'response' : do_something})
    action_item = grequests.post(uri_desc_cnt, json=body, headers=headers)

    async_list.append(action_item)


for b in range(20):
    t1=time.time()
    async_list = []
    i=200
    p=10
    k=i/p
    iterations=i
    for lol in range(p):
        while(k):
            # it+=1
            k-=1
            t = str(datetime.datetime.now()).split('.')[0]
            air_ci1="["+t+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+"False,False,"+"node1"+"]"
            n_val = r.randint(0,4)
            v_val = r.randint(0,b)

            async_create_desc_cin(con[0][n_val],"admin:admin",air_ci1)

            # async_create_desc_cin(con[v_val][n_val],"admin:admin",air_ci1)


        # print(async_list)
        res=(grequests.map(async_list))
    # print(res)
    t2 = time.time()
    print("FINAL TIME ELAPSED FOR "+str(iterations*b)+"-"+str(iterations*(b+1))+" request is "+str(t2-t1))
    sleep(10)
    # print("FINAL TIME ELAPSED FOR "+str(iterations)+" requests at "+str((b+1))+" verticals is "+str(t2-t1))
