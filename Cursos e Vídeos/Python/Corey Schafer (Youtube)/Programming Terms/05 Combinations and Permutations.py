# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 14:28:44 2020

@author: pedro
"""
import itertools


my_list = [1,2,3]

combinations = itertools.combinations(my_list,2)
permutations = itertools.permutations(my_list,2)

for c in combinations:
    print(c)

for p in permutations:
    print(p)

############################

my_list = [1,2,3,4,5,6]

combinations = itertools.combinations(my_list,3)
permutations = itertools.permutations(my_list,3)

lista = [result for result in combinations if sum(result) == 10]
print(lista)

lista = [result for result in permutations if sum(result) == 10]
print(lista)

############################

word = 'sample'
my_letters = 'plmeas'

combinations = itertools.combinations(my_letters,6)
permutations = itertools.permutations(my_letters,6)

for p in combinations:
    # print(p)
    if ''.join(p) == word:
        print('Match!')
        break
else:
    print('No Match!')

for p in permutations:
    # print(p)
    if ''.join(p) == word:
        print('Match!')
        break
else:
    print('No Match!')



