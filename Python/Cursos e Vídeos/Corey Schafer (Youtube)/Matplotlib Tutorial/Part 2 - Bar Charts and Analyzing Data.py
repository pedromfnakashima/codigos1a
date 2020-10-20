# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:20:52 2020

@author: pedro
"""
globals().clear()

from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    print('Logado de casa')
    caminho = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('Logado da salj-alems')
    caminho = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv(caminho / 'Cursos e Livros' / 'Corey Schafer - Youtube' / 'Matplotlib Tutorials' / 'Part 2' /'data.csv',
                       encoding = 'latin',
                       delimiter = ',',
                       decimal = ".")

ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()

plt.show()