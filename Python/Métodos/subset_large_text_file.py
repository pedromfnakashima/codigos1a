# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 08:32:04 2020

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
    print('\nLogado de casa')
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('\nLogado da salj-alems')
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos'# / 'temp1'
#caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos_2002-2009'# / 'temp1'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

#############################
#############################

linhas = []
num_linhas = 1000
with open('CAGEDMOV201206.txt', 'r') as rf:
    for linha in range(num_linhas):
        linhas.append(rf.readline())
with open('CAGEDMOV201206_amostra.txt', 'a') as wf:
    for linha in linhas:
        
        wf.write(linha)
        











with open('CAGEDMOV200701.txt', 'r') as rf:
    num_linhas = 1
    for linha in range(num_linhas):
        linhas.append(rf.readline())
        #linha = rf.readline()
    
    
    with open('CAGEDMOV200701_amostra.txt', 'a') as wf:
        for linha in range(num_linhas):
            
            linha = rf.readline()
            
            wf.write(linha)





with open("test.txt", 'r') as myfile:
    N = 3
    head = [next(myfile) for x in range(N)]

print(head)
print(head[0])
print(head[1])


with open('CAGEDMOV200701.txt', 'r') as rf:
    with open('CAGEDMOV200701_amostra.txt', 'w') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)







