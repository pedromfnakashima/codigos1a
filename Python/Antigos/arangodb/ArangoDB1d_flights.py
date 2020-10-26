import pandas as pd
from pathlib import Path
caminho = Path(r'C:\Users\salj\Desktop\Pedro Nakashima\Códigos\arangodb\airports.csv')
from pyArango.connection import *

conn = Connection(username='root', password='1234')

db_voos_1 = conn.createDatabase(name="db_voos_1")

db_northwind_1 = conn.createDatabase(name="db_northwind_1")




# arangoimp --file "C:\Users\salj\Desktop\Pedro Nakashima\Códigos\arangodb\airports.csv" --server.database db_voos_1 --collection airports --create-collection true --type csv
# arangoimp --file "C:\Users\salj\Desktop\Pedro Nakashima\Códigos\arangodb\flights.csv" --server.database db_voos_1 --create-collection-type edge --collection flights --create-collection true --type csv


























