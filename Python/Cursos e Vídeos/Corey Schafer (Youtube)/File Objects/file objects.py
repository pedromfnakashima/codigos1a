# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:01:50 2020

@author: pedro
"""
globals().clear()

""" Muda o diretório """
import os
print(os.getcwd())
os.chdir('D:\Códigos, Dados, Documentação e Cheat Sheets\Cursos e Livros\Corey Schafer - Youtube\File Objects')
print(os.getcwd())

##############################
###### EXEMPLO 01 ############
##############################
""" 
sem context manager
"""

f = open('test.txt', 'r')
print(f.name)
print(f.mode)

f.close()

##############################
###### EXEMPLO 02 ############
##############################
""" 
com context manager
(não precisa fechar)
"""

with open('test.txt', 'r') as f:
    pass

print(f.closed) # True
print(f.read()) # erro


##############################
###### EXEMPLO 03 ############
##############################
""" Lê o arquivo todo
"""
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)


##############################
###### EXEMPLO 04 ############
##############################
""" lê algumas linhas
"""
with open('test.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)


##############################
###### EXEMPLO 05 ############
##############################
""" lê a primeira linha
"""
with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents)


##############################
###### EXEMPLO 06 ############
##############################
""" lê a primeira e a segunda
linhas
"""
with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents)
    
    f_contents = f.readline()
    print(f_contents)



##############################
###### EXEMPLO 07 ############
##############################
""" lê a primeira e a segunda
linhas;
com final não sendo uma linha
extra (\n)
f.readline funciona como um
iterador
"""
with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='')
    
    f_contents = f.readline()
    print(f_contents)

##############################
###### EXEMPLO 08 ############
##############################
""" lê todas as linhas
"""
with open('test.txt', 'r') as f:
    
    for line in f:
        print(line, end='')


##############################
###### EXEMPLO 09 ############
##############################
""" 
"""
with open('test.txt', 'r') as f:
    
    f_contents = f.read(100) # primeiros 100 caracteres
    print(f_contents, end='')

    f_contents = f.read(50) # 100 caracteres seguintes
    print(f_contents, end='')

##############################
###### EXEMPLO 10 ############
##############################
""" p/ ler um arquivo grande
que não sabe o tamanho
"""
with open('test.txt', 'r') as f:
    
    size_to_read = 100
    
    f_contents = f.read(size_to_read) # primeiros 100 caracteres
    
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)

##############################
###### EXEMPLO 11 ############
##############################
""" 
"""
with open('test.txt', 'r') as f:
    
    size_to_read = 10
    
    f_contents = f.read(size_to_read) # primeiros 100 caracteres
    
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)


##############################
###### EXEMPLO 12 ############
##############################
""" 
"""
with open('test.txt', 'r') as f:
    
    size_to_read = 10
    
    f_contents = f.read(size_to_read) # primeiros 100 caracteres
    print(f_contents, end='')
    
    f.seek(0) # faz voltar para o início do arquivo
    
    f_contents = f.read(size_to_read) # primeiros 100 caracteres
    print(f_contents)
    

##############################
###### EXEMPLO 13 ############
##############################
""" write
só cria o arquivo
pass: diz p/ não fazer nada
"""
with open('test2.txt', 'w') as f:
    
    pass

##############################
###### EXEMPLO 14 ############
##############################
""" write
sobrescreve o arquivo se ele
já existe
"""
with open('test2.txt', 'w') as f:
    
    f.write('Test')

##############################
###### EXEMPLO 15 ############
##############################
""" write
sobrescreve o arquivo se ele
já existe
escreve 2 vezes Test
"""
with open('test2.txt', 'w') as f:
    
    f.write('Test')
    f.write('Test')

##############################
###### EXEMPLO 16 ############
##############################
""" write
sobrescreve o arquivo se ele
já existe
f.seek(0) faz ir p/ o início
o segundo Test sobrescreveu
o primeiro
"""
with open('test2.txt', 'w') as f:
    
    f.write('Test')
    f.seek(0)
    f.write('Test')

##############################
###### EXEMPLO 17 ############
##############################
""" write
sobrescreve o arquivo se ele
já existe
f.seek(0) faz ir p/ o início
muda a primeira letra para R.
Apenas sobrescreveu a primeira
letra
"""
with open('test2.txt', 'w') as f:
    
    f.write('Test')
    f.seek(0)
    f.write('R')

##############################
###### EXEMPLO 18 ############
##############################
""" lê um arquivo
copia em outro
"""
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

##############################
###### EXEMPLO 19 ############
##############################
""" lê um arquivo
copia em outro
pedaço por pedaço
"""
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

##############################
###### EXEMPLO 20 ############
##############################
""" abrir as primeiras N linhas e
colocar cada linha em um elemento de
uma lista
(não está no vídeo)
(retirado do stackoverflow:
 https://stackoverflow.com/questions/1767513/read-first-n-lines-of-a-file-in-python)
"""

with open("test.txt", 'r') as myfile:
    N = 3
    head = [next(myfile) for x in range(N)]

print(head)
print(head[0])
print(head[1])




