# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 22:13:54 2020

@author: pedro
https://www.youtube.com/watch?v=k9TUPpGqYTo
"""

##############################
###### EXEMPLO 01 ############
##############################
""" string em várias linhas """
mensagem = """Esta é uma
string com várias linhas """
print(mensagem)

##############################
###### EXEMPLO 02 ############
##############################
""" slicing """
mensagem = "Hello World"
print(len(mensagem))
print(mensagem[0])
print(mensagem[10])
""" primeiro índice inclusivo,
segundo índice exclusivo"""
print(mensagem[0:5])
print(mensagem[:5])
print(mensagem[6:])
print(mensagem.lower())
print(mensagem.upper())

##############################
###### EXEMPLO 03 ############
##############################
""" número de ocorrências """
mensagem = "Hello World"
print(mensagem.count('Hello'))
print(mensagem.count('l'))

##############################
###### EXEMPLO 04 ############
##############################
""" encontra posição """
mensagem = "Hello World"
print(mensagem.find('World'))
print(mensagem.find('Universe'))

##############################
###### EXEMPLO 05 ############
##############################
""" substituição """
mensagem = "Hello World"
print(mensagem.replace('World', 'Universe'))

mensagem = mensagem.replace('World', 'Universe')
print(mensagem)
##############################
###### EXEMPLO 06 ############
##############################
"""  """
saudacao = "Hello"
nome = 'Michael'

mensagem = saudacao + ', ' + nome
print(mensagem)

mensagem = '{}, {}. Welcome!'.format(saudacao, nome)
print(mensagem)


##############################
###### EXEMPLO 07 ############
##############################
""" f strings """
saudacao = "Hello"
nome = 'Michael'

mensagem = f'{saudacao}, {nome}. Welcome!'
print(mensagem)

mensagem = f'{saudacao}, {nome.upper()}. Welcome!'
print(mensagem)

##############################
###### EXEMPLO 08 ############
##############################
""" não tá no vídeo """

mensagem = "Hello World"
print(mensagem.find('World'))

posicao = mensagem.find('World')
tamanho = len(mensagem)
restante = tamanho - posicao

print(mensagem[posicao:tamanho])

