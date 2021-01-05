# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:50:15 2020

@author: pedro
"""

import os

""" métodos """
print(dir(os))

""" wd atual """
print(os.getcwd())

""" muda diretório """
os.chdir('D:/Códigos, Dados, Documentação e Cheat Sheets/Cursos e Livros/Corey Schafer - Youtube/Os')
print(os.getcwd())

""" lista arquivos """
print(os.listdir())

""" cria nova pasta: 2 métodos
os.mkdir: p/ 1 nível
os.makedirs: p/ + de 1 nível
"""
os.mkdir('OS-Demo-1')
os.makedirs('OS-Demo-2/Sub-Dir-2')

""" deleta pasta: 2 métodos
os.rmdir: p/ 1 nível
os.removedirs: p/ + de 1 nível
"""
os.rmdir('OS-Demo-1')
os.removedirs('OS-Demo-2/Sub-Dir-2')

""" renomear arquivo ou pasta """
os.rename('test.txt', 'demo.txt')

""" informações sobre o arquivo:
Tamanho."""
print(os.stat('demo.txt'))
""" informações sobre o arquivo:
Última modificação."""
from datetime import datetime
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

""" caminhar pela árvore toda
do diretório.
Útil para fazer buscas de
arquivos."""
for dirpath, dirnames, filenames in os.walk('D:/Códigos, Dados, Documentação e Cheat Sheets/Códigos (não versionados)'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()

""" pegar variáveis de ambiente """
print(os.environ.get('HOME'))

""" Combinar paths """
file_path = os.path.join(os.getcwd(), 'test.txt')
print(file_path)

""" Combinar paths """
dir_path = 'D:\Códigos, Dados, Documentação e Cheat Sheets\codigos_versionados\Python\Cursos e Vídeos\Corey Schafer (Youtube)\OS'
file_path = os.path.join(dir_path, 'test.txt')
print(file_path)

""" pega o nome do arquivo do path """
print(os.path.basename(file_path))

""" pega o nome do diretório do path """
print(os.path.dirname(file_path))

""" pega o nome e o diretório do path, e coloca numa tupla de 2 """
print(os.path.split(file_path))

""" checa a existência de um path """
print(os.path.exists(file_path))

""" checar se é diretório ou arquivo """
print(os.path.isdir(file_path))
print(os.path.isfile(file_path))

""" separa a rota e a extensão, colocando numa tupla de 2 """
print(os.path.splitext(file_path))


