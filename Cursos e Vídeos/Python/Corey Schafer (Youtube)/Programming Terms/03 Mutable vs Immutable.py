# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:53:33 2020

@author: pedro
"""
# String é IMUTÁVEL

a = 'corey'
print(a)
print('Address of a is: {}'.format(id(a)))

a = 'john'
print(a)
print('Address of a is: {}'.format(id(a))) # endereço diferente, porque string é imutável

a[0] = 'C' # Erro, porque string é imutável
print(a)
print('Address of a is: {}'.format(id(a)))

# Lista é MUTÁVEL

a = [1,2,3,4,5]
print(a)
print('Address of a is: {}'.format(id(a))) # endereço diferente, porque string é imutável

a[0] = 6 # Sem erro, porque lista é mutável
print(a)
print('Address of a is: {}'.format(id(a))) # mesmo endereço

#

employees = ['Corey','John','Rick','Steve','Carl','Adam']
output = '<ul>\n'

for employee in employees:
    output += '\t<li>{}</li>\n'.format(employee)

output += '</ul>'

print(output)

print('\n')

#

employees = ['Corey','John','Rick','Steve','Carl','Adam']
output = '<ul>\n'

for employee in employees:
    output += '\t<li>{}</li>\n'.format(employee)
    print('Address of output is {}'.format(id(output))) # endereço diferente -> cria um objeto string a cada iteração
output += '</ul>'

print(output)

print('\n')







