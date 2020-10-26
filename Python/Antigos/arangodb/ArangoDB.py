
from pyArango.connection import *

conn = Connection(username="root", password=1234)

conn

conn_errado1 = Connection(username="root", password=1235)

Connection(username="root", password=1235)

def db_conecta(usuario, senha):
    
    try:
        conn = Connection(username=usuario, password=senha)
    except NameError:
            print(f"Função Connection, do módulo pyArango, não importada")
    except ConnectionError:
        print(f"Acesso não autorizado. Possíveis erros: 1) Usuário ou senha incorretos; 2) Servidor não inicializado")
    else:
        print(f"Conexão realizada com sucesso!")
        return conn

conn = db_conecta('root', '1234')


conn = db_conecta('root', '1234')
db = conn["Politica"]

db["Pessoas"]

aql = "FOR c IN Pessoas LIMIT 6 RETURN c"
queryResult = db.AQLQuery(aql, rawResults=False)
document = queryResult[1]
print(queryResult)

len(queryResult)

print(queryResult[0]['Nome'])
print(queryResult[1]['Nome'])
print(queryResult[2]['Nome'])
print(queryResult[3]['Nome'])
print(queryResult[4]['Nome'])

def consulta(n):
    aql = f"""
        FOR c IN Pessoas
        LIMIT {n}
        RETURN c
        """
    queryResult = db.AQLQuery(aql, rawResults=False)
    for x in queryResult:
        print(x['Nome'])
    

consulta(10)


doc1 = db["Pessoas"].createDocument()
doc1["_key"] = "Zeh_Maneh"
doc1["_id"] = "Pessoas/Zeh_Maneh"
doc1["Nome"] = "Zeh Maneh da Silva"
doc1.save()

doc2 = db["Pessoas"].createDocument()
doc2["_key"] = "Joao_Bobo"
doc2["Nome"] = "João Bobo de Medeiros"
doc2.save()

doc3 = db["Pessoas"].createDocument()
doc3["_key"] = "Joao_Bobo"
doc3["Nome"] = "Nome repetido"
doc3.save()

doc3 = db["colecao_inexistente"].createDocument()

doc4 = db["Pessoas"].createDocument()
doc4["_key"] = "Joao_Bobo"
doc4["chave_inexistente"] = "Nome repetido"
doc4.save()

doc5 = db["Pessoas"].createDocument()
doc5["Nome"] = "Zeh Maneh da Silva"
doc5.save()

doc5 = db["Pessoas"].createDocument()
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










