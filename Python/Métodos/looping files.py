# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:59:02 2020

@author: pedro-salj
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
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados' / 'cnae e ncm'
os.chdir(caminho_wd)
##########################################################################################################
##########################################################################################################
##########################################################################################################


import glob

for arq_nome in glob.glob('*.csv'):
    print(arq_nome)
    
    
    
            