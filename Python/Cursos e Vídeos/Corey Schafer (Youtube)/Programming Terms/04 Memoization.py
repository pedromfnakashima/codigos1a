# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 14:10:51 2020

@author: pedro
"""
# INEFICIENTE
import time

def expensive_func(num):
    print('Computing {}...'.format(num))
    time.sleep(1)
    return num * num

start_time = time.time()

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

print('Tempo de execução: ', (time.time() - start_time))

# EFICIENTE


import time

ef_cache = {}

def expensive_func(num):
    if num in ef_cache:
        return ef_cache[num]
    
    print('Computing {}...'.format(num))
    time.sleep(1)
    
    result = num * num
    ef_cache[num] = result
    
    return result

start_time = time.time()

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

print('Tempo de execução: ', (time.time() - start_time))









