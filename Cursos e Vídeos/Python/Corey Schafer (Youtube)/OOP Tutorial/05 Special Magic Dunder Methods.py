# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 08:32:19 2020

@author: pedro
"""

# https://www.youtube.com/watch?v=3ohzBxoFHAY&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=5

###########################################

globals().clear()

print(1 + 2)
print('a' + 'b')

class Employee:
    
    # variável de classe:
    raise_amt = 1.04
    
    def __init__(self,first,last,pay): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(Employee.pay * self.raise_amount) # não permite mudança do valor de raise_amount apenas na instância
        self.pay = int(self.pay * self.raise_amt) # permite mudança do valor de raise_amount apenas na instância

emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','Employee',60000)

print(emp_1)

repr(emp_1)
str(emp_1)

###########################################
"""
__repr__ é mais para o dev, identifica de
forma única o objeto.
__str__ é mais direcionado ao usuário
final. Deve ser mais legível.
"""

globals().clear()

class Employee:
    
    # variável de classe:
    raise_amt = 1.04
    
    def __init__(self,first,last,pay): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(Employee.pay * self.raise_amount) # não permite mudança do valor de raise_amount apenas na instância
        self.pay = int(self.pay * self.raise_amt) # permite mudança do valor de raise_amount apenas na instância
        
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    # def __str__(self):
    #     return '{} - {}'.format(self.fullname(),self.email)


emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','Employee',60000)

print(emp_1)

###########################################

"""
__repr__ é mais para o dev, identifica de
forma única o objeto.
__str__ é mais direcionado ao usuário
final. Deve ser mais legível.
"""

globals().clear()

class Employee:
    
    # variável de classe:
    raise_amt = 1.04
    
    def __init__(self,first,last,pay): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(Employee.pay * self.raise_amount) # não permite mudança do valor de raise_amount apenas na instância
        self.pay = int(self.pay * self.raise_amt) # permite mudança do valor de raise_amount apenas na instância
        
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)


emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','Employee',60000)

print(emp_1)

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

###########################################

globals().clear()

print(1+2)
print(int.__add__(1,2))
print(str.__add__('a','b'))

print(len('test'))
print('test'.__len__())

"""
Com o método especial __add__:
Retornamos com print o salário total adicionando os
empregados.

Com o método especial __len__:
Retornamos com print o número de caracteres
do nome completo.

"""

class Employee:
    
    # variável de classe:
    raise_amt = 1.04
    
    def __init__(self,first,last,pay): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(Employee.pay * self.raise_amount) # não permite mudança do valor de raise_amount apenas na instância
        self.pay = int(self.pay * self.raise_amt) # permite mudança do valor de raise_amount apenas na instância
        
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','Employee',60000)

# Método __add__
print(emp_1 + emp_2)

# Método __len__
print(len(emp_1))
















