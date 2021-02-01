# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:20:53 2020

@author: pedro
"""

# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

##############################################
# 
globals().clear()

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

# print(emp_1)
# print(emp_2)

emp_1.first = 'Corey'
emp_1.first = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.apy = 50000

emp_2.first = 'Test'
emp_2.first = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.apy = 60000

print(emp_1.email)
print(emp_2.email)

##############################################
# init

globals().clear()

class Employee:
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@compay.com'
        
emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))

##############################################
# fullname

globals().clear()

class Employee:
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@compay.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)

print(emp_1.fullname())
print(emp_2.fullname())

print(Employee.fullname(emp_1))




















