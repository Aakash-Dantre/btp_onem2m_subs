
#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import psycopg2
import xmltodict
import json

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))

        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        try:
            resp=json.loads(post_data.decode('utf-8'))
            container=resp["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["ri"].split("/in-cse/")[1]
            resp=resp["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"].split("[")[1].split("]")[0]
            resp=resp.split(',')
            logging.info(len(resp))
            if(len(resp)==2):#water
                query="INSERT INTO water2(level,nodename,container_instance) VALUES ('{}','{}','{}')".format(resp[0],resp[1],container)
                cur=con.cursor()
                cur.execute(query)
                con.commit()
                cur.close()
            elif(len(resp)==13):#air
                query="INSERT INTO air2(timestamp,pm25,pm10,temperature,humidity,co,nh2,nh3,aqi,aql,aqimp,datainterval,nodename,container_instance) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format('sdf',resp[1],resp[2],resp[3],resp[4],resp[5],resp[6],resp[7],resp[8],resp[9],resp[10],resp[11],resp[12],container)
                cur=con.cursor()
                cur.execute(query)
                con.commit()
                cur.close()
            else:#wind
                query="INSERT INTO wind2(timestamp,solarradiation,temperature,relativehumidity,winddirection,windspeed,gustspeed,dewpoint,batterydcvoltage,rain,pressure,nodename,container_instance) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format('dsf',resp[1],resp[2],resp[3],resp[4],resp[5],resp[6],resp[7],resp[8],resp[9],resp[10],resp[11],container)
                cur=con.cursor()
                cur.execute(query)
                con.commit()
                cur.close()
        except:
            print("subscription")

        # logging.info(vert)
        # logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
        #         str(self.path), str(self.headers), post_data.decode('utf-8'))
        
        # dataInXML=xmltodict.parse(post_data.decode('utf-8'))
        # print(dataInXML['m2m:sgn']['nev']['rep'])
        # db()
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    
    con = psycopg2.connect(
        host="localhost",
        database="subs",
        user="postgres",
        password="po6S.dance"
    )
    
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()


