# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 07:37:45 2019

@author: Pedro
"""

###############################################################################
# LAMBDA
###############################################################################

def square(num):
    result = num ** 2
    return result

square(2)
###

def square(num):
    return num ** 2

square(2)
###

def square(num): return num**2
square(2)
###

square = lambda num: num**2
square(2)
###

eh_par = lambda num: num%2 == 0

eh_par(4)
###
first = lambda s: s[0]

first('hello')
###
rev = lambda s: s[::-1]
rev('hello')
###

soma = lambda x,y: x+y
soma(10,20)

"""
Funções lambda usadas com:
    map()
    filter()
    reduce()

"""
###############################################################################
# LAMBDA, map(), filter() e reduce() ############################
###############################################################################

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

map(square, my_nums) # iterável -> aplica looping ou list()

for item in map(square, my_nums):
    print(item)

list(map(square, my_nums))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']

list(map(splicer, names))

######################################################################

def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]

filter(check_even, mynums) # iterável -> aplica looping ou list()

for x in filter(check_even, mynums):
    print(x)

list(filter(check_even, mynums))

#####################################################################

def square(num):
    result = num ** 2
    return result

square(3)

# 1

def square(num):
    return num ** 2

square(3)

# 2

def square(num): return num ** 2

square(3)

# 3

lambda num: num ** 2 # é retornado tudo o que está à direita de dois pontos

square = lambda num: num ** 2

square(3)

# 4 - Usando de forma anônima, com map() e filter()
""" Útil quando se quer usar só uma vez """

map(lambda num: num ** 2, mynums)

list(map(lambda num: num ** 2, mynums))

#################################################################

lambda num: num%2 == 0

filter(lambda num: num%2 == 0, mynums)

list(filter(lambda num: num%2 == 0, mynums))

#################################################################

map(lambda x: x[0], names)
list(map(lambda x: x[0], names))

#################################################################

map(lambda x: x[::-1], names)
list(map(lambda x: x[::-1], names))

#################################################################




###############################################################################
# ESCOPO ###################################################
###############################################################################




x = 25 # esse x tem escopo global

def printer():
    x = 50 # esse x tem escopo local
    return x

print(x)
print(printer())


f = lambda x: x**2 # esse x tem escopo local

nome = 'esse nome tem escopo global'

def saudar():
    nome = 'Maria'
    
    def olá():
        print(f"Olá {nome}")
    
    olá()

saudar() # Olá Maria

"""
Regras de escopo:
    1) Procura se tem dentro da própria função.
    2) Se não encontra dentro da própria função, procura na função de fora.
    3) Vai seguindo o fluxo.

Quando você declara variáveis DENTRO da definição de uma função,
elas NÃO estão relacionadas de nenhuma forma com os mesmos nomes usados
FORA da função - isto é, nomes das variáveis são locais para as funções.
Ex.:
"""

x = 50
def func(x):
    print(f"x é {x}")
    x = 2
    print(f"Mudado o x local para {x}")
func(x)
print(f"x ainda é {x}")

"""
Se você quer atribuir a uma variável um valor definido no topo de do programa
(isto é, fora de um escopo, tal como uma função ou uma classe), então você
tem que dizer ao Python que aquele nome não é local, mas global.
Fazemos isso usando a palavra 'global'.
Ex.:
"""

x = 50
def func():
    global x
    print("Essa função agora está usando o x global!")
    print(f"Porque o x global é {x}")
    x = 2
    print(f"Execute func(), mudado o x global para {x}")

print(f"Antes de executar func(), x é {x}")
func()
print(f"Valor de x (fora de func()) é {x}")

"""
Tudo no Python é um objeto.
Isso significa 1que posso atribuir funções a variáveis tal como números.
Ver seção de decoradores.
"""



"""
Dentro da função lambda, todas as variáveis são locais. Ex.

lambda num: num**2

