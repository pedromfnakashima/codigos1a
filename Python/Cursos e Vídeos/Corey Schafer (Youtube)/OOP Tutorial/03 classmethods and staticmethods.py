# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 18:35:02 2020

@author: pedro

Diferença entre REGULAR METHOD, CLASSMETHOD, E
STATIC METHOD:

METODO REGULAR: passa automaticamente a
instância (SELF) como primeiro argumento.

CLASSMETHOD: passa automaticamente a
classe (CLS) como primeiro argumento.

STATIC METHOD: não passa nada automaticamente.

"""
# https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3


globals().clear()

class Employee:
    
    # variáveis de classe:
    num_of_emps = 0 # a cada vez que é criado uma nova instância, o valor é aumentado
    raise_amt = 1.04
    
    def __init__(self,first,last,pay): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@compay.com'
        # Aumenta num_of_emps na classe e em todas as instâncias
        Employee.num_of_emps += 1 # aqui é melhor usa o nome da classe (Emlployee) porque é interessante que o número de empregados seja o mesmo tanto para a classe quanto para todas as instâncias
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(Employee.pay * self.raise_amount) # não permite mudança do valor de raise_amount apenas na instância
        self.pay = int(self.pay * self.raise_amount) # permite mudança do valor de raise_amount apenas na instância
    
    @classmethod # aqui cls é a classe, e não a instância
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# Rodando o método da CLASSE, muda p/ a classe e todas as instâncias
Employee.set_raise_amt(1.05)

print(Employee.raise_amt) # 1.05
print(emp_1.raise_amt) # 1.05
print(emp_2.raise_amt) # 1.05

#########################################
"""
CLASS METHOD: decorado com @classmethod
"""

globals().clear()

class Employee:
    
    # variáveis de classe:
    num_of_emps = 0 # a cada vez que é criado uma nova instância, o valor é aumentado
    raise_amt = 1.04
    
    def __init__(self,first,last,pay): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@compay.com'
        # Aumenta num_of_emps na classe e em todas as instâncias
        Employee.num_of_emps += 1 # aqui é melhor usa o nome da classe (Emlployee) porque é interessante que o número de empregados seja o mesmo tanto para a classe quanto para todas as instâncias
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(Employee.pay * self.raise_amount) # não permite mudança do valor de raise_amount apenas na instância
        self.pay = int(self.pay * self.raise_amount) # permite mudança do valor de raise_amount apenas na instância
    
    @classmethod # aqui cls é a classe, e não a instância
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# Rodando o método da INSTÂNCIA, TAMBÉM muda p/ a classe e todas as instâncias, porque o método é de classe
emp_1.set_raise_amt(1.05)

print(Employee.raise_amt) # 1.05
print(emp_1.raise_amt) # 1.05
print(emp_2.raise_amt) # 1.05

#########################################



globals().clear()

class Employee:
    
    # variáveis de classe:
    num_of_emps = 0 # a cada vez que é criado uma nova instância, o valor é aumentado
    raise_amt = 1.04
    
    def __init__(self,first,last,pay): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # Aumenta num_of_emps na classe e em todas as instâncias
        Employee.num_of_emps += 1 # aqui é melhor usa o nome da classe (Emlployee) porque é interessante que o número de empregados seja o mesmo tanto para a classe quanto para todas as instâncias
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(Employee.pay * self.raise_amount) # não permite mudança do valor de raise_amount apenas na instância
        self.pay = int(self.pay * self.raise_amount) # permite mudança do valor de raise_amount apenas na instância
    
    @classmethod # aqui cls é a classe, e não a instância
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first,last,pay)

print(new_emp_1.email)
print(new_emp_1.pay)


#########################################
"""
Usando CLASSMETHOD como construtor da classe
alternativo

Employee.from_string(emp_str_1)

"""

globals().clear()

class Employee:
    
    # variáveis de classe:
    num_of_emps = 0 # a cada vez que é criado uma nova instância, o valor é aumentado
    raise_amt = 1.04
    
    def __init__(self,first,last,pay): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # Aumenta num_of_emps na classe e em todas as instâncias
        Employee.num_of_emps += 1 # aqui é melhor usa o nome da classe (Emlployee) porque é interessante que o número de empregados seja o mesmo tanto para a classe quanto para todas as instâncias
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(Employee.pay * self.raise_amount) # não permite mudança do valor de raise_amount apenas na instância
        self.pay = int(self.pay * self.raise_amount) # permite mudança do valor de raise_amount apenas na instância
    
    @classmethod # aqui cls é a classe, e não a instância
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
        
    @classmethod # construtror alternativo
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay) # retorna a classe cls

emp_1 = Employee('Corey','Schafer',50000)

print(emp_1.email)
print(emp_1.pay)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)


#########################################
"""
STATIC METHODS: decorado com @staticmethod

"""


globals().clear()

class Employee:
    
    # variáveis de classe:
    num_of_emps = 0 # a cada vez que é criado uma nova instância, o valor é aumentado
    raise_amt = 1.04
    
    def __init__(self,first,last,pay): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # Aumenta num_of_emps na classe e em todas as instâncias
        Employee.num_of_emps += 1 # aqui é melhor usa o nome da classe (Emlployee) porque é interessante que o número de empregados seja o mesmo tanto para a classe quanto para todas as instâncias
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(Employee.pay * self.raise_amount) # não permite mudança do valor de raise_amount apenas na instância
        self.pay = int(self.pay * self.raise_amount) # permite mudança do valor de raise_amount apenas na instância
    
    @classmethod # aqui cls é a classe, e não a instância
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
        
    @classmethod # construtror alternativo
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# emp_1 = Employee('Corey','Schafer',50000)
# emp_2 = Employee('Test','User',60000)

import datetime

my_date = datetime.date(2016,7,10)
print(Employee.is_workday(my_date))

my_date = datetime.date(2016,7,11)
print(Employee.is_workday(my_date))









