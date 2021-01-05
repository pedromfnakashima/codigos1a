# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 14:36:12 2020

@author: pedro
"""

globals().clear()
import numpy as np

# AULA 06

""" Lista python """
lista = [1,2,3]
print(lista + 1) # dá erro

""" Array numpy """
array = np.array(lista)
print(array + 1) # não dá erro

mylist = [[1,2,3], [4,5,6], [7,8,9]]

mymatrix = np.array(mylist)
print(mymatrix)

print(mymatrix.shape)

mynewmatrix = np.array(mylist)

""" Array de 10 elementos """
print(np.arange(0,10))

print(np.arange(0,10, 2))

print(np.arange(0,11, 2))

""" Array de 5 zeros
float"""
print(np.zeros(5))

print(type(0.))
print(type(0.0))
print(type(5))

print(np.zeros((3,3)))
print(np.ones((3,3)))

print(np.ones((3,3)) + 4)
print(np.ones(4) * 1000)

""" Ocorre diferente com
lista python """
print([1,1,1,1] * 5)

""" MMC e MDC """

print(np.gcd.reduce([12, 20]))
print(np.lcm.reduce([12, 20]))
print(np.lcm.reduce([3, 5]))

print(np.gcd.reduce([15, 25, 35]))
print(np.lcm.reduce([40, 12, 20]))

""" np.linspace
3 números igualmente espaçados
entre 0 e 10"""
print(np.linspace(0,10,3))
print(len(np.linspace(0,10,3)))

""" Identidade 3x3 """
print(np.eye(3))

""" Número aleatório entre 0 e 1
Distribuição uniforme"""
print(np.random.rand(1))
print(np.random.rand(4))
print(np.random.rand(3,3))

""" Número aleatório entre 0 e 1
Distribuição normal-padrão"""
print(np.random.randn(1))
print(np.random.randn(4))
print(np.random.randn(3,3))

""" Número aleatório entre 0 e 1
Distribuição normal
loc: média
scale: desvio-padrão"""
print(np.random.normal(loc=5, scale=3))
print(np.random.normal(loc=5, scale=3, size=3))
print(np.random.normal(loc=5, scale=3, size=(3,3)))

""" Número aleatório inteiro
low: inclusivo.
high: exclusivo
"""
print(np.random.randint(low=1, high=100, size=1))
print(np.random.randint(low=1, high=100, size=(3,3)))

""" seed """
np.random.seed(42)
print(np.random.rand(4))

""" reshape """
arr = np.arange(25)
print(arr)

ranarr = np.random.randint(0,50,10)
print(ranarr)

print(arr.shape)

print(arr.reshape(5,5))

""" maior e menor elemento """
print(ranarr)
print(ranarr.max())
print(ranarr.min())

""" posição do maior e do
menor elemento """
print(ranarr)
print(ranarr.argmax())
print(ranarr.argmin())

""" dtype """
print(ranarr.dtype)

""" filtragem, seleção """
arr = np.arange(0,11)
print(arr)

print(arr[8])
print(arr[1:5])
print(arr[:5])
print(arr[5:])

"""  """
print(arr + 100)
print(arr /2)
print(arr ** 2)

""" slicing """
print(arr)
slice_of_arr = arr[0:6]
print(slice_of_arr)

slice_of_arr[:] = 99
print(slice_of_arr)

print(arr) # continua apontando para o array original

arr_copy = arr.copy() # copia
arr_copy[:] = 10000

print(arr_copy)
print(arr)

""" indexing on 2d array """

arr_2d = np.array([[5,10,15], [20,25,30], [35,40, 45]])
print(arr_2d.shape)
print(arr_2d)


""" Segunda linha """
print(arr_2d[1])

"""  """
print(arr_2d[1][1])
print(arr_2d[1,1])

""" primeiras duas linhas
até, mas não inclusa"""
print(arr_2d[:2])

"""  """
print(arr_2d[:2,1:])

""" Seleção condicional """

arr = np.arange(0,10)
print(arr)

print(arr > 4)

bool_arr = arr > 4
print(bool_arr)

print(arr[bool_arr])

print(arr[arr > 4])
print(arr[arr < 2])
print(arr[arr <= 6])

"""  """
print(arr)
print((arr + 2)/100)
print(arr + arr)

print(1/arr) # não dá erro, só warning

print(arr/arr) # não dá erro, só warning

print(np.sqrt(arr))

print(np.log(arr))

print(np.sin(arr))

""" Soma, Max, Min, Mean """
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())

""" Soma das colunas e das linhas """
arr_2d = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(arr_2d.shape)
print(arr_2d)

""" Soma das colunas,
ao longo das linhas (axis=0) """
print(arr_2d.sum(axis=0))

""" Soma das linhas,
ao longo das colunas (axis=1) """
print(arr_2d.sum(axis=1))

"""  """