"""



###############################################################################
# *ARGS E **ARGS
###############################################################################

### *ARGS: passa uma TUPLA

def myfunc(a,b):
    # Retorna 5% da soma de a e b
    return sum((a,b)) * 0.05

myfunc(40,60)

def myfunc(*args):
    print(args) # imprime uma tupla
    return sum(args) * 0.05

myfunc(40,60)
myfunc(40,60,100)

def myfunc(*variaveis):
    print(variaveis) # imprime uma tupla
    return sum(variaveis) * 0.05

myfunc(40,60)
myfunc(40,60,100)
myfunc(40,60,100,1,34)


def myfunc(*args):
    for item in args:
        print(item)

myfunc(40,60,100,1,34)

def myfunc(*tupla):
    for item in tupla:
        print(item)

myfunc(40,60,100,1,34)

### **ARGS: passa um DICIONÁRIO

def myfunc(**kwargs):
    if 'fruta' in kwargs:
        print('Minha fruta escolhida é {}'.format(kwargs['fruta']))
    else:
        print('Não encontrei nenhuma fruta aqui.')

myfunc(fruta='maçã')

myfunc(fruta='maçã', verdura = 'alface')

###

def myfunc(**kwargs):
    print(kwargs)
    if 'fruta' in kwargs:
        print('Minha fruta escolhida é {}'.format(kwargs['fruta']))
    else:
        print('Não encontrei nenhuma fruta aqui.')

myfunc(fruta='maçã')

myfunc(fruta='maçã', verdura = 'alface')

myfunc(fruta='uva', verdura = 'alface')

###
def myfunc(**dicionario):
    print(dicionario)
    if 'fruta' in dicionario:
        print('Minha fruta escolhida é {}'.format(dicionario['fruta']))
    else:
        print('Não encontrei nenhuma fruta aqui.')

myfunc(fruta='maçã')

###

def myfunc(*args, **kwargs):
    print('Eu queria {} {}'.format(args[0], kwargs['comida']))

myfunc(10,20,30, fruta='laranja', comida='ovos', animal='cachorrro')

###

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('Eu queria {} {}'.format(args[0], kwargs['comida']))

myfunc(10,20,30, fruta='laranja', comida='ovos', animal='cachorrro')

###

def myfunc(*tupla, **dicionario):
    print(tupla)
    print(dicionario)
    print('Eu queria {} {}'.format(tupla[0], dicionario['comida']))

myfunc(10,20,30, fruta='laranja', comida='ovos', animal='cachorrro')

def myfunc2(**dicionario, *tupla):
    print(tupla)
    print(dicionario)
    print('Eu queria {} {}'.format(tupla[0], dicionario['comida']))

myfunc2(fruta='laranja', comida='ovos', animal='cachorrro', 10,20,30, )

def myfunc3(**dicionario1, **dicionario2):
    print(tupla)
    print(dicionario1)
    print('Eu queria {} {}'.format(tupla[0], dicionario1['comida']))

myfunc(fruta='laranja', comida='ovos', animal='cachorrro', 10,20,30, )






"""
ATENÇÃO! a ordem da definição (tupla, dicionário) deve ser seguida!
Não é possível algo como:
    myfunc(10,20,30, fruta='laranja', comida='ovos', animal='cachorrro', 100)
"""

###################################################################
# Programação Orientada por Objetos ###############################
###################################################################

"""
__init__() é um construtor para a classe. É chamado automaticamente
quando você cria uma instância da classe.
self representa a própria instância do objeto.

