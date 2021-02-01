# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:07:39 2020

@author: pedro
"""
# https://www.youtube.com/watch?v=KlBPCzcQNU8&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=38

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
caminho_wd = caminho_base / 'codigos_versionados' / 'Python' / 'Cursos e Vídeos' / 'Corey Schafer (Youtube)'
os.chdir(caminho_wd)

##############################################

globals().clear()

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Executed Before', original_function.__name__)
        result = original_function(*args, **kwargs)
        print('Executed After', original_function.__name__, '\n')
        return result
    return wrapper_function


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
display_info('Travis', 30)

##############################################
"""
Vamos customizar o prefixo do decorador
colocando argumentos na função decorador.

Passos.
- Coloca mais uma função fora;
- Coloca mais um return

É como se colocasse uma nova camada ao
decorador existente

"""

globals().clear()

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__, '\n')
            return result
        return wrapper_function
    return decorator_function


# @decorator_function
@prefix_decorator('LOG: ')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
display_info('Travis', 30)













































