# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 18:53:53 2020

@author: pedro
"""

# https://www.youtube.com/watch?v=pd-0G0MigUA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=51


#############################
##### CONFIGURAÇÃO GERAL ####
#############################
globals().clear()
""" Mudar diretório """
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'codigos_versionados' / 'Python' / 'Cursos e Vídeos' / 'Corey Schafer (Youtube)' / 'SQLite'
os.chdir(caminho_wd)

#######################################################

import sqlite3
from employee import Employee

# conn = sqlite3.connect('employee.db')


conn = sqlite3.connect(':memory:')

c = conn.cursor()

#### Cria a tabela
c.execute("""CREATE TABLE employees (
        first text,
        last text,
        pay integer
    )""")


def insert_emp(emp):
    with conn: # não precisa mais fazer o commit
        c.execute(f"INSERT INTO employees VALUES (:first,:last,:pay)", {'first':emp.first, 'last':emp.last, 'pay':emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last':lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John','Doe',80000)
emp_2 = Employee('Jane','Doe',90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

conn.close()



















emp_1 = Employee('John','Doe',80000)
emp_2 = Employee('Jane','Doe',90000)
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)

"""
Os dois métodos abaixo são imunes a SQL injection
"""
c.execute(f"INSERT INTO employees VALUES (?,?,?)", (emp_1.first, emp_1.last, emp_1.pay))
conn.commit()
c.execute(f"INSERT INTO employees VALUES (:first,:last,:pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})
conn.commit()

c.execute("INSERT INTO employees VALUES ('Corey','Schafer', 50000)")
c.execute("INSERT INTO employees VALUES ('Mary','Schafer', 70000)")

# conn.commit()

# c.execute("SELECT * FROM employees WHERE last='Schafer'")
# c.execute("SELECT * FROM employees WHERE last='Schafer'")

"""
Os dois métodos abaixo são imunes a SQL injection
"""
c.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))
print(c.fetchall())
c.execute("SELECT * FROM employees WHERE last=:last", {'last':'Doe'})
print(c.fetchall())


# print(c.fetchone())
# print(c.fetchall())
### print(c.fetchmany(5))
### print(c.fetchall())

conn.commit()

conn.close()


























