"""


class Sample(): # Por CONVENÇÃO, nome da classe é CAPITALIZADO
    pass

my_sample = Sample()

type(my_sample)

## Por convenção (nome do argumento = nome do atributo)

class Dog():
    
    def __init__(self, breed):
        self.breed = breed

my_dog = Dog() # erro (falta o parâmetro breed)

my_dog = Dog(breed = 'Lab')

type(my_dog)

my_dog.breed

## Mas o nome do argumento não precisa ser igual ao nome do atributo:

class Dog():
    
    def __init__(self, mybreed):
        # Atributos
        # Pegamos o argumento e
        # Atribuímos usando self.nome_do_atributo
        self.breed = mybreed

my_dog = Dog(mybreed='Huskie') # usa o nome do ARGUMENTO

my_dog.breed # usa o nome do ATRIBUTO

###

class Dog():
    
    def __init__(self, mybreed):
        # Atributos
        # Pegamos o argumento e
        # Atribuímos usando self.nome_do_atributo
        self.meu_atributo = mybreed

my_dog = Dog(mybreed='Huskie') # usa o nome do ARGUMENTO

my_dog.meu_atributo # usa o nome do ATRIBUTO

"""
Mas, por CONVENÇÃO, usa-se o mesmo nome para o argumento e o atributo
Assim:
"""

class Dog():
    
    def __init__(self, breed):
        # Atributos
        # Pegamos o argumento e
        # Atribuímos usando self.nome_do_atributo
        self.breed = breed

#############################################

class Dog():
    
    def __init__(self, breed, name, spots):
        # Atributos
        # Pegamos o argumento e
        # Atribuímos usando self.nome_do_atributo
        self.breed = breed
        self.name = name
        
        # Esperando booleano True/False:
        self.spots = spots

my_dog = Dog(breed='lab', name='Sammy', spots=False)

my_dog.breed
my_dog.name
my_dog.spots

my_dog = Dog(breed='lab', name='Sammy', spots='NO SPOTS')

my_dog.spots

##############################################

class Dog():
    
    # CLASS OBJECT ATTRIBUTO
    # MESMO PARA QUALQUER INSTÂNCIA DA CLASSE:
    species = 'mammal'
    
    
    def __init__(self, breed, name, spots):
        # Atributos
        # Pegamos o argumento e
        # Atribuímos usando self.nome_do_atributo
        self.breed = breed
        self.name = name
        
        # Esperando booleano True/False:
        self.spots = spots

my_dog = Dog(breed='lab', name='Sam', spots=False)

my_dog.species
my_dog.breed
my_dog.name
my_dog.spots

##############################################

class Dog():
    
    # CLASS OBJECT ATTRIBUTO
    # MESMO PARA QUALQUER INSTÂNCIA DA CLASSE:
    species = 'mammal'
    
    
    def __init__(self, breed, name):
        # Atributos
        # Pegamos o argumento e
        # Atribuímos usando self.nome_do_atributo
        self.breed = breed
        self.name = name
        
    
    # OPERAÇÕES/AÇÕES -->> Methods
    def bark(self):
        print(f"WOOF! My name is {self.name}")
    

my_dog = Dog(breed='Lab', name='Frankie')

my_dog.species
my_dog.breed
my_dog.name

my_dog.bark()

##############################################

class Dog():
    
    # CLASS OBJECT ATTRIBUTO
    # MESMO PARA QUALQUER INSTÂNCIA DA CLASSE:
    species = 'mammal'
    
    
    def __init__(self, breed, name):
        # Atributos
        # Pegamos o argumento e
        # Atribuímos usando self.nome_do_atributo
        self.breed = breed
        self.name = name
        
    
    # OPERAÇÕES/AÇÕES -->> Methods
    def bark(self, number):
        print(f"WOOF! My name is {self.name}, and the number is {number}")
    

my_dog = Dog(breed='Lab', name='Frankie')

my_dog.bark(number = 10)
my_dog.bark(10)

##############################################

class Circle():
    
    # CLASS OBJECT ATTRIBUTE:
    pi = 3.14
    
    def __init__(self, radius=1):
        
        self.radius = radius
        
    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle()
my_circle.pi
my_circle.radius # 1

my_circle = Circle(30)
my_circle.pi
my_circle.radius # 30

my_circle.get_circumference()

##############################################

class Circle():
    
    # CLASS OBJECT ATTRIBUTE:
    pi = 3.14
    
    def __init__(self, radius=1):
        
        self.radius = radius
        """ Um atributo não precisa vir necessariamente de
        um parâmetro. Ex.:"""
        self.area = radius * radius * self.pi
        
    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(30)
my_circle.pi
my_circle.radius # 30

my_circle.area

##############################################

class Circle():
    
    # CLASS OBJECT ATTRIBUTE:
    pi = 3.14
    
    def __init__(self, radius=1):
        
        self.radius = radius
        """ É possível referenciar com o nome da classe (Circle),
        ao invés de self. Ex.:"""
        self.area = radius * radius * Circle.pi
        
    # METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(30)
my_circle.area

###
### HERANÇA
###

##############################################

class Animal():
    
    def __init__(self):
        print("ANIMAL CRIADO")
    
    def who_am_i(self):
        print("I am an animal")
        
    def eat(self):
        print("I am eating")

myanimal = Animal()

myanimal.eat()

myanimal.who_am_i()


##############################################

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Cachorro Criado")

mydog = Dog()

mydog.eat()
mydog.who_am_i()

###
### Sobrescrevendo métodos
###

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Cachorro Criado")
    
    def who_am_i(self):
        print("I am a dog")

mydog = Dog()

mydog.eat()

mydog.who_am_i()

###
### Adicionando novos métodos
###

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Cachorro Criado")
    
    def eat(self):
        print("I am a dog eating")
    
    def bark(self):
        print("WOOF!")

mydog = Dog()

mydog.eat()

mydog.who_am_i()

mydog.bark()

###
### POLIMORFISMO
###

class Dog():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " diz au au!"
        #print(self.name + " diz au au!")

class Cat():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " diz miau!"
        #print(self.name + " diz miau!")
        

niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

# Mostrando Polimorfismo:
for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))

# Mostrando o Polimorfismo de outra forma:
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

###
### Classes abstratas
### (não precisa criar instância)

class Animal():
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("A subclasse precisa implementar esse método abstrato")

myanimal = Animal('fred')

myanimal.speak()

class Dog(Animal):
    
    def speak(self):
        return self.name + " fala au au!"

class Cat(Animal):
    
    def speak(self):
        return self.name + " fala miau!"

fido = Dog("Fido")
isis = Cat("Isis")

print(fido.speak())
print(isis.speak())

###
### Métodos especiais
###

mylist = [1,2,3]
len(mylist)
print(mylist)

class Sample():
    pass

mysample = Sample()

len(mysample) # erro
print(mysample) # erro? localização na memória

class Book():
    
    def __init__(self, title, author, pages):
        
        self.title = title
        self.author = author
        self.pages = pages

b = Book('Python rocks', 'Jose', 200)
print(b) # erro? localização na memória
str(b) # erro? localização na memória

#############################################################################

class Book():
    
    def __init__(self, title, author, pages):
        
        self.title = title
        self.author = author
        self.pages = pages
    ## print() e str() ####################################
    def __str__(self):
        return f"{self.title} escrito por {self.author}"
    ## len() ##############################################
    def __len__(self):
        return self.pages
    ## del ################################################
    def __del__(self):
        print("Um objeto de livro foi deletado.")

#################################################
b = Book('Python rocks', 'Jose', 200)
#################################################
print(b) # Python rocks escrito por Jose
str(b) # Python rocks escrito por Jose
#################################################
len(b) # 200
#################################################
b
del b # Um objeto de livro foi deletado.
b
#################################################

from colorama import init

init()

from colorama import Fore

print(Fore.RED + "some red text")

################################################################
# Error Handling
################################################################

"""
try:
    Esse é o bloco que é tentando executar (pode
    levar a erro).
