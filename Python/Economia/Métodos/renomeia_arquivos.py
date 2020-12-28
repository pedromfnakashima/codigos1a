# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:18:02 2020

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
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos_2007-2019'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

import glob
import os

for arq_num, arq_nome in enumerate(glob.glob('*.txt')):
    ano = arq_nome[-8:-4]
    mes = arq_nome[-10:-8]
    novo_nome = 'CAGEDMOV' + ano + mes + '.txt'
    print(novo_nome)
    os.rename(arq_nome, novo_nome)
    


# CAGEDMOV202008.txt
os.rename(nomevelho, nomenovo)