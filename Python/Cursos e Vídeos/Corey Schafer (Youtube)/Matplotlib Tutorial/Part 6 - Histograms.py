# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:50:21 2020

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


import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv(caminho / 'Cursos e Livros' / 'Corey Schafer - Youtube' / 'Matplotlib Tutorials' / 'Part 6' /'data.csv',
                       encoding = 'latin',
                       delimiter = ',',
                       decimal = ".")

ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black', log=True)

median_age = 29
color = '#fc4f30'

plt.axvline(median_age, color=color, label='Age Median', linewidth=2)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()