except:
    Bloco de código que será executado no caso de
    existir um erro no bloco try.
finally:
    Blocode código final que será executado,
    independentemente de erro.

"""

def add(n1,n2):
    print(n1+n2)


#add(10,20)

number1 = 10
number2 = input('Por favor escreva um número: ')
add(number1, number2)
print("Alguma coisa aconteceu") # não executa se tem erro antes

#################################################################

try:
    # QUEREMOS TENTAR ESSE CÓDIGO
    # NO ENTANTO, PODE HAVER ERRO
    result = 10 + 10
except:
    print("Ei... parece que você não está adicionando corretamente!")

result

#################################################################

try:
    # QUEREMOS TENTAR ESSE CÓDIGO
    # NO ENTANTO, PODE HAVER ERRO
    result = 10 + '10'
except:
    print("Ei... parece que você não está adicionando corretamente!")

#################################################################

try:
    # QUEREMOS TENTAR ESSE CÓDIGO
    # NO ENTANTO, PODE HAVER ERRO
    result = 10 + '10'
except:
    print("Ei... parece que você não está adicionando corretamente!")
else:
    print("A adição deu certo!!")
    print(result)

#################################################################

try:
    # QUEREMOS TENTAR ESSE CÓDIGO
    # NO ENTANTO, PODE HAVER ERRO
    result = 10 + 10
except:
    print("Ei... parece que você não está adicionando corretamente!")
else:
    print("A adição deu certo!!")
    print(result)

#################################################################

import sys
print(sys.path)
pasta = r'F:\Python - Cursos\Udemy - Complete Python Bootcamp'.replace("\\", "/")
sys.path.append(pasta)


try:
    f = open('testfile', 'w')
    f.write("Escreva uma linha de teste")
except TypeError:
    print("Houve um erro de tipo")
except OSError:
    print("Você tem um erro de OS")
finally:
    print("Eu sempre executo")

#################################################################

import sys
print(sys.path)
pasta = r'F:\Python - Cursos\Udemy - Complete Python Bootcamp'.replace("\\", "/")
sys.path.append(pasta)


try:
    f = open('testfile', 'w')
    f.write("Escreva uma linha de teste")
    print("escreveu")
except TypeError:
    print("Houve um erro de tipo")
except:
    print("Todas as outras exceções")
finally:
    print("Eu sempre executo")

#################################################################

try:
    f = open('testfile', 'w')
    f.write("Escreva uma linha de teste")
except:
    print("Todas as outras exceções")
finally:
    print("Eu sempre executo")

#################################################################

try:
    f = open('testfile', 'r')
    f.write("Escreva uma linha de teste")
except:
    print("Todas as outras exceções")
finally:
    print("Eu sempre executo")

#################################################################

def ask_for_int():
    try:
        result = int(input("Por favor forneça um número: "))
    except:
        print("Whoops! Esse não é um número!")
    finally:
        print("Fim do try/except/finally")

ask_for_int()

#################################################################

def ask_for_int():
    while True:
        try:
            result = int(input("Por favor forneça um número: "))
        except:
            print("Whoops! Esse não é um número!")
            continue
        else:
            print("Sim, muito obrigado!")
            break
        finally:
            print("Fim do try/except/finally")
            print("Eu sempre executo no final!")

ask_for_int()

#################################################################

def ask_for_int():
    while True:
        try:
            result = int(input("Por favor forneça um número: "))
        except:
            print("Whoops! Esse não é um número!")
            continue
        else:
            print("Sim, muito obrigado!")
            break
        finally:
            print("Vou te perguntar novamente! \n")

ask_for_int()

#################################################################

def ask_for_int():
    while True:
        try:
            result = int(input("Por favor forneça um número: "))
        except:
            print("Whoops! Esse não é um número!")
            continue
        else:
            print("Sim, muito obrigado!")
            break

ask_for_int()

###
### Excercícios de Erros
###

#################################################################

for i in ['a', 'b', 'c']:
    print(i**2) # TypeError

###

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("Tipo errado!!! Se liga!!!")

###

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print("Erro geral!!! Se liga!!!")

#################################################################

x = 5
y = 0
z = x / y

###

try:
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError:
    print("Nunca, jamais e em tempo algum dividirás por zero!!!")

###

try:
    x = 5
    y = 0
    z = x / y
except:
    print("Erro na conta!!!")

###

try:
    x = 5
    y = 0
    z = x / y
except:
    print("Erro na conta!!!")
finally:
    print("Finalizado")

#################################################################

def ask():
    
    while True:
        try:
            n = int(input("Digite um número: "))
        except:
            print("Por favor, tente novamente! \n")
            continue
        else:
            break
    print("Seu número ao quadrado é:")
    print(n**2)

ask()

#################################################################

# Mesma coisa que usar o break:

def ask():
    
    # Esperando por uma resposta correta
    esperando = True
    while esperando:
        try:
            n = int(input("Digite um número: "))
        except:
            print("Por favor, tente novamente! \n")
            continue
        else:
            esperando = False
    print("Seu número ao quadrado é:")
    print(n**2)

ask()

#################################################################

"""
Unit testing, Pylint
Modificações. Fazer testes para assegurar que o código antigo ainda
roda.

