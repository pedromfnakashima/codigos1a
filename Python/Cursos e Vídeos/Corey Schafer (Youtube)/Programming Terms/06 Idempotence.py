# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:26:49 2020

@author: pedro
"""

# Função NÃO idempotente

def add_ten(num):
    return num + 10

print(add_ten(10))

print(add_ten(add_ten(10)))

# Função idempotente

print(abs(-10))

print(abs(abs(-10)))


# 

a = 10

"""
IDEMPOTENTES (MÉTODOS HTTP)

GET: sim
PUT: sim
POST: não
DELETE: sim
"""










