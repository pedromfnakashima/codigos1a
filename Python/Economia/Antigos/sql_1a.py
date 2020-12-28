"""
import os
from pathlib import Path
caminho = Path(r'C:\Users\salj\Desktop\Pedro Nakashima\Códigos\Sqlite\Northwind.Sqlite3.sql')
caminho
import sqlite3

conn = sqlite3.connect(caminho)
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM Categories;
""")

for linha in cursor.fetchall():
    print(linha)

"""

# https://www.youtube.com/watch?v=pd-0G0MigUA

class Employee:
    """A sample Employee class"""
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"


import sqlite3
conn = sqlite3.connect('employee.db')

c = conn.cursor()

'''
c.execute("""
CREATE TABLE employees (
first text,
last text,
pay integer
)""")
'''

#c.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 50000)")
#c.execute("INSERT INTO employees VALUES ('Mary', 'Schafer', 70000)")

#conn.commit()

c.execute("SELECT * FROM employees WHERE last='Schafer'")
#c.execute("SELECT * FROM employees WHERE last='Smith'")

#print(c.fetchone())
print(c.fetchall())

conn.commit()

conn.close()


