pylint:
    biblioteca que olha para o seu código e reporta possíveis erros.
unittest:
    essa biblioteca embutida possibilitará testar seus próprios
    programas e checar se você está tendo os outputs corretos.

"""

###
### Módulos
###


"""
Módulos são apenas scripts .py que você chama a partir de
outro script .py.
Pacotes são coleções de módulos.

"""


"""
if __name__ == "__main__"

Algumas vezes, quando você está importando de um módulo,
você gostaria de saber se uma função módulo está sendo usada
com import, ou se está usando o arquivo original .py daquele
módulo.


"""

"""
Seção 12: Python Decorators

Decoradores possibilitam você 'decorar' uma função.

Temos uma função e queremos adicionar funcionalidades.

Decoradores: facilita se quisermos tirar aquela nova funcionalidade
que adicionamos.
Decoradores: permitem que você coloque funcionalidades extras
em uma função existente.
Usa o operador @ e são colocados no topo da função original.
Se você não quer mais a funcionalidade extra, basta deletar
aquela linha com o @.


"""

def func():
    return 1

func # retorna a representação da função

func() # executa a função

def hello():
    return "Hello!"

hello # retorna a representação da função

hello() # executa a função

greet = hello # faz uma cópia da função

greet() # executa a função copiada

hello() # executa a função original

del hello # deleta a função original

hello() # não pode ser mais executado

greet() # continua sendo executado, pois continua
# apontando para aquela função original

def hello(name='Jose'):
    print('A função hello() foi executada!')
    
    def greet():
        return '\t Essa é a função greet() de dentro de hello()!'
    
    def welcome():
        return '\t Esse é welcome() de dentro de hello()!'
    
    print(greet())
    print(welcome())
    print('Esse é o fim da função hello()!')

hello()

"""
Como greet() e welcome() são definidos dentro da função
hello(), só podemos executar greet() e welcome() dentro
de hello().
Se tentarmos executar greet() ou welcome() fora
de hello(), fala que não foi definido.
"""

welcome()

"""
No entanto, podemos executar greet() ou welcome()
caso hello() retorne uma função:

