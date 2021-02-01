# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 18:40:25 2020

@author: pedro
"""

##############################
###### EXEMPLO 01 ############
##############################
""" 

"""
globals().clear()

student = {'name': 'John', 'age':25, 'courses': ['Math', 'CompSci']}

print(student)
print(student['name'])
print(student['courses'])

##############################
###### EXEMPLO 02 ############
##############################
""" 

"""
globals().clear()

student = {1: 'John', 'age':25, 'courses': ['Math', 'CompSci']}

print(student[1])

##############################
###### EXEMPLO 03 ############
##############################
""" acessando chave que
não existe
"""
globals().clear()

student = {'name': 'John', 'age':25, 'courses': ['Math', 'CompSci']}

""" dá erro """
print(student['phone'])
""" não dá erro (retorna None ou
alguma coisa personalizada) """
print(student.get('phone'))
print(student.get('phone', 'não encontrado!'))

##############################
###### EXEMPLO 04 ############
##############################
""" atualiza
"""
globals().clear()

student = {'name': 'John', 'age':25, 'courses': ['Math', 'CompSci']}

student['phone'] = '555-5555'
student['name'] = 'Jane'

print(student)


##############################
###### EXEMPLO 05 ############
##############################
""" atualiza com update()
útil para atualizar múltiplos
valores de uma vez só
"""
globals().clear()

student = {'name': 'John', 'age':25, 'courses': ['Math', 'CompSci']}

student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

print(student)

##############################
###### EXEMPLO 06 ############
##############################
""" deleta uma chave específica
e valores
"""
globals().clear()

student = {'name': 'John', 'age':25, 'courses': ['Math', 'CompSci']}

del student['age']

print(student)

##############################
###### EXEMPLO 07 ############
##############################
""" deleta uma chave específica
e valores com pop()
também retorna o valor (do
par excluído),
que colocamos na variável age
"""
globals().clear()

student = {'name': 'John', 'age':25, 'courses': ['Math', 'CompSci']}

age = student.pop('age')

print(student)
print(age)


##############################
###### EXEMPLO 08 ############
##############################
""" quantas chaves tem no
dicionário
"""
globals().clear()

student = {'name': 'John', 'age':25, 'courses': ['Math', 'CompSci']}

print(len(student))

##############################
###### EXEMPLO 09 ############
##############################
""" quais são as chaves e os
valores do dicionário
"""
globals().clear()

student = {'name': 'John', 'age':25, 'courses': ['Math', 'CompSci']}

print(student.keys())
print(student.values())
print(student.items())

##############################
###### EXEMPLO 10 ############
##############################
""" loop nas chaves e valores
"""
globals().clear()

student = {'name': 'John', 'age':25, 'courses': ['Math', 'CompSci']}

for chave, valor in student.items():
    print(chave, valor)
