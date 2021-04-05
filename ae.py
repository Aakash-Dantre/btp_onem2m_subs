from functions import *
import random as r
import time
t1 = time.time()
s=1                                         ## CHANGES THE TYPE OF SERVER
if s==1:
	url="http://127.0.0.1:8080/~/in-cse/in-name"
	auth="admin:admin"
	# create_ae(url,"admin:admin","Air_Quality_Monitoring1")
	uri_air=url+"/Air_Quality_Monitoring1"
	# create_cnt(uri_air,"admin:admin","descriptor")
	# create_cnt(uri_air,"admin:admin","node1")
	# create_cnt(uri_air,"admin:admin","node2")
	uri_air1=uri_air+"/node1"
	uri_air2=uri_air+"/node2"

	# create_ae(url,"admin:admin","Water_Level_Monitoring1")
	uri_water=url+"/Water_Level_Monitoring1"
	# create_cnt(uri_water,"admin:admin","descriptor")
	# create_cnt(uri_water,"admin:admin","node1")
	# create_cnt(uri_water,"admin:admin","node2")
	uri_water1=uri_water+"/node1"
	uri_water2=uri_water+"/node2"

	# create_ae(url,"admin:admin","Wind_Monitoring1")
	uri_wind=url+"/Wind_Monitoring1"
	# create_cnt(uri_wind,"admin:admin","descriptor")
	# create_cnt(uri_wind,"admin:admin","node1")
	# create_cnt(uri_wind,"admin:admin","node2")
	uri_wind1=uri_wind+"/node1"
	uri_wind2=uri_wind+"/node2"

	# create_desc_cin(uri_air1,"admin:admin","")
	create_sub(uri_water1,"water/",auth)
	# create_sub(uri_water2,"water/",auth)
	# create_sub(uri_air1,"air/",auth)
	# create_sub(uri_air2,"air/",auth)
	# create_sub(uri_wind1,"wind/",auth)
	# create_sub(uri_wind2,"wind/",auth)

if s==2:
	url="http://127.0.0.1:8080/~/in-cse/in-name"
	auth="admin:admin"
	# create_ae(url,"admin:admin","Air_Quality_Monitoring2")
	uri_air=url+"/Air_Quality_Monitoring2"
	# create_cnt(uri_air,"admin:admin","descriptor")
	# create_cnt(uri_air,"admin:admin","node1")
	# create_cnt(uri_air,"admin:admin","node2")
	uri_air1=uri_air+"/node1"
	uri_air2=uri_air+"/node2"

	# create_ae(url,"admin:admin","Water_Level_Monitoring2")
	uri_water=url+"/Water_Level_Monitoring2"
	# create_cnt(uri_water,"admin:admin","descriptor")
	# create_cnt(uri_water,"admin:admin","node1")
	# create_cnt(uri_water,"admin:admin","node2")
	uri_water1=uri_water+"/node1"
	uri_water2=uri_water+"/node2"

	# create_ae(url,"admin:admin","Wind_Monitoring2")
	uri_wind=url+"/Wind_Monitoring2"
	# create_cnt(uri_wind,"admin:admin","descriptor")
	# create_cnt(uri_wind,"admin:admin","node1")
	# create_cnt(uri_wind,"admin:admin","node2")
	uri_wind1=uri_wind+"/node1"
	uri_wind2=uri_wind+"/node2"

	# create_desc_cin(uri_air1,"admin:admin","")
	# create_sub2(uri_water1,auth)
	# create_sub2(uri_water2,auth)
	# create_sub2(uri_air1,auth)
	# create_sub2(uri_air2,auth)
	# create_sub2(uri_wind1,auth)
	# create_sub2(uri_wind2,auth)

i=0
te=i
while(i):
	i-=1
	time.sleep(1)
	# water
	water_ci1="["+str(r.randint(0,3))+","+"node1"+"]"
	water_ci2="["+str(r.randint(0,3))+","+"node2"+"]"
	create_desc_cin(uri_water1,"admin:admin",water_ci1)
	create_desc_cin(uri_water2,"admin:admin",water_ci2)
	#air
	air_ci1="["+str(time.time())[:8]+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+","+"False,False,"+"node1"+"]"
	air_ci2="["+str(time.time())[:8]+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+","+"False,False,"+"node2"+"]"

	
	create_desc_cin(uri_air1,"admin:admin",air_ci1)
	create_desc_cin(uri_air2,"admin:admin",air_ci2)

	wind_ci1="["+str(time.time())[:8]+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+","+"False,"+"node1"+"]"
	wind_ci2="["+str(time.time())[:8]+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+str(round(r.uniform(10,50),3))+","+","+"False,"+"node2"+"]"

	create_desc_cin(uri_wind1,"admin:admin",wind_ci1)
	create_desc_cin(uri_wind2,"admin:admin",wind_ci2)


t2 = time.time()

print("FINAL TIME ELAPSED FOR "+str(te)+"interations is "+str(t2-t1))