"""

def hello(name='Pedro'):
    print('A função hello() foi executada!')
    
    def greet():
        return '\t Essa é a função greet() de dentro de hello()!'
    
    def welcome():
        return '\t Esse é welcome() de dentro de hello()!'
    
    print("Eu vou retornar uma função!!")
    
    if name == 'Pedro':
        return greet
    else:
        return welcome

hello()

my_new_func = hello('Pedro')

my_new_func()
print(my_new_func())

def cool():
    
    def super_cool():
        return 'I am very cool!'
    
    return super_cool
    
some_func = cool()

some_func # a função
some_func() # executa a função

#####################################################

def hello():
    return 'Olá Pedro!'

def other(some_def_func): # passa uma função como argumento
    print('Outro código roda aqui!')
    print(some_def_func())

hello # a função hello

hello() # executa a função hello

other(hello) # passando a função hello como argumento

#######################################################
#######################################################
#######################################################

def new_decorator(original_func):
    
    def wrap_func(): # funcionalidade extra que queremos decorar a original_function
        
        print('Algum código extra, antes da função original')
        
        original_func()
        
        print('Algum código extra, depois da função original')
    
    return wrap_func

def func_needs_decorator():
    print("Eu quero ser decorado!")

func_needs_decorator()

###

decorated_func = new_decorator(func_needs_decorator)

decorated_func()

###

@new_decorator # a função abaixo está sendo passada com oargumento da função new_decorator
def func_needs_decorator():
    print("Eu qero ser decorado!")

func_needs_decorator()

###

#@new_decorator # a função abaixo está sendo passada com oargumento da função new_decorator
def func_needs_decorator():
    print("Eu qero ser decorado!")

func_needs_decorator()

#######################################################
#######################################################
#######################################################

# -X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
def novo_decorador(func_input):
    
    def func_envoltório(): # funcionalidade extra que queremos decorar a original_function
        
        print('\n Código extra ANTES da função original')
        
        func_input()
        
        print('\n Código extra DEPOIS da função original')
    
    return func_envoltório
# -X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
def func_precisa_decorador():
    print("\nEU QUERO SER DECORADO !!!")
# -X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
    
func_precisa_decorador()

func_decorada = novo_decorador(func_precisa_decorador)
func_decorada()

###############################

@novo_decorador # a função abaixo está sendo passada com oargumento da função new_decorator
def func_precisa_decorador():
    print("\nEU QUERO SER DECORADO !!!")

func_precisa_decorador()

#######################################################
#######################################################
#######################################################

"""
FUNÇÕES GERADORAS E ITERADORES

