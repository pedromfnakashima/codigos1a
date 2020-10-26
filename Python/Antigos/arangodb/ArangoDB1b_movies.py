import pandas as pd
from pyArango.connection import *
movies = pd.read_csv('http://bit.ly/imdbratings')

conn = Connection(username='root', password='1234')

db_filmes = conn["Filmes"]

col_filmes = db_filmes.createCollection(name="filmesAmericanos")

db_filmes['filmesAmericanos']

doc1 = db_filmes["filmesAmericanos"].createDocument()
doc1["_key"] = "um_filme_ruim"
doc1["Nome"] = "O pior filme da minha vida"
doc1["Ano"] = 2019
doc1.save()










