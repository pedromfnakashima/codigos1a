# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 15:54:39 2020

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
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'codigos_versionados' / 'Python' / 'testes' / 'Módulo'
os.chdir(caminho_wd)

#############################################

from pasta1 import mod_pasta1
from pasta2 import mod_pasta2

from pasta1.pastaa import mod_pastaa
from pasta2.pastab import mod_pastab

mod_pastaa.olá()

mod_pastab.olá()

