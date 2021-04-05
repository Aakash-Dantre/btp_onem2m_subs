
import requests
import time
t1=time.time()
data = {
   "m2m:sgn" : {
      "m2m:nev" : {
         "m2m:rep" : {
            "m2m:cin" : { 
               "rn" : "cin_527453661",
               "ty" : 4,
               "ri" : "/in-cse/cin-527453661",
               "pi" : "/in-cse/cnt-649712568",
               "ct" : "20210402T060639",
               "lt" : "20210402T060639",
               "lbl" : [ "" ],
               "st" : 0,
               "cnf" : "application/json",
               "cs" : 85,
               "con" : "[1617323735.637,21.089,40.761,27.524,17.653,12.386,39.677,45.794,21.625,,False,node2]"
            }
         },
         "m2m:rss" : 1
      },
      "m2m:sud" : False,
      "m2m:sur" : "/in-cse/sub-305157817" 
   }
}
url='http://127.0.0.1:8000/water/'
i=1
it=i
while(i):
   i-=1
   requests.post(url,json=data)

t2=time.time()

print("FINAL TIME ELAPSED FOR "+str(it)+" interations is "+str(t2-t1))

