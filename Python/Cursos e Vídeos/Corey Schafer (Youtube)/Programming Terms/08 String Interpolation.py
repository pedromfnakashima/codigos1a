# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:58:19 2020

@author: pedro
"""

name = 'Corey'
age = 28

greeting = 'My name is ' + name + ' and I am ' + str(age) + ' years old'

print(greeting)

################################

greeting = 'My name is {} and I am {} years old'.format(name,age)

print(greeting)


################################

greeting = 'I am {age} years old and my name is {name}'.format(name=name,age=age)

print(greeting)














