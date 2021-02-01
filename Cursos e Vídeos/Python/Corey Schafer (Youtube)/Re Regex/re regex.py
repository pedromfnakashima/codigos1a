# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:28:17 2020

@author: pedro
"""
#############################
##### CONFIGURAÇÃO GERAL ####
#############################
globals().clear()
""" Mudar diretório """
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    print('\nLogado de casa')
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('\nLogado da salj-alems')
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados' / 'Cursos e Livros' / 'Corey Schafer - Youtube' / 'Re Regex'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

#############################
#############################
#############################

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

'''

sentence = 'Start a sentence and then bring it to an end'

##############################
######### EXEMPLO 01 #########
##############################
"""  """
import re

#padrao = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d', re.I)
#padrao = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d', re.I)
#padrao = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d', re.I)
#padrao = re.compile(r'[^b]at', re.I)
#padrao = re.compile(r'\d{3}.\d{3}.\d{4}', re.I)
#padrao = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*', re.I)
#padrao = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*', re.I)
#padrao = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
padrao = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = padrao.finditer(text_to_search)

for match in matches:
    print(match)

##############################
######### EXEMPLO 02 #########
##############################
"""  """
import re

#padrao = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d', re.I)
padrao = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d', re.I)

with open('data.txt', 'r') as f:
    conteudo = f.read()
    
    matches = padrao.finditer(conteudo)
    
    for match in matches:
        print(match)



##############################
######### EXEMPLO 03 #########
##############################
"""  """
import re

#padrao = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d', re.I)
#padrao = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d', re.I)
#padrao = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d', re.I)
#padrao = re.compile(r'[^b]at', re.I)
#padrao = re.compile(r'\d{3}.\d{3}.\d{4}', re.I)
#padrao = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*', re.I)
#padrao = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*', re.I)
#padrao = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
padrao = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = padrao.finditer(text_to_search)

for match in matches:
    print(match.group(0))


##############################
######### EXEMPLO 04 #########
##############################
"""  """
import re

#padrao = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d', re.I)
#padrao = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d', re.I)
#padrao = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d', re.I)
#padrao = re.compile(r'[^b]at', re.I)
#padrao = re.compile(r'\d{3}.\d{3}.\d{4}', re.I)
#padrao = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*', re.I)
#padrao = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*', re.I)
#padrao = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
padrao = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = padrao.finditer(text_to_search)

for match in matches:
    print(match.group(2))

##############################
######### EXEMPLO 05 #########
##############################
""" padrao.sub """
import re

#padrao = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d', re.I)
#padrao = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d', re.I)
#padrao = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d', re.I)
#padrao = re.compile(r'[^b]at', re.I)
#padrao = re.compile(r'\d{3}.\d{3}.\d{4}', re.I)
#padrao = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*', re.I)
#padrao = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*', re.I)
#padrao = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
padrao = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

texto_com_url_modificada = padrao.sub(r'\2\3', text_to_search)

print(texto_com_url_modificada)


##############################
######### EXEMPLO 06 #########
##############################
""" padrao.findall
retorna uma lista de strings
"""
import re

#padrao = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d', re.I)
#padrao = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d', re.I)
#padrao = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d', re.I)
#padrao = re.compile(r'[^b]at', re.I)
padrao = re.compile(r'\d{3}.\d{3}.\d{4}', re.I)
#padrao = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*', re.I)
#padrao = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*', re.I)
#padrao = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
#padrao = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

li_matches = padrao.findall(text_to_search)

print(li_matches)

for match in li_matches:
    print(match)

##############################
######### EXEMPLO 07 #########
##############################
""" padrao.match
NÃO retorna um iterável
Só retorna se estiver no começo"""
import re

padrao = re.compile(r'Start')

sentence = 'Start a sentence and then bring it to an end'

matches = padrao.match(sentence)

print(matches)


##############################
######### EXEMPLO 08 #########
##############################
""" matches """
import re

padrao = re.compile(r'sentence')

sentence = 'Start a sentence and then bring it to an end'

matches = padrao.match(sentence)

print(matches)
# retorna None (pq 'sentence' não tá no começo da string)


##############################
######### EXEMPLO 09 #########
##############################
""" search
retorna o primeiro match
encontrado
Retorna None se é procurado
algo que não está na string"""
import re

padrao = re.compile(r'sentence')
sentence = 'Start a sentence and then bring it to an end'
matches = padrao.search(sentence)
print(matches)
# Encontrado

padrao = re.compile(r'abcd')
sentence = 'Start a sentence and then bring it to an end'
matches = padrao.search(sentence)
print(matches)
# retorna None

##############################
######### EXEMPLO 10 #########
##############################
""" flags
podemos usar ignorecase
No padrão, colocar o parâmetro:
re.IGNORECASE ou re.I
Mesmo que o padrão estiver tudo
em minúsculo, é possível achar
ocorrências em matches em
maiúsculo.
"""

import re

padrao = re.compile(r'start', re.IGNORECASE)
sentence = 'Start a sentence and then bring it to an end'
matches = padrao.search(sentence)
print(matches)
# Encontrado

