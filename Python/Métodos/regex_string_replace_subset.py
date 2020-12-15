# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:15:35 2020

@author: pedro-salj
"""



texto = '''
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
import re

padrao = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = padrao.finditer(texto)

for match in matches:
    print(match.group(0))

'''
Meta:
Substituir "cnae2_grupo_cod3"
por "cnae2_grupo_desc"
Ou seja:
Substituir "_cod3"
por "_desc"
'''

texto = 'cnae2_grupo_cod3'
padrao = re.sub(r'https?://(www\.)?(\w+)(\.\w+)')

for match in matches:
    print(match.group(0))


# STRING REPLACE

# Sucesso da meta
import re
texto = 'cnae2_grupo_cod3'
print(re.sub(r'_cod\d', "_desc", texto))

# STRING SUBSET

# Ok
import re
texto = '1101.Cereais, leguminosas e oleaginosas'
matches = re.search('^\d+', texto)
if matches != None:
    print(matches.group(0))

# Ok
import re
texto = 'Índice geral'
matches = re.search('^\d+', texto)
if matches != None:
    print(matches.group(0))

# retorna TRUE ou FALSE

# Ok
import re
texto = '1101.Cereais, leguminosas e oleaginosas'
matched = re.match('^\d+', texto)
is_match = bool(matched)
print(is_match)

# Ok
import re
texto = 'Índice geral'
matched = re.match('^\d+', texto)
is_match = bool(matched)
print(is_match)

# case insensitive

import re
texto = 'Índice geral'
matches = re.search('^\d+', texto)
é_índice = bool(re.match('índice', texto, re.IGNORECASE))
#print(is_match)
if é_índice == True:
    print('É índice!!!!')









