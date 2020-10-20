# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:31:44 2020

@author: pedro
"""
globals().clear()
###############################
# Dica 1 ######################
###############################
globals().clear()
condicao = False
x = 1 if condicao else 0
print(x)
###############################
# Dica 2 ######################
###############################
globals().clear()
num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2
print(f'{total:,}')
###############################
# Dica 3 ######################
###############################
"""
Com o context manager (with open), abre e fecha
automaticamente o texto, ou a base
de dados.
"""
globals().clear()
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    print('Logado de casa')
    caminho = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('Logado da salj-alems')
    caminho = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

with open(caminho / 'Cursos e Livros' / 'Corey Schafer - Youtube' / '10 Python Tips and Tricks' /'test.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

###############################
# Dica 4 ######################
###############################
globals().clear()
nomes = ['João', 'Maria', 'Manoel', 'Ana']
for indice, nome in enumerate(nomes):
    print(indice, nome)

nomes = ['João', 'Maria', 'Manoel', 'Ana']
for indice, nome in enumerate(nomes, start=1):
    print(indice, nome)

###############################
# Dica 5 ######################
###############################
globals().clear()
nomes = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
herois = ['Homem Aranha', 'Super homem', 'Deadpool', 'Batman']
universos = ['Marvel', 'DC', 'Marvel', 'DC']

for nome, heroi, universo in zip(nomes, herois, universos):
    print(f'{nome} é na verdade {heroi} da {universo}.\n')

for valor in zip(nomes, herois, universos):
    print(valor)

###############################
# Dica 6 ######################
###############################
""" Unpacking """
globals().clear()
a, b = (1,2)
print(a)
print(b)

""" Unpacking ignorando a segunda
variável """
a, _ = (1,2)
print(a)

""" c carrega o resto """
globals().clear()
a, b, *c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

""" *_ serve p/ ignorar o resto """
globals().clear()
a, b, *_ = (1, 2, 3, 4, 5)
print(a)
print(b)

""" 
a e b são os dois primeiros
c é  todos os demais até o último (não incluindo)
d é o último
"""
globals().clear()
a, b, *c, d = (1, 2, 3, 4, 5, 6, 7)
print(a)
print(b)
print(c)
print(d)

""" 
a e b são os dois primeiros
o meio, até o último, é ignorado (não incluindo)
d é o último
"""
globals().clear()
a, b, *_, d = (1, 2, 3, 4, 5, 6, 7)
print(a)
print(b)
print(d)

###############################
# Dica 7 ######################
###############################
""" Definindo atributos de um objeto
de forma tradicional """
globals().clear()
class Pessoa():
    pass

pessoa = Pessoa()
pessoa.primeiro = "Pedro"
pessoa.ultimo = "Nakashima"

print(pessoa.primeiro)
print(pessoa.ultimo)

""" Definindo atributos de um objeto
dinamicamente com setattr"""
globals().clear()

class Pessoa():
    pass

pessoa = Pessoa()

setattr(pessoa, 'primeiro', 'Pedro')

print(pessoa.primeiro)

""" Definindo atributos de um objeto
dinamicamente com setattr"""
globals().clear()

class Pessoa():
    pass

pessoa = Pessoa()

primeira_chave = 'primeiro'
primeiro_valor = 'Pedro'

setattr(pessoa, primeira_chave, primeiro_valor)

print(pessoa.primeiro)

""" Acessando atributos de um objeto
dinamicamente com getattr"""
globals().clear()

class Pessoa():
    pass

pessoa = Pessoa()

primeira_chave = 'primeiro'
primeiro_valor = 'Pedro'

setattr(pessoa, primeira_chave, primeiro_valor)

first = getattr(pessoa, primeira_chave)

print(first)

""" Definindo atributos de um objeto
dinamicamente com setattr.
Outro exemplo."""
globals().clear()

class Pessoa():
    pass

pessoa = Pessoa()

pessoa_info = {'primeiro':'Pedro', 'ultimo':'Nakashima'}

for chave, valor in pessoa_info.items():
    setattr(pessoa, chave, valor)

print(pessoa.primeiro)
print(pessoa.ultimo)

""" Definindo e acessando
atributos de um objeto
dinamicamente com setattr getattr.
Outro exemplo."""
globals().clear()

class Pessoa():
    pass

pessoa = Pessoa()

pessoa_info = {'primeiro':'Pedro', 'ultimo':'Nakashima'}

for chave, valor in pessoa_info.items():
    setattr(pessoa, chave, valor)

for chave in pessoa_info.keys():
    print(getattr(pessoa, chave))


###############################
# Dica 8 ######################
###############################
""" Fazendo input de informação
secreta.
Em arquivos separados!"""


###############################
# Dica 9 ######################
###############################
""" Quando não sabe os parâmetros
python
import smtpd
help(smtpd)

from datetime import datetime
dir(datetime)
-> mostra todos os métodos
disponíveis em datetime
datetime.today
-> mostra que é um método builtin
datetime.today()
-> executa (mostra o dia atual)
sair do python: exit()
"""


###############################
# Dica 10 #####################
###############################
""" não tem """


