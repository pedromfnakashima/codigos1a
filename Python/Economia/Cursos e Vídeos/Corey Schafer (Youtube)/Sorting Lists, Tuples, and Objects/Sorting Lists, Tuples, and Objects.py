# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:43:55 2020

@author: pedro
"""
############################
# Exemplo 01 ###############
############################
"""  """
globals().clear()
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li) # mudança inplace

print('Sorted Variable:\t', s_li)

li.sort()

print('Original Variable:\t', li)

############################
# Exemplo 02 ###############
############################
"""  """
globals().clear()
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li, reverse=True)

print('Sorted Variable:\t', s_li)

############################
# Exemplo 03 ###############
############################
"""  """
globals().clear()
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)

s_tup = sorted(tup)

print('Sorted Tup:\t', s_tup)

############################
# Exemplo 04 ###############
############################
"""  """
globals().clear()

di ={'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}

s_di = sorted(di)

print('Sorted Dic:\t', s_di)

############################
# Exemplo 05 ###############
############################
"""  """
globals().clear()

li = [-6, -5, -4, 1, 2, 3]

print(li)

s_li = sorted(li)

print(s_li)

""" com base no valor absoluto """

globals().clear()

li = [-6, -5, -4, 1, 2, 3]

print(li)

s_li = sorted(li, key=abs)

print(s_li)

############################
# Exemplo 06 ###############
############################
"""  """
globals().clear()

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

def e_sort(emp):
    return emp.name

s_employees = sorted(employees, key=e_sort)

print(s_employees)

############################
# Exemplo 07 ###############
############################
"""  """
globals().clear()

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

def e_sort(emp):
    return emp.age

s_employees = sorted(employees, key=e_sort)

print(s_employees)

############################
# Exemplo 08 ###############
############################
"""  """
globals().clear()

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

def e_sort(emp):
    return emp.salary

s_employees = sorted(employees, key=e_sort)

print(s_employees)


############################
# Exemplo 09 ###############
############################
"""  """
globals().clear()

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

def e_sort(emp):
    return emp.salary

s_employees = sorted(employees, key=e_sort, reverse=True)

print(s_employees)

############################
# Exemplo 10 ###############
############################
"""  """
globals().clear()

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

s_employees = sorted(employees, key=lambda e: e.name)

print(s_employees)

############################
# Exemplo 11 ###############
############################
""" attrgetter """

globals().clear()

from operator import attrgetter

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

s_employees = sorted(employees, key=attrgetter('age'))

print(s_employees)










