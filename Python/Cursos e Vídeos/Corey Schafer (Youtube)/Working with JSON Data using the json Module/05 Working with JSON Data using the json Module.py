# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:53:28 2020

@author: pedro
"""

# https://www.youtube.com/watch?v=9N6a-VLBa2I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=47

#############################
##### CONFIGURAÇÃO GERAL ####
#############################
globals().clear()
""" Mudar diretório """
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'codigos_versionados' / 'Python' / 'Cursos e Vídeos' / 'Corey Schafer (Youtube)' / 'Working with JSON Data using the json Module'
os.chdir(caminho_wd)

#############################################

import json

people_string_json = '''
{
  "people": [
    {
      "name":"John Smith",
      "phone":"615-555-7164",
      "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
      "has_license": false
    },
    {
      "name":"Jane Doe",
      "phone":"560-555-5153",
      "emails": null,
      "has_license": true
    }
  ]
}
'''
# CONVERTE (json.loads): JSON string OBJECT ==>> PYTHON dic
data_dic = json.loads(people_string_json)

"""
Tabela de conversão
https://docs.python.org/3/library/json.html
Python

PYTHON --- JSON
dict --- object
list, tuple --- array
str --- string
int, float, int- & float-derived Enums --- number
True --- true
False --- false
None --- null
"""

print(type(data_dic)) # <class 'dict'>

print(data_dic)

print(data_dic['people'])

print(type(data_dic['people'])) # <class 'list'>

for person in data_dic['people']:
    print(person)

for person in data_dic['people']:
    print(person['name'])

# Removendo o telefone de cada pessoa:
for person in data_dic['people']:
    del person['phone']

# CONVERTE (json.dumps): PYTHON dic ==>> STRING JSON
new_string_json = json.dumps(data_dic, indent=2, sort_keys=True)

print(new_string_json)

#############################################

globals().clear()

import json

# Lendo formato .json
with open('states.json') as f:
  data_dic = json.load(f)

# Deletando area_codes de cada estado
for state in data_dic['states']:
  del state['area_codes']

# CONVERTE (json.dumps): PYTHON dic ==>> em ARQUIVO .json
with open('new_states.json', 'w') as f:
  json.dump(data_dic, f, indent=2)


#############################################

'''
ATENÇÃO!

O CÓDIGO ABAIXO NÃO MAIS FUNCIONA POIS A API DO
YAHOO FOI DESCONTINUADA!

'''
# globals().clear()

# import json
# from urllib.request import urlopen

# with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
#     source = response.read()

# data = json.loads(source)

# # print(json.dumps(data, indent=2))

# usd_rates = dict()

# for item in data['list']['resources']:
#     name = item['resource']['fields']['name']
#     price = item['resource']['fields']['price']
#     usd_rates[name] = price

# print(50 * float(usd_rates['USD/INR']))









#############################################










#############################################








