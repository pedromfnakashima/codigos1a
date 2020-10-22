# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:41:29 2020

@author: pedro
Usar interpretador Python 3.9
"""
import sys
print(dir(sys))
print(sys.executable)

""" Mudar diretório """
import os
print(os.getcwd())
os.chdir('D:\Códigos, Dados, Documentação e Cheat Sheets\Dados\Siconfi\RGF - Estados\Anexo 01 - Demonstrativo da Despesa Com Pessoal\DTP e Apuração do Cumprimento do Limite Legal')
print(os.getcwd())

for arquivo in os.listdir():
    print(arquivo)


teste = 'Dr. Estranho'

print(teste.str.removeprefix('Dr. '))

print('TestHook'.removeprefix('Test'))



