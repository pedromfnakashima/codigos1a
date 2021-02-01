# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 10:44:39 2020

@author: pedro
"""

# https://www.youtube.com/watch?v=jxmzY9soFXg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=53

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
caminho_wd = caminho_base / 'codigos_versionados' / 'Python' / 'Cursos e Vídeos' / 'Corey Schafer (Youtube)' / 'Logging'
os.chdir(caminho_wd)

##########################################################################################################
##########################################################################################################
##########################################################################################################


import employee

# Cria o logger
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Cria e configura o FILE HANDLER (imprime no .log)
formatter_file_handler = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter_file_handler)

# Cria e configura o STREAM HANDLER (imprime no console)
formatter_stream_handler = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter_stream_handler)

# Adiciona file_handler e stream_handler ao logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result


num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
























