import http.client
import pandas as pd
import json


conn=http.client.HTTPSConnection("api.openweathermap.org")
payload=''
headers={}
conn.request("GET","/data/2.5/weather?lat=35&lon=139&appid=38c4ea9a0b79a44ba94381bf9ffe8549",payload,headers)
res=conn.getresponse()
data=res.read()
data = json.loads(data)
print(data)


import csv
csv_columns = ['coord','weather','base','main','visibility','wind','rain','clouds','dt','sys','timezone','id','name','cod']
csv_file = "F:\weather.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        #for row in data:
        writer.writerow(data)
except IOError:
    print("I/O error")
