# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 08:52:31 2020

@author: pedro-salj
https://www.dataquest.io/blog/python-api-tutorial/
"""

import requests

response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")

print(response.status_code) # 404

import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())


parameters = {
    "lat": 40.71,
    "lon": -74
}


response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

jprint(response.json())

pass_times = response.json()['response']

jprint(pass_times)

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)

from datetime import datetime

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)




###################################################################################
############################## APLICAÇÕES #########################################
###################################################################################
# https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63,66/p/all/c315/all/d/v63%202,v66%204

import pandas as pd

import requests

response = requests.get("http://api.sidra.ibge.gov.br/values")
print(response.status_code) # 400

response = requests.get("https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63,66/p/all/c315/all/d/v63%202,v66%204")
print(response.status_code) # 400

print(response.json())


import requests
import pandas as pd
import io
url = "https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63,66/p/all/c315/all/d/v63%202,v66%204"

import requests
import pandas as pd

r = requests.get(url)

j = r.json()

df = pd.DataFrame([[d['v'] for d in x['c']] for x in j['rows']],
                  columns=[d['label'] for d in j['cols']])


df = pd.DataFrame.from_dict(j)

################################################
import requests
url = "https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63,66/p/all/c315/all/d/v63%202,v66%204"
r = requests.get(url)
j = r.json()
df = pd.DataFrame.from_dict(j)
########################


import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())


######################################## http://api.sidra.ibge.gov.br/home/ajuda





parameters = {
    "t": "7060",
    "n1": "all",
    "v": ["63","66"],
    "p": "all",
    "c315": "all",
    "d": ["v63%202","v66%204"]
}

# https://apisidra.ibge.gov.br/values
t/7060/
n1/all/
v/63,66/
p/all/
c315/all/
d/v63%202,v66%204

parameters = {
    "t": "7060",
    "n1": "all",
    "v": "63,66",
    "p": "all",
    "c315": "all",
    "d": "v63%202,v66%204"
}

response = requests.get("https://apisidra.ibge.gov.br/values", params=parameters)

print(response.status_code) # 400

##############

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)

###############
# https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63,66/p/all/c315/all/d/v63%202,v66%204


response = requests.get("https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63,66/p/all/c315/all/d/v63%202,v66%204")
print(response.status_code) # 400



url = 'https://apisidra.ibge.gov.br/values'
parameters = {
    "t": "7060",
    "n1": "all",
    "v": "63,66",
    "p": "all",
    "c315": "all",
    "d": "v63%202,v66%204"
}

r = requests.get(url)
r = requests.get(url, params=parameters)


Código e nome (parâmetros /t/1612/n1/1/v/allxp/p/last/c81/2702/h/n)















