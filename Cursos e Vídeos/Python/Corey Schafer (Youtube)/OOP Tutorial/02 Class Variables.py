# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:40:51 2020

@author: pedro
"""
# https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2
#############################################

globals().clear()

class Employee:
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@compay.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)

print(emp_1.pay)

emp_1.apply_raise()

print(emp_1.pay)

#############################################
'''
raise_amount é variável de classe.
Deve ser acessada de uma das duas formas:
    * self.raise_amount - permite mudar o valor
    da variável de classe raise_amount apenas para
    a instância
    * Employee.raise_amount - NÃO permite mudar o valor
    da variável de classe raise_amount apenas para
    a instância

No exemplo abaixo, é melhor usar referenciar
a variável de classe por self.raise_amount, pois
permite que mude o valor dela apenas em uma
instância específica
'''
globals().clear()

class Employee:
    
    # variável de classe:
    raise_amount = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@compay.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount) # não permite mudança do valor de raise_amount apenas na instância
        self.pay = int(self.pay * self.raise_amount) # permite mudança do valor de raise_amount apenas na instância


emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)

print(emp_1.pay)

emp_1.apply_raise()

print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

"""
NÃO EXISTE o atributo raise_amount para as
instâncias, apenas para a classe
"""
print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)

# 
"""
Mudando o valor da variável de classe, 
USANDO A CLASSE, muda o
valor dela para a classe E PARA TODAS as suas
instâncias
"""
Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

"""
Mudando o valor da variável de classe, 
USANDO A INSTÂNCIA, muda o
valor dela para a INSTÂNCIA, MAS NÃO PARA
AS DEMAIS instâncias, NEM para a classe
toda.
Aqui, na verdade CRIOU o atributo raise_amount
para instância emp_1
"""
emp_1.raise_amount = 1.06

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)

##############################################
"""
No exemplo abaixo, é melhor usar referenciar
a variável de classe por Employee.raise_amount
Aqui é melhor usa o nome da classe (Emlployee)
porque é interessante que o número de
empregados seja o mesmo tanto para a
classe quanto para todas as instâncias
"""
globals().clear()

class Employee:
    
    # variáveis de classe:
    num_of_emps = 0 # a cada vez que é criado uma nova instância, o valor é aumentado
    raise_amount = 1.04
    
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


emp_1 = Employee('Corey','Schafer',50000)

print(emp_1.num_of_emps) # 1

emp_2 = Employee('Test','User',60000)

print(emp_1.num_of_emps) # 2
