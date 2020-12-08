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




# Sucesso da meta
import re
texto = 'cnae2_grupo_cod3'
print(re.sub(r'_cod\d', "_desc", texto))