Funções geradores nos permitem escrever uma função que
pode retornar um valor e então mais tarde retomar
para pegar onde ela deixou.
Uma função geradora permite gerar uma sequência de
valores ao longo do tempo.
A principal diferença na sintaxe é o uso de yield
na definição.
Quando uma função geradora é compilada, ela se torna
um objeto que suporta um protocolo de iteração.
Isso significa que quando elas são chamadas no seu
código elas não precisam de fato retornar um valor
e então sair.
Funções geradoras vão suspender automaticamente e
retomar sua execução e marcar o último ponto da
geração do valor.
A vantagem é que ao invés de ter que computar uma
série inteira de valores do início, o gerador computa
um valor e espera até que o próximo valor seja chamado.
Por exemplo, a função range() não produz uma lista
na memória para todos os valores do início ao fim.
Ao contrário, ela mantém registro do último número e do
tamanho do passo, para fornecer um fluxo de números.
Se o usuário precisa de uma lista, ele tem que transformar
o gerador em uma lista com list(range(0,10)).
"""

# Forma que consome muita memória:

def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

create_cubes(10)

for x in create_cubes(10):
    print(x)

###################################################
# Forma que consome menos memória:

def create_cubes(n):
    for x in range(n):
        yield x**3 # não criou a lista, mais eficiente no uso da memória

create_cubes(10) # objeto generator. Funciona que nem o range()

list(create_cubes(10))

for x in create_cubes(100):
    print(x)

##################################################

def gen_fibon(n): # fibonacci
    
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b

for number in gen_fibon(10):
    print(number)

##################################################

def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()

g

#next(g)

print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # StopIteration (todos os valores foram fornecidos)

##################################################
##################################################

s = 'hello' # string não iterável

for letter in s:
    print(letter)

next(s) # 'str' object is not an iterator

##################################################
# Criand0 uma string iterável
# (Como converter um objeto iterável num iterador)

s_iter = iter(s) # string iterável

next(s_iter) # h
next(s_iter) # e
next(s_iter) # l
next(s_iter) # l
next(s_iter) # o
next(s_iter) # StopIteration

#################################################
#################################################
#################################################

###
### Counter
###

from collections import Counter

l = [1,1,1,1,1,1,12,2,2,2,2,3,3,3,3,4,4,4,5,5,5,5]

Counter(l) # conta o número de ocorrências de cada elemento

s = 'aaaasssvvsvsbababadsdffffg'
Counter(s)

s = 'How may times each word show up in this setence word word show up up'

words = s.split()
Counter(words)

c = Counter(words)

c.most_common(2) # tupla com as duas palavras mais comuns
c.most_common(3) # tupla com as três palavras mais comuns

sum(c.values()) # total todas as contagens
c.clear() # reseta a contagem
list(c) # lista elementos únicos
set(c) # converte para um set
dict(c) # converte para um dicionário normal
c.items() # converte para uma lista com pares (elemento, contagem)
Counter(dict(list_of_pairs)) # converte de uma lista de pares (elemento, contagem)
c.most_common()[:-n-1:-1] # n elementos menos comuns
c += Counter() # remove contagens zero ou negativo

###
### defaultdict
###
"""
Um dicionário padrão nunca fará raise KeyError.
Qualquer key que não existe faz o valor retornado
por default da fábrica.
"""
from collections import defaultdict

d = {'k1':1}

d['k1']

d['k2'] # KeyError: 'k2'

d = defaultdict(object)

d['one']

for item in d:
    print(item) # one

d = defaultdict(lambda :0) # sempre retorna zero (se não for atribuído outro valor)
d['one']
d['two'] = 2

d

###
### OrderedDict
###

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

d

for k, v in d.items():
    print(k,v)

############################################

from collections import OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k, v in d.items():
    print(k,v)

d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print(d1 == d2) # True

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1 == d2) # False

###
### NamedTuple
###

t = (1,2,3)
t[0]

from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2, breed='Lab', name='Sammy')
sam

sam.age
sam[0]

Cat = namedtuple('Cat', 'fur claws name')
c = Cat(fur='Fuzzy', claws=False, name='Kitty')
c

c.name
c[2]
c[1]

############################################

###
### datetime
###

import datetime

t = datetime.time(5, 25, 1)
print(t)

t.hour
t.minute
t.microsecond

datetime.time.min

print(datetime.time.min)
print(datetime.time.max)

print(datetime.time.resolution)

# datas

today = datetime.date.today()
print(today)

today.timetuple()

today.year
today.month
today.day

datetime.date.min
print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)
datetime.date(1,1,1)

d1 = datetime.date(2015,3,11)
print(d1)

d2 = d1.replace(year=1990)
d2

d1
d2

d1 - d2 # diferenças em dias

datetime.timedelta(9131)

###
### Python Debugger - pdb
###

import pdb

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

#pdb.set_trace()

x

result2 = y + x
print(result2)

###
### timeit
###

import timeit

'0-1-2-3-...-99'

"-".join(str(n) for n in range(100))

timeit.timeit( '-'.join(str(n) for n in range(100)), number=10000)

timeit.timeit( '-'.join([str(n) for n in range(100)]), number=10000)

timeit.timeit('-'.join(map(str,range(100))), number=10000)

'-'.join(map(str,range(100)))

###
### Regular Expressions - re
###

import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, but no the other term'

re.search('hello', 'hello, world!')

for pattern in patterns:
    print(f"Procurando pelo padrão {pattern} em {patterns}")
    
    # Check for match
    if re.search(pattern, text):
        print("\n")
        print("Match foi encontrado. \n")
    else:
        print("\n")
        print("Nenhum match foi encontrado. \n")

re.search('h', 'w')
print(re.search('h', 'w'))

##################################################

match = re.search(patterns[0], text)
type(match)

match.start() # início do match

match.end() # fim do match

##################################################

split_term = '@'
phrase = 'What is your email, is it hello@gmail.com?'

re.split(split_term, phrase)

#########################

'hello world'.split()

########################

re.findall('match', 'Here is one match, here is another match')

#######################

def multi_re_find(patterns, phrase):
    '''
    Takes in a List of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print(f'Searching the phrase using the re check: {pattern}')
        print(re.findall(pattern, phrase))
        print('\n')

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns = [ 'sd*', # s followed by zero or more d's
                 'sd+', # s followed by one or more d's
                 'sd?', # s followed by zero or one d's
                 'sd{3}', # s followed by three d's
                 'sd{2,3}' # s followed by two to three d's
        ]

multi_re_find(test_patterns, test_phrase)

#######################

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['[sd]', # either s or d
                 's[sd]'] # s followed by one or more s or d

multi_re_find(test_patterns, test_phrase)

#######################

test_phrase = 'This is a string! But it has punctutation. How can we remove it?'

re.findall('[^!.? ]+', test_phrase)

#######################

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'
test_patterns = ['[a-z]+', # sequences of lower case letter
                 '[A-Z]+', # sequences of upper case letter
                 '[a-zA-Z]+', # sequences of lower or upper case letter
                 '[A-Z][a-z]' # one upper case letter followed by lower case letters
        ]

multi_re_find(test_patterns, test_phrase)

#######################

test_phrase = 'This is string with some numbers 1233 and a symbol #hashtag'
test_patterns = [r'\d+', # sequence of digites
        r'\D+', # sequence of non-digits
        r'\s+', # sequence of whitespace
        r'\S+', # sequence of non-whitespace
        r'\w+', # caracteres alfanuméricos
        r'\W+', # caracteres não alfanuméricos
        ]

multi_re_find(test_patterns, test_phrase)

#######################

###
### StringIO
###

#import StringIO

#######################





















###
### 
###
