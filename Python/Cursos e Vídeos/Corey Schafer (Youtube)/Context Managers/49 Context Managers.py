# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 18:04:58 2020

@author: pedro
"""

# https://www.youtube.com/watch?v=-aKFBoZpiqA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=49

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
caminho_wd = caminho_base / 'codigos_versionados' / 'Python' / 'Cursos e Vídeos' / 'Corey Schafer (Youtube)' / 'Context Managers'
os.chdir(caminho_wd)

#############################################

globals().clear()

class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with Open_File('sample.txt','w') as f:
    f.write('Testing')

print(f.closed)

#############################################

globals().clear()

from contextlib  import contextmanager

#### Using contextlib ####

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

with open_file('sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(f.closed)

#############################################

globals().clear()

import os
from contextlib  import contextmanager

#### CD Example ####

cwd = os.getcwd()
os.chdir('Sample-Dir-One')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('Sample-Dir-Two')
print(os.listdir())
os.chdir(cwd)


#############################################
"""
Forma mais eficiente de rodar o bloco anterior


"""

globals().clear()

import os
from contextlib  import contextmanager

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('Sample-Dir-One'):
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())





