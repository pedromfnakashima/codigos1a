# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:00:25 2020

@author: pedro
"""
##################
### exemplo 01 ###
##################
""" count """

globals().clear()
import itertools

contador = itertools.count()

print(next(contador))
print(next(contador))
print(next(contador))

##################
### exemplo 02 ###
##################
""" count """
globals().clear()
import itertools

contador = itertools.count()

dados = [100, 200, 300, 400]

dados_diarios = list(zip(itertools.count(), dados))

print(dados_diarios)

""" Função zip(): ver vídeo
do 10 tips, do Corey Schafer.
Essa função funciona com dados
de qualquer tamanho."""

##################
### exemplo 03 ###
##################
""" count """
globals().clear()
import itertools

contador = itertools.count(start=5, step=5)

print(next(contador))
print(next(contador))
print(next(contador))

##################
### exemplo 04 ###
##################
""" count """
globals().clear()
import itertools

contador = itertools.count()

dados = [100, 200, 300, 400]

dados_diarios = list(zip(range(10), dados))

print(dados_diarios)

##################
### exemplo 05 ###
##################
""" zip_longest """
globals().clear()
import itertools

contador = itertools.count()

dados = [100, 200, 300, 400]

dados_diarios = list(itertools.zip_longest(range(10), dados))

print(dados_diarios)

##################
### exemplo 06 ###
##################
""" cycle """
globals().clear()
import itertools

contador = itertools.cycle([1, 2, 3])

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

##################
### exemplo 07 ###
##################
""" cycle """
globals().clear()
import itertools

contador = itertools.cycle(('Ligado', 'Desligado'))

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

##################
### exemplo 08 ###
##################
""" repeat """
globals().clear()
import itertools

contador = itertools.repeat(2)

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

##################
### exemplo 09 ###
##################
""" repeat """
globals().clear()
import itertools

contador = itertools.repeat(2, times=3)

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

##################
### exemplo 10 ###
##################
""" repeat """
globals().clear()
import itertools

contador = itertools.repeat(2, times=3)
quadrados = map(pow, range(10), itertools.repeat(2))

print(list(quadrados))

##################
### exemplo 11 ###
##################
""" repeat, starmap """
globals().clear()
import itertools

contador = itertools.repeat(2, times=3)
quadrados = itertools.starmap(pow, [(0,2), (1,2), (2,2)])

print(list(quadrados))

##################
### exemplo 12 ###
##################
""" combinations
Combinações
(ordem não importa) """
globals().clear()
import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = itertools.combinations(letters, 2)

for item in result:
    print(item)

##################
### exemplo 13 ###
##################
""" permutations
Permutações
(ordem importa) """
globals().clear()
import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = itertools.permutations(letters, 2)

for item in result:
    print(item)

##################
### exemplo 14 ###
##################
""" product
Produto cartesiano """
globals().clear()
import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = itertools.product(numbers, repeat=4)

for item in result:
    print(item)

##################
### exemplo 15 ###
##################
""" combinations
Todas as Combinações
Quebrando password
"""
globals().clear()
import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = itertools.combinations_with_replacement(numbers, 4)

for item in result:
    print(item)

##################
### exemplo 16 ###
##################
""" chain """
globals().clear()
import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

combined = itertools.chain(letters, numbers, names)

for item in combined:
    print(item)

##################
### exemplo 17 ###
##################
""" islice """
globals().clear()
import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = itertools.islice(range(10), 5)

for item in result:
    print(item)

##################
### exemplo 18 ###
##################
""" islice """
globals().clear()
import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = itertools.islice(range(10), 1, 5)

for item in result:
    print(item)

##################
### exemplo 19 ###
##################
""" islice """
globals().clear()
import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = itertools.islice(range(10), 1, 5, 2)

for item in result:
    print(item)

##################
### exemplo 20 ###
##################
""" islice """
globals().clear()

from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    print('Logado de casa')
    caminho = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('Logado da salj-alems')
    caminho = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

import itertools

with open(caminho / 'codigos_versionados' / 'Python' / 'Cursos e Vídeos' / 'Corey Schafer (Youtube)' / 'Itertools module' / 'test.log') as f:
    header = itertools.islice(f, 3)
    
    for line in header:
        print(line, end='')

##################
### exemplo 21 ###
##################
""" compress
Parecido com função filter """
globals().clear()
import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]

result = itertools.compress(letters, selectors)

for item in result:
    print(item)

""" comparação com função filter """

globals().clear()
import itertools

numbers = [0, 1, 2, 3]

def lt_2(n):
    if n < 2:
        return True
    return False

result = filter(lt_2, numbers)

for item in result:
    print(item)

##################
### exemplo 22 ###
##################
""" filterfalse """
globals().clear()
import itertools

numbers = [0, 1, 2, 3]

def lt_2(n):
    if n < 2:
        return True
    return False

result = itertools.filterfalse(lt_2, numbers)

for item in result:
    print(item)

##################
### exemplo 23 ###
##################
""" dropwhile """
globals().clear()
import itertools

numbers = [0, 1, 2, 3, 2, 1, 0]

def lt_2(n):
    if n < 2:
        return True
    return False

result = itertools.dropwhile(lt_2, numbers)

for item in result:
    print(item)

##################
### exemplo 24 ###
##################
""" takewhile """
globals().clear()
import itertools

numbers = [0, 1, 2, 3, 2, 1, 0]

def lt_2(n):
    if n < 2:
        return True
    return False

result = itertools.takewhile(lt_2, numbers)

for item in result:
    print(item)

##################
### exemplo 25 ###
##################
""" accumulate """
globals().clear()
import itertools

numbers = [0, 1, 2, 3, 2, 1, 0]

result = itertools.accumulate(numbers)

for item in result:
    print(item)

##################
### exemplo 26 ###
##################
""" accumulate """
globals().clear()
import itertools
import operator

numbers = [1, 2, 3, 2, 1, 0]

result = itertools.accumulate(numbers, operator.mul)

for item in result:
    print(item)

##################
### exemplo 27 ###
##################
""" groupby
agrupar pessoas pelo estado
"""
globals().clear()
import itertools

def get_state(person):
    return person['state']

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]


""" Imprime pessoas de cada
estado """
person_group = itertools.groupby(people, get_state)

for key, group in person_group:
    print(key)
    for person in group:
        print(person)
    print()

""" Imprime número de pessoas
de cada estado """
person_group = itertools.groupby(people, get_state)

for key, group in person_group:
    print(key, len(list(group)))


##################
### exemplo 28 ###
##################
""" tee
replicar o iterador """
globals().clear()
import itertools

def get_state(person):
    return person['state']

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

""" Imprime número de pessoas
de cada estado """
person_group = itertools.groupby(people, get_state)

copy1, copy2 = itertools.tee(person_group)

for key, group in person_group:
    print(key, len(list(group)))




