from django.test import TestCase
import requests , json
import datetime
# Create your tests here

data =  {"name": "javilon", "point": {"type": "Point", "coordinates": [-4.425794, 36.720364 ]}}
lap = { "mac": '87844841464', "date": str(datetime.datetime.now()), "data": 'fafaffsafafaf'}


data_json = json.dumps(data)
headers = {"Authorization": 'Token dc1fb76928fe80e32ae22f86b87200042e4e315a' }
try:
   r = requests.post(url='http://153.92.209.82:9000/api/lap/', json=lap,  headers=headers )
except requests.exceptions.HTTPError as error:
    print(error)   
print((r.json()))

