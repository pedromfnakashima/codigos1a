# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:34:24 2020

@author: pedro
"""
globals().clear()

from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    caminho = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

pasta = caminho_base / 'Dados' / 'Cursos e Livros' / 'Corey Schafer - Youtube' / 'Matplotlib Tutorials' / 'Part 10'
data = pd.read_csv(pasta / 'data.csv',
                       encoding = 'latin',
                       delimiter = ',',
                       decimal = ".")
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# Uma figura:
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
    
ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

#fig.savefig('fig.png')
