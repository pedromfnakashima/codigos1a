# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:34:16 2020

@author: pedro

Documentação (String handling):
https://pandas.pydata.org/pandas-docs/stable/reference/index.html

"""
###########################
# How do I use string methods in pandas?
# https://www.youtube.com/watch?v=bofaC0IckHo
###########################
globals().clear()
import pandas as pd
orders = pd.read_table('http://bit.ly/chiporders')

#############################
######## EXEMPLO 01 #########
#############################
"""  """

# Só funciona p/ python. P/ pandas precisa usar str.método_string
print('hello'.upper())

print(orders.item_name.head())

print(orders.item_name.str.upper().head())

print(orders.item_name.str.contains('Chicken'))
# série de booleanos

filtro = orders.item_name.str.contains('Chicken')

print(orders[filtro])
print(orders[filtro].item_name)

#############################
######## EXEMPLO 02 #########
#############################
"""
Retirar os colchetes da coluna
choice_description
"""
print(orders.choice_description.str.replace('[',''))

print(orders.choice_description.str.replace('[','').str.replace(']',''))


#############################
######## EXEMPLO 03 #########
#############################
""" usando regex
precisa escapar com \
"""
print(orders.choice_description.str.replace('[\[\]]',''))

