# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:36:53 2020

@author: pedro
"""

# https://www.youtube.com/watch?v=FsAPt_9Bf3U&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=37

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
caminho_wd = caminho_base / 'codigos_versionados' / 'Python' / 'Cursos e Vídeos' / 'Corey Schafer (Youtube)' / 'Decorators'
os.chdir(caminho_wd)



##############################################

globals().clear()

def outer_function():
    message = 'Hi'
    
    def inner_function():
        print(message)
    return inner_function()

outer_function()

##############################################
# closure

globals().clear()

def outer_function():
    message = 'Hi'
    
    def inner_function():
        print(message)
    return inner_function

my_func = outer_function()
my_func()

##############################################

globals().clear()

def outer_function(msg):
    message = msg
    
    def inner_function():
        print(message)
    return inner_function

hi_func = outer_function('Hi')
hi_func()

bye_func = outer_function('Bye')
bye_func()

##############################################

globals().clear()

def outer_function(msg):
    
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function('Hi')
hi_func()

bye_func = outer_function('Bye')
bye_func()

##############################################
"""
DECORATOR é:
-Uma função que toma outra função como argumento.
-Adiciona algum tipo de funcionalidade e
-Retorna uma outra função
-Sem alterar o código da função original que
foi tomada como argumento

Mudança de nomes
outer_function -> decorator_function
inner_function -> wrapper_function
"""

globals().clear()

# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function

# def decorator_function(message):
#     def wrapper_function():
#         print(message)
#     return wrapper_function

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display(): # <- função original
    print('display function ran')

decorated_display = decorator_function(display)

decorated_display()

##############################################

"""
Adicionando funcionalidades à função
de entrada (display)
"""
globals().clear()

def decorator_function(original_function):
    # funcionalidade adicionada pela função decorator_function
    print('wrapper executed this before {}\n'.format(original_function.__name__))
    def wrapper_function():
        return original_function()
    return wrapper_function

def display(): # <- função original
    print('display function ran')

decorated_display = decorator_function(display)

decorated_display()


##############################################

globals().clear()

def decorator_function(original_function):
    
    # funcionalidade adicionada pela função decorator_function
    print('wrapper executed this before {}\n'.format(original_function.__name__))
    
    def wrapper_function():
        return original_function()
    
    return wrapper_function

@decorator_function
def display(): # <- função original
    print('display function ran')


# display = decorator_function(display)
# é a mesma coisa que:
display()

##############################################
"""
11:30
display_info
Se a função orignal tem argumentos,
é preciso adicionar argumentos no decorador
"""

globals().clear()

def decorator_function(original_function):
    
    # funcionalidade adicionada pela função decorator_function
    print('wrapper executed this before {}\n'.format(original_function.__name__))
    
    def wrapper_function():
        return original_function()
    
    return wrapper_function

@decorator_function
def display(): # <- função original
    print('display function ran')

def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John',25)


##############################################
"""
11:30
display_info
Se a função orignal tem argumentos,
é preciso adicionar argumentos no decorador.
Adiciona:
"""

globals().clear()

def decorator_function(original_function):
    
    # funcionalidade adicionada pela função decorator_function
    print('wrapper executed this before {}\n'.format(original_function.__name__))
    
    def wrapper_function(*args, **kwargs):
        return original_function(*args, **kwargs)
    
    return wrapper_function

@decorator_function
def display(): # <- função original
    print('display function ran')

@decorator_function
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John',25)


##############################################
"""
Usando CLASSES como decoradores ao invés de
FUNÇÕES.

"""
globals().clear()

class decorator_class():
    
    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print('call method executed this before {}\n'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)
    
@decorator_class
def display(): # <- função original
    print('display function ran')

@decorator_class
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John',25)


##############################################
"""
Exemplos práticos com decoradores.
logger
"""

globals().clear()

# Practical Examples

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    
    return wrapper


def my_timer(orig_func):
    import time
    
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    
    return wrapper

@my_logger
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John',25)

display_info('Hank',30)


##############################################
"""
Exemplos práticos com decoradores.
timer
"""
globals().clear()

# Practical Examples

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    
    return wrapper


def my_timer(orig_func):
    import time
    
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time

@my_timer
def display_info(name,age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John',25)

display_info('Hank',30)


##############################################
"""
Alterações necessárias para ser possível
encadear decoradores.

Segundo decorador + função original:
display_info = my_timer(display_info)

Primeiro decorador + Segundo decorador + Função original:
display_info = my_logger(my_timer(display_info))

- my_timer retorna função wrapper
- uma vez em my_logger, orig_func.__name__ = wrapper

CÓDIGO NÃO FUNCIONANDO COMO O ESPERADO.

"""

globals().clear()

# Practical Examples

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time
    
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time

# @my_logger
# @my_timer
def display_info(name,age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info = my_timer(display_info)
print(display_info.__name__) # wrapper

# display_info('John',25)
# display_info('Hank',30)

"""
Alterações necessárias para ser possível
encadear decoradores.

Segundo decorador + função original:
display_info = my_timer(display_info)

Primeiro decorador + Segundo decorador + Função original:
display_info = my_logger(my_timer(display_info))

- my_timer retorna função wrapper
- uma vez em my_logger, orig_func.__name__ = wrapper

Solução.
PRESERVAR INFORMAÇÕES DA FUNÇÃO ORIGINAL:
- from functools import wraps
- @wraps(orig_func) em cima das funções wrapper, onde orig_func é a função original passada como input, argumento

CÓDIGO FUNCIONANDO COMO O ESPERADO.

"""

globals().clear()

from functools import wraps

# Practical Examples

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time

# @my_logger
# @my_timer
def display_info(name,age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info = my_timer(display_info)
print(display_info.__name__) # display_info

# display_info('John',25)
# display_info('Hank',30)

"""
Alterações necessárias para ser possível
encadear decoradores.

Segundo decorador + função original:
display_info = my_timer(display_info)

Primeiro decorador + Segundo decorador + Função original:
display_info = my_logger(my_timer(display_info))

- my_timer retorna função wrapper
- uma vez em my_logger, orig_func.__name__ = wrapper

Solução.
PRESERVAR INFORMAÇÕES DA FUNÇÃO ORIGINAL:
- from functools import wraps
- @wraps(orig_func) em cima das funções wrapper, onde orig_func é a função original passada como input, argumento

CÓDIGO FUNCIONANDO COMO O ESPERADO.

"""

globals().clear()

from functools import wraps

# Practical Examples

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    
    @wraps(orig_func) # <=== FAZ PRESERVAR INFORMAÇÕES (NOME) DA FUNÇÃO ORIGINAL orig_func
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time
    
    @wraps(orig_func) # <=== FAZ PRESERVAR INFORMAÇÕES (NOME) DA FUNÇÃO ORIGINAL orig_func
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time

@my_logger
@my_timer
def display_info(name,age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name,age))

# display_info = my_timer(display_info)
# print(display_info.__name__) # display_info

display_info('Tom',9)
display_info('Jerry',8)





















