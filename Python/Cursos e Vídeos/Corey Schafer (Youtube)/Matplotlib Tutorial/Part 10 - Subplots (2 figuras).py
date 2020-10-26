# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:34:24 2020

@author: pedro
"""
#############################
##### CONFIGURAÇÃO GERAL ####
#############################
globals().clear()
""" Mudar diretório """
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    print('\nLogado de casa')
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('\nLogado da salj-alems')
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados' / 'Cursos e Livros' / 'Corey Schafer - Youtube' / 'Matplotlib Tutorials' / 'Part 10'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

#############################
#############################
#############################


import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data.csv',
                       encoding = 'latin',
                       delimiter = ',',
                       decimal = ".")
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# Duas figuras:
fig1, ax1 = plt.subplots(nrows=1, ncols=1)
fig2, ax2 = plt.subplots(nrows=1, ncols=1)
    
ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()
ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

#fig1.savefig('fig1.png')
#fig2.savefig('fig2.png')