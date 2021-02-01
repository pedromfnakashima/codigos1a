# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:29:19 2021

@author: pedro
"""
# https://www.youtube.com/watch?v=FXlixv8Ieoc

import mysql.connector

con = mysql.connector.connect(host='localhost',database='books_db',user='root',password='admin')

if con.is_connected():
    db_info = con.get_server_info()
    print(f"Conectado ao servidor MySQL versão {db_info}.")
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print(f"Conectado ao banco de dados {linha}.")

if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada.")






