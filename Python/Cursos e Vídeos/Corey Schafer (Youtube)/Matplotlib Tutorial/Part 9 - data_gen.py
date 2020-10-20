# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:14:22 2020

@author: pedro
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

import csv
import random
import time

x_value = 0
total_1 = 1000
total_2 = 1000

fieldnames = ["x_value", "total_1", "total_2"]


with open(caminho / 'Cursos e Livros' / 'Corey Schafer - Youtube' / 'Matplotlib Tutorials' / 'Part 9' /'data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open(caminho / 'Cursos e Livros' / 'Corey Schafer - Youtube' / 'Matplotlib Tutorials' / 'Part 9' /'data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }

        csv_writer.writerow(info)
        print(x_value, total_1, total_2)

        x_value += 1
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)

    time.sleep(1)