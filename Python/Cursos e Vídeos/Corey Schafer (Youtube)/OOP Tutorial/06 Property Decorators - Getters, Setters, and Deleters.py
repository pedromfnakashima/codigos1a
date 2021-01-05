# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 09:13:39 2020

@author: pedro
"""

# https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6

#############################################
"""
Decorador @property
Permite definir um método, e acessá-lo como
um atributo.
"""


globals().clear()

class Employee:
    
    
    def __init__(self,first,last): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John','Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email) # John.Smith@company.com
print(emp_1.fullname())

#############################################

globals().clear()

class Employee:
    
    
    def __init__(self,first,last): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
        
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John','Smith')


emp_1.first = 'Jim'
print(emp_1.first)
# Acessando o email como MÉTODO
print(emp_1.email()) # Jim.Smith@company.com
print(emp_1.fullname())

#############################################

globals().clear()

class Employee:
    
    
    def __init__(self,first,last): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John','Smith')


emp_1.first = 'Jim'
print(emp_1.first)
# Acessando o email como ATRIBUTO
print(emp_1.email) # Jim.Smith@company.com
# Acessando o nome completo como ATRIBUTO
print(emp_1.fullname)

#############################################
"""
Problema (dá erro).
Não é possível fazer
emp_1.fullname = 'Corey Schafer'
A solução é criando-se um SETTER.
"""
globals().clear()

class Employee:
    
    
    def __init__(self,first,last): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John','Smith')

emp_1.fullname = 'Corey Schafer' # dá ERRO !!!

#############################################
"""
Para mudar com o nome completo do empregado.

Problema (dá erro).
Não é possível fazer
emp_1.fullname = 'Corey Schafer'
A solução é criando-se um SETTER.

O nome do DECORADOR é o mesmo NOME do
método que queremos definir como atributo,
mais .setter.

Exemplo.
@property
def fullname(self)

-->

@fullname.setter
def fullname(self, name)

name é o valor que queremos definir

"""
globals().clear()

class Employee:
    
    
    def __init__(self,first,last): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name): # tem que ser o mesmo nome da função que define o método como propriedade
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp_1 = Employee('John','Smith')

emp_1.fullname = 'Corey Schafer' # NÃO dá erro !!!

print(emp_1.first) # Corey
# Acessando o email como ATRIBUTO
print(emp_1.email) # Corey.Schafer@company.com
# Acessando o nome completo como ATRIBUTO
print(emp_1.fullname) # Corey Schafer

#############################################

"""
Para deletar o empregado com del.

Passos:
    
@NOMEDOMÉTODODECORADOR.deleter
def NOMEDOMÉTODODECORADOR
    self.atributo = NONE

"""

globals().clear()

class Employee:
    
    
    def __init__(self,first,last): # roda sempre que é criada uma nova instância
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property # <- permite acessar o retorno da função abaixo como atributo (é o getter)
    def fullname(self): # <- acessado como atributo
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter # <- @ + nome da função que é acessada como atributo + .setter
    def fullname(self, name): # tem que ser o mesmo nome da função que define o método como propriedade
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter # <- @ + nome da função que é acessada como atributo + .deleter
    def fullname(self): # tem que ser o mesmo nome da função que define o método como propriedade
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('John','Smith')
emp_1.fullname = 'Corey Schafer' # NÃO dá erro !!!

del emp_1.fullname
























