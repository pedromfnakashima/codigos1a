# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:28:20 2020

@author: pedro
"""

""" Muda o diretório """
import os
print(os.getcwd())
os.chdir('D:\Códigos, Dados, Documentação e Cheat Sheets\Cursos e Livros\Corey Schafer - Youtube\Zip Files')
print(os.getcwd())

##############################
###### EXEMPLO 01 ############
##############################
""" cria e adiciona
precisa abrir e fechar"""
import zipfile

my_zip = zipfile.ZipFile('file.zip', 'w')

my_zip.write('test.txt')
my_zip.write('thumbnail.png')

my_zip.close()

##############################
###### EXEMPLO 02 ############
##############################
""" cria e adiciona
com context manager
NÃO precisa fechar
"""
import zipfile

with zipfile.ZipFile('file.zip', 'w') as my_zip:
    my_zip.write('test.txt')
    my_zip.write('thumbnail.png')

##############################
###### EXEMPLO 03 ############
##############################
""" cria e adiciona
com o parâmetro compression, DE
FATO comprime os arquivos.
Sem o parâmetro, NÃO há compressão
"""
import zipfile

with zipfile.ZipFile('file.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('test.txt')
    my_zip.write('thumbnail.png')

##############################
###### EXEMPLO 04 ############
##############################
""" extrai arquivos de zip
parâmetro r ao invés de w
só pega os nomes
"""
import zipfile

with zipfile.ZipFile('file2.zip', 'r') as my_zip:
    print(my_zip.namelist())

##############################
###### EXEMPLO 05 ############
##############################
""" extrai arquivos de zip
parâmetro r ao invés de w
extrai tudo
"""
import zipfile

with zipfile.ZipFile('file2.zip', 'r') as my_zip:
    my_zip.extractall('arquivos')


##############################
###### EXEMPLO 06 ############
##############################
""" extrai arquivos de zip
parâmetro r ao invés de w
extrai um arquivo específico
"""
import zipfile

with zipfile.ZipFile('file2.zip', 'r') as my_zip:
    my_zip.extract('thumbnail2.png')

##############################
###### EXEMPLO 07 ############
##############################
""" cria um zip
com todos os arquivos de
um diretório
"""
import shutil

shutil.make_archive('outro', 'zip', 'arquivos')

##############################
###### EXEMPLO 08 ############
##############################
""" extrai

"""
import shutil

shutil.unpack_archive('outro.zip', 'outro')

##############################
###### EXEMPLO 09 ############
##############################
""" cria um gztar
com todo o diretório
"""
import shutil

shutil.make_archive('outro', 'gztar', 'arquivos')

##############################
###### EXEMPLO 10 ############
##############################
""" download de arquivo zip

"""
globals().clear()
import requests
import zipfile

r = requests.get('https://github.com/CoreyMSchafer/dotfiles/archive/master.zip')

with open('data.zip', 'wb') as f:
    f.write(r.content)

""" lista """
with zipfile.ZipFile('data.zip', 'r') as data_zip:
    print(data_zip.namelist())
""" extrai """
with zipfile.ZipFile('data.zip', 'r') as data_zip:
    data_zip.extractall('data')



