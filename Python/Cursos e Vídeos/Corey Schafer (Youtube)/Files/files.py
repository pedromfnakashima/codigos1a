# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:44:46 2020

@author: pedro
"""
""" STRING
Tira brancos de cada lado:
"""
texto = '  um texto  '
print(texto)
print(texto.strip())
""" STRING
Pega uma parte da string:
"""
texto = 'Constituição'
print(texto)
print(texto[4:])
""" STRING
Preenche string numérica com 0:
"""
texto = '5'
print(texto)
print(texto.zfill(2))
print(texto.zfill(3))

""" Mudar diretório """
import os
print(os.getcwd())
os.chdir('D:\Códigos, Dados, Documentação e Cheat Sheets\Dados\Siconfi\RGF - Estados\Anexo 01 - Demonstrativo da Despesa Com Pessoal\DTP e Apuração do Cumprimento do Limite Legal')
print(os.getcwd())

""" Lista os arquivos """
for arquivo in os.listdir():
    print(arquivo)

""" tuplas: nomes + extensão """
for arquivo in os.listdir():
    print(os.path.splitext(arquivo))

""" tuplas: nomes + extensão """
for arquivo in os.listdir():
    arq_nome, arq_ext = os.path.splitext(arquivo)
    print(arq_nome)
    print(arq_ext)

""" pega ano e o trimestre """
for arquivo in os.listdir():
    arq_nome, arq_ext = os.path.splitext(arquivo)
    print(arq_nome.split('q'))

""" pega ano e o trimestre """
for arquivo in os.listdir():
    arq_nome, arq_ext = os.path.splitext(arquivo)
    ano, trimestre = arq_nome.split('q')
    print(ano)
    print(trimestre)

""" Muda o nome do arquivo
os.rename(nomevelho, nomenovo)
"""
