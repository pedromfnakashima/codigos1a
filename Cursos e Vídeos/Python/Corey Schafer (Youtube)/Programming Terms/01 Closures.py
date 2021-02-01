# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 11:40:17 2020

@author: pedro
"""

def outer_func():
    message = 'Hi'
    
    def inner_func():
        print(message)
        
    return inner_func()

outer_func()

# -------------------------

def outer_func():
    message = 'Hi'
    
    def inner_func():
        print(message)
        
    return inner_func

my_func = outer_func()

print(my_func)
print(my_func.__name__)

my_func()

# -------------------------

def outer_func(msg):
    message = msg
    
    def inner_func():
        print(message)
        
    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()

# -------------------------

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
caminho_wd = caminho_base / 'codigos_versionados' / 'Python' / 'Cursos e Vídeos' / 'Corey Schafer (Youtube)' / 'Programming Terms'  # pasta onde tem os scripts (para importar as funções)
os.chdir(caminho_wd)

# -------------------------


import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__,args))
        print(func(*args))
    return log_func

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,3)
add_logger(4,5)

sub_logger(10,5)
sub_logger(20,10)

















