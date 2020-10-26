
from pyArango.connection import *

def conecta(usuario, senha, base):
    
    def conecta_server(usuario, senha):
        try:
            conn = Connection(username=usuario, password=senha)
        except NameError:
                print(f"Função Connection, do módulo pyArango, não importada")
        except ConnectionError:
            print(f"Acesso não autorizado. Possíveis erros: 1) Usuário ou senha incorretos; 2) Servidor não inicializado")
        else:
            print(f"Conexão com o servidor realizada com sucesso!")
            return conn
    
    conn = conecta_server(usuario, senha)
    
    def conecta_bd(base):
        try:
            db_col = conn[base]
        except KeyError:
            print(f"Coleção {base} inexistente.")
        else:
            print(f"Conectado ao BD: {base}.")
            return db_col
    
    bd = conecta_bd(base)
    return bd

bd_politica = conecta('root', 1234, 'Politica')
aql = "FOR c IN Pessoas LIMIT 6 RETURN c"
pesquisa = bd_politica.AQLQuery(aql, rawResults=False)




###############################################################################
###############################################################################
###############################################################################


conn = Connection(username="root", password=1234)
db = conn.createDatabase(name="school")
db = conn["school"]
db
studentsCollection = db.createCollection(name="Students")
db["Students"]

students = [('Oscar', 'Wilde', 3.5),
            ('Thomas', 'Hobbes', 3.2),
            ('Mark', 'Twain', 3.0),
            ('Kate', 'Chopin', 3.8),
            ('Fyodor', 'Dostoevsky', 3.1),
            ('Jane', 'Austen',3.4),
            ('Mary', 'Wollstonecraft', 3.7),
            ('Percy', 'Shelley', 3.5),
            ('William', 'Faulkner', 3.8),
            ('Charlotte', 'Bronte', 3.0)]

students
type(students)
len(students)

for (first, last, gpa) in students:
    doc = studentsCollection.createDocument()
    doc['name'] = "%s %s" % (first, last)
    doc['gpa'] = gpa
    doc['year'] = 2017
    doc._key = ''.join([first, last]).lower()
    doc.save()


def report_gpa(document):
    print("Student: %s" % document['name'])
    print("GPA:     %s" % document['gpa'])
kate = studentsCollection['katechopin']
report_gpa(kate)




###############################################################################
###############################################################################
###############################################################################



















document = pesquisa[1]
print(pesquisa)
len(pesquisa)
print(pesquisa[0]['Nome'])
print(pesquisa[1]['Nome'])
print(pesquisa[2]['Nome'])
print(pesquisa[3]['Nome'])
print(pesquisa[4]['Nome'])

def lista_dep(n, bancoDados):
    aql = f"""
        FOR c IN Pessoas
        LIMIT {n}
        RETURN c
        """
    lista = [] 
    pesquisa = bancoDados.AQLQuery(aql, rawResults=False)
    for x in pesquisa:
        lista.append(x['Nome'])
    return lista

lista_dep(26, bd_politica)
###############################################################################
###############################################################################
###############################################################################

doc1
print(doc1)
doc1["_key"]

type(doc1)
type(doc1["_key"])


doc2 = bd_politica["Pessoas"].createDocument()







doc1 = bd_politica["Pessoas"].createDocument()
doc1["_key"] = "Zeh_Maneh"
doc1["Nome"] = "Zeh Maneh da Silva"
doc1.save()

doc2 = bd_politica["Pessoas"].createDocument()
doc2["_key"] = "Joao_Bobo"
doc2["Nome"] = "João Bobo de Medeiros"
doc2.save()

doc3 = bd_politica["Pessoas"].createDocument()
doc3["_key"] = "Joao_Bobo"
doc3["Nome"] = "Nome repetido"
doc3.save()

doc3 = bd_politica["colecao_inexistente"].createDocument()

doc4 = bd_politica["Pessoas"].createDocument()
doc4["_key"] = "Joao_Bobo"
doc4["chave_inexistente"] = "Nome repetido"
doc4.save()

doc5 = bd_politica["Pessoas"].createDocument()
doc5["Nome"] = "Zeh Maneh da Silva"
doc5.save()

doc5 = bd_politica["Pessoas"].createDocument()
doc5["Nome"] = "Ronaldo Nazário"
doc5.save()


class DbArango():
    
    def insertDoc(self, colecao, campo, valor_inserido):
        try:
            doc = db["Pessoas"].createDocument()
        except KeyError:
            print(f"A coleção {colecao} não existe")
        doc[campo] = valor_inserido
        try:
            doc.save()
        except CreationError:
            print(f"A variável _key = {campo} já existe.")










>>> doc1 = studentsCollection.createDocument()
>>> doc1["name"] = "John Smith"
>>> doc1
ArangoDoc 'None': {'name': 'John Smith'}
>>> doc2 = studentsCollection.createDocument()
>>> doc2["firstname"] = "Emily"
>>> doc2["lastname"] = "Bronte"
>>> doc2
ArangoDoc 'None': {'firstname': 'Emily', 'lastname': 'Bronte'}





def consulta_pessoas(document):
    print(f"Nome: {document['Nome']}")

consulta_pessoas('Amarildo_Cruz')



>>> def report_gpa(document):
...    print("Student: %s" % document['name'])
...    print("GPA:     %s" % document['gpa'])
>>> kate = studentsCollection['katechopin']
>>> report_gpa(kate)










