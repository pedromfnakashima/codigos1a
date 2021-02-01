# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 10:58:02 2020

@author: pedro
"""

# https://www.youtube.com/watch?v=bD05uGo_sVI&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=36

############################################

globals().clear()

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])

print(my_nums)

############################################

"""
Converter num generator

Geradores não armazenam o resultado total
na memória. Ele fornece (yield) um resultado
por vez
"""

globals().clear()

def square_numbers(nums):

    for i in nums:
        yield (i*i)


my_nums = square_numbers([1,2,3,4,5])

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

############################################

# List compreension

my_nums = [x*x for x in [1,2,3,4,5]]

############################################

"""
Converter num generator

Geradores não armazenam o resultado total
na memória. Ele fornece (yield) um resultado
por vez
"""

globals().clear()

def square_numbers(nums):

    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5])

for num in my_nums:
    print(num)

############################################
"""
Generator
"""

my_nums = (x*x for x in [1,2,3,4,5])

print(my_nums)

for num in my_nums:
    print(num)

"""
Convertendo Generator em List
Há perda de performance
"""
my_nums = (x*x for x in [1,2,3,4,5])
print(list(my_nums))

############################################
"""
Ilustrando a diferença de performance
entre generator e list
"""

globals().clear()
# pip install memory_profiler

import memory_profiler as mem_profile
import random
import time

names = ['John','Corey','Adam','Steve','Rick','Thomas']
majors = ['Math','Engineering','CompSci','Arts','Business']

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                'id':i,
                'name':random.choice(names),
                'major':random.choice(majors)
            }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                'id':i,
                'name':random.choice(names),
                'major':random.choice(majors)
            }
    yield person

# t1 = time.time()
# people = people_list(1_000_000)
# t2 = time.time()

# t1 = time.time()
# people = people_generator(1_000_000)
# t2 = time.time()

t1 = time.time()
people = list(people_generator(1_000_000))
t2 = time.time()


print('Memory (After): {}Mb'.format(mem_profile.memory_usage()))
print('Took {} Seconds'.format(t2-t1))







