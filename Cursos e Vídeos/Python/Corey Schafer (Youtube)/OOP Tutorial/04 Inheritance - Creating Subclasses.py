# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 19:32:25 2020

@author: pedro
"""

# https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4

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
        self.pay = int(self.pay * self.raise_amount) # permite mudança do valor de raise_amount apenas na instância

class Developer(Employee):
    pass

dev_1 = Developer('Corey','Schafer',50000)
dev_2 = Developer('Test','Employee',60000)

print(dev_1.email)
print(dev_2.email)

print(help(Developer))

"""
 |  Method resolution order:
 |      Developer
 |      Employee
 |      object
 
 |  Methods inherited from Employee:
 |  
 |  __init__(self, first, last, pay)
 |  
 |  apply_raise(self)
 |  
 |  fullname(self)
"""

###########################################

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

class Developer(Employee):
    pass

dev_1 = Developer('Corey','Schafer',50000)
dev_2 = Developer('Test','Employee',60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

###########################################
"""
O aumento dos devs é maior
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

class Developer(Employee):
    raise_amt = 1.1

dev_1 = Developer('Corey','Schafer',50000)
dev_2 = Developer('Test','Employee',60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

###########################################
"""
Se voltar para Employee, volta a ser 1.04
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

class Developer(Employee):
    raise_amt = 1.1

dev_1 = Employee('Corey','Schafer',50000)
dev_2 = Developer('Test','Employee',60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

###########################################
"""
A classe filha pode ser iniciada com mais
atributos que a classe mãe.
Basta colocar um método __init__ na classe
filha e adicionar atributos.
Os atributos que são repetidos são
substituídos por:

super().__init__(ATRIBUTOS)
ou
CLASSEMÃE.__init__(ATRIBUTOS)

Exemplo:

super().__init__(first,last,pay)
ou
Employee.__init__(first,last,pay)

O último é menos maintainable, mas tb
é útil quando há múltiplas heranças.

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

class Developer(Employee):
    raise_amt = 1.1
    
    # A classe-filha deve ter como argumentos todos os atributos, repetidos (da classe-mãe) e novos (da classe-filha)
    def __init__(self,first,last,pay,prog_lang): # roda sempre que é criada uma nova instância
        # A linha abaixo faz herdar os atributos repetidos da classe-mãe:
        super().__init__(first,last,pay)
        # Novos atributos:
        self.prog_lang = prog_lang

dev_1 = Developer('Corey','Schafer',50000,'Python')
dev_2 = Developer('Test','Employee',60000,'Java')

print(dev_1.email)
print(dev_1.prog_lang)

###########################################
"""
A classe Manager tem uma lista de empregados
que o gerente supervisiona.
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

class Developer(Employee):
    raise_amt = 1.1
    
    # A classe-filha deve ter como argumentos todos os atributos, repetidos (da classe-mãe) e novos (da classe-filha)
    def __init__(self,first,last,pay,prog_lang): # roda sempre que é criada uma nova instância
        # A linha abaixo faz herdar os atributos repetidos da classe-mãe:
        super().__init__(first,last,pay)
        # Novos atributos:
        self.prog_lang = prog_lang

class Manager(Employee):

        def __init__(self,first,last,pay,employees=None): # roda sempre que é criada uma nova instância
            # A linha abaixo faz herdar os atributos repetidos da classe-mãe:
            super().__init__(first,last,pay)
            # Novos atributos:
            if employees is None:
                self.employees = []
            else:
                self.employees = employees
        
        def add_emp(self,emp):
            if emp not in self.employees:
                self.employees.append(emp)
        
        def remove_emp(self,emp):
            if emp in self.employees:
                self.employees.remove(emp)
        
        def print_emps(self):
            for emp in self.employees:
                print('-->',emp.fullname())

dev_1 = Developer('Corey','Schafer',50000,'Python')
dev_2 = Developer('Test','Employee',60000,'Java')

mgr_1 = Manager('Sue','Smith',90000,[dev_1])

print(mgr_1.email)

mgr_1.print_emps()

mgr_1.add_emp(dev_2)

mgr_1.print_emps()

mgr_1.remove_emp(dev_1)

mgr_1.print_emps()


###########################################
"""
isinstance():
    - diz se um objeto é instância de uma
    classe;
issubclass():
    - diz se uma classe é subclasse de
    outra classe.
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

class Developer(Employee):
    raise_amt = 1.1
    
    # A classe-filha deve ter como argumentos todos os atributos, repetidos (da classe-mãe) e novos (da classe-filha)
    def __init__(self,first,last,pay,prog_lang): # roda sempre que é criada uma nova instância
        # A linha abaixo faz herdar os atributos repetidos da classe-mãe:
        super().__init__(first,last,pay)
        # Novos atributos:
        self.prog_lang = prog_lang

class Manager(Employee):

        def __init__(self,first,last,pay,employees=None): # roda sempre que é criada uma nova instância
            # A linha abaixo faz herdar os atributos repetidos da classe-mãe:
            super().__init__(first,last,pay)
            # Novos atributos:
            if employees is None:
                self.employees = []
            else:
                self.employees = employees
        
        def add_emp(self,emp):
            if emp not in self.employees:
                self.employees.append(emp)
        
        def remove_emp(self,emp):
            if emp in self.employees:
                self.employees.remove(emp)
        
        def print_emps(self):
            for emp in self.employees:
                print('-->',emp.fullname())

dev_1 = Developer('Corey','Schafer',50000,'Python')
dev_2 = Developer('Test','Employee',60000,'Java')

mgr_1 = Manager('Sue','Smith',90000,[dev_1])

print(isinstance(mgr_1,Manager)) # True
print(isinstance(mgr_1,Employee)) # True
print(isinstance(mgr_1,Developer)) # False

print(issubclass(Developer,Employee)) # True
print(issubclass(Manager,Employee)) # True
print(issubclass(Manager,Developer)) # False








