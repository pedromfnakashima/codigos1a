-- Boson treinamentos

-- Listar tabela no Workbench (abrir tela de código SQL antes):

SELECT * FROM db_biblioteca.tbl_autores;
SELECT * FROM db_biblioteca.tbl_editoras;
SELECT * FROM db_biblioteca.tbl_livro;

-- Mostra os tipos de dados de cada coluna:
SHOW FIELDS FROM tbl_livro;

-- ou:
-- Informações sobre as colunas de um BD:
SHOW COLUMNS FROM tbl_editoras;

-- Informações COMPLETAS sobre as colunas de um BD:
SHOW FULL COLUMNS FROM tbl_editoras;

-- Filtragem: colunas que começam com a letra i.
SHOW COLUMNS FROM tbl_livro LIKE 'I%';

-- Filtragem: colunas com de um tipo específico:
SHOW COLUMNS FROM tbl_livro WHERE TYPE LIKE 'varchar%';

-- Atalho p/ SHOW COLUMNS FROM. DESCRIBE NÃO SUPORTA AS CLÁUSULAS WHERE E LIKE.
DESCRIBE tbl_livro;
DESC tbl_livro;

-- Altera o tipo de dados de uma coluna:
ALTER TABLE tbl_livro
MODIFY COLUMN Preco_Livro DECIMAL(10,2);



-- Comentar código SQL
-- colocar antes --

-- ################################################
-- # 07 Criar BD ##################################
-- ################################################

-- Criar novo BD:

-- CREATE DATABASE [IF NOT EXISTS] nome_BD;

-- Saber os BDs que existem no servidor:

-- SHOW DATABASES;

-- Para criar uma tabela, precisa selecionar o banco de dados antes:

-- USE nome_banco_de_dados;

USE db_Biblioteca;

-- Para visualizar o banco de dados selecionado no momento:

SELECT DATABASE();

Excluir Banco de Dados:

DROP DATABASE [IF EXISTS] nome_BD;

Mostrar as tabelas existentes no BD:

SHOW TABLES;

################################################
# 08 SQL CONSTRAINTS ###########################
################################################
https://www.youtube.com/watch?v=10Gu4XZBMdo&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=8

Principais
NOT NULL: impõe coluna não aceitar valores NULL;
UNIQUE: impede a repetição de dados na coluna;
PRIMARY KEY: 1 ou combinação de colunas que identifica de forma única cada registro em uma tabela de um banco de dados. Não pode ter valor NULL;
FOREIGN KEY: campo que aponta p/ uma chave primária em outra tabela. Ex.:   
    CONSTRAINT fk_ID_Autor FOREIGN KEY (ID_Autor) REFERENCES tbl_autores(ID_Autor)
DEFAULT: inserir valor padrão, caso nenhum seja especificado na hora da inserção.

################################################
# 09 CRIAÇÃO DE TABELAS ########################
################################################
https://www.youtube.com/watch?v=H1_3ttK2Wbw&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=9

CREATE TABLE [IF NOT EXISTS] nome_tabela (
    coluna tipo_dados constraints
)

CREATE TABLE IF NOT EXISTS tbl_Livro (
    ID_Livro smallint AUTO_INCREMENT PRIMARY KEY,
    Nome_Livro Varchar(50) NOT NULL,
    ISBN Varchar(30) NOT NULL,
    ID_Autor smallint NOT NULL,
    Data_Pub DATE NOT NULL,
    Preco_Livro decimal(10,2) NOT NULL
)

CREATE TABLE tbl_autores (
    ID_Autor SMALLINT PRIMARY KEY,
    Nome_Autor VARCHAR(50),
    Sobrenome_Autor VARCHAR(60)
);

CREATE TABLE tbl_editoras (
    ID_Editora SMALLINT PRIMARY KEY AUTO_INCREMENT,
    Nome_Editora VARCHAR(50) NOT NULL
);

CREATE TABLE Compras (
    ID_Compra SMALLINT PRIMARY KEY,
    Codigo_Produto VARCHAR(50),
    Data_Compra date,
    FOREIGN KEY (Codigo_Produto) REFERENCES Produtos(Cod_Produto)
);

######################################################
# 10  Auto incremento de valores em colunas ##########
######################################################
https://www.youtube.com/watch?v=-jWUUGiKDeI&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=10

- Ao inserir valores na tabela, não é necessário especificar o valor para a coluna de auto-incremento;
- Só é permitido usar uma coluna de auto incremento por tabela, geralmente do tipo inteiro;
- Necessita também da constraint NOT NULL (configurado automaticamente);

Definindo o valor inicial:
AUTO_INCREMENT = 100


CREATE TABLE tbl_teste_incremento (
    Codigo SMALLINT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(20) NOT NULL
) AUTO_INCREMENT = 15;

INSERT INTO tbl_teste_incremento (Nome) VALUES('Ana');
INSERT INTO tbl_teste_incremento (Nome) VALUES('Maria');
INSERT INTO tbl_teste_incremento (Nome) VALUES('Julia');
INSERT INTO tbl_teste_incremento (Nome) VALUES('Joana');

SELECT * FROM tbl_teste_incremento;

Verificar o valor atual do auto incremento:

SELECT MAX (nome_coluna)
FROM tabela;

SELECT MAX(Codigo)
FROM tbl_teste_incremento;

SELECT MAX(ID_Livro)
FROM tbl_livro;

Alterar o próximo valor no campo de auto-incremento:

ALTER TABLE tabela AUTO_INCREMENT = valor;

ALTER TABLE tbl_teste_incremento
AUTO_INCREMENT = 90;

######################################################
# 11  Tipos de dados ############
######################################################
https://www.youtube.com/watch?v=5oost838ogk&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=11

######################################################
# 12 Alterar tabelas depois de ter sido criada ############
######################################################
https://www.youtube.com/watch?v=ZTWhdNG963M&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=12

Deletar coluna:

ALTER TABLE tabela
DROP COLUMN coluna;

(antes: USE db_Biblioteca;)

ALTER TABLE tbl_Livro
DROP COLUMN ID_Autor;

Pode-se excluir uma chave primária da tabela (sem excluir a coluna em si - como a tabela só tem uma chave primária, não precisa especificar qual coluna é a chave primária):

ALTER TABLE tabela
DROP PRIMARY KEY;

Criar coluna:

ALTER TABLE tabela
ADD coluna tipo_dados constraints;

ALTER TABLE tbl_Livro
ADD ID_Autor SMALLINT NOT NULL;

Transformar a coluna ID_Autor, de tbl_Livro, em chave estrangeira:

ALTER TABLE tbl_Livro
ADD CONSTRAINT fk_ID_Autor
FOREIGN KEY (ID_Autor)
REFERENCES tbl_autores (ID_autor);

Criar coluna na tabela editora:

ALTER TABLE tbl_Livro
ADD ID_editora SMALLINT NOT NULL;

Transformar a coluna ID_editora, de tbl_Livro, em chave estrangeira:

ALTER TABLE tbl_Livro
ADD CONSTRAINT fk_ID_editora
FOREIGN KEY (ID_editora)
REFERENCES tbl_editoras (ID_editora);

Mudar o tipo de dados de uma coluna:

ALTER TABLE tbl_Livro
ALTER COLUMN ID_Autor SMALLINT;

Adicionar chave primária a uma tabela que já tem a coluna, mas não tem a chave primária definida:

ALTER TABLE nome_da_tabela
ADD PRIMARY KEY (nome_da_coluna ou nomes_das_colunas_separados_por_vírgula)

ex.:

ALTER TABLE tbl_Clientes
ADD PRIMARY KEY (ID_Cliente)

(a coluna ID_Cliente deve existir antes de ser transformada em chave primária)

Ver relacionamentos no MySql Workbench:
https://www.youtube.com/watch?v=RbKEYDtkAJI

Botão da casa (home) -> Models -> + -> Database -> Rever Engineer -> Stored Connection = Local Instance -> Next -> escolha do BD -> Next, Execute, Next, Finish

######################################################
# 13 Inserir dados em uma tabela ############
######################################################
https://www.youtube.com/watch?v=ONfaKQOyjH4&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=13

Inserir dados em uma tabela:

INSERT INTO tabela (coluna1, coluna2,...)
VALUES (valor1, valor2,...);

INSERT INTO tbl_autores (ID_Autor, Nome_Autor, Sobrenome_Autor)
VALUES (1, 'Daniel', 'Barret');

INSERT INTO tbl_autores (ID_Autor, Nome_Autor, Sobrenome_Autor)
VALUES (2, 'Gerald', 'Carter');

INSERT INTO tbl_autores (ID_Autor, Nome_Autor, Sobrenome_Autor)
VALUES (3, 'Mark', 'Sobel');

INSERT INTO tbl_autores (ID_Autor, Nome_Autor, Sobrenome_Autor)
VALUES (4, 'William', 'Stanek');

INSERT INTO tbl_autores (ID_Autor, Nome_Autor, Sobrenome_Autor)
VALUES (5, 'Richard', 'Blum');

-----

INSERT INTO tbl_editoras (Nome_Editora)
VALUES ('Prentice Hall');

INSERT INTO tbl_editoras (Nome_Editora)
VALUES ('O´Reilly');

INSERT INTO tbl_editoras (Nome_Editora)
VALUES ('Microsoft Press');

INSERT INTO tbl_editoras (Nome_Editora)
VALUES ('Willey');

-----

INSERT INTO tbl_livro (Nome_Livro, ISBN, Data_Pub, Preco_Livro, ID_Autor, ID_editora)
VALUES ('Linux Command Line and Shell Scripting', 143856969,'20091221', 68.35, 5, 4);

INSERT INTO tbl_livro (Nome_Livro, ISBN, Data_Pub, Preco_Livro, ID_Autor, ID_editora)
VALUES ('SSH, the Secure Shell', 127658789,'20091221', 58.30, 1, 2);

INSERT INTO tbl_livro (Nome_Livro, ISBN, Data_Pub, Preco_Livro, ID_Autor, ID_editora)
VALUES ('Using Samba', 123856789,'20001221', 61.45, 2, 2);

INSERT INTO tbl_livro (Nome_Livro, ISBN, Data_Pub, Preco_Livro, ID_Autor, ID_editora)
VALUES ('Fedora and Red Hat Linux', 123456789,'20101101', 62.24, 3, 1);

INSERT INTO tbl_livro (Nome_Livro, ISBN, Data_Pub, Preco_Livro, ID_Autor, ID_editora)
VALUES ('Windows Server 2012 Inside Out', 123356789,'20040517', 66.80, 4, 3);

INSERT INTO tbl_livro (Nome_Livro, ISBN, Data_Pub, Preco_Livro, ID_Autor, ID_editora)
VALUES ('Microsoft Exchange Server 2010', 123366789,'20001221', 45.30, 4, 3);

-- Altera o tipo de dados de uma coluna:
ALTER TABLE tbl_livro
MODIFY COLUMN Preco_Livro DECIMAL(10,2);


######################################################
# 14 Consultas simples ############
######################################################
https://www.youtube.com/watch?v=5sTFJHOSDvg&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=14


SELECT coluna FROM tabela;

SELECT Nome_Autor FROM tbl_autores;
SELECT * FROM tbl_autores;
SELECT Nome_Livro FROM tbl_livro;

* = todas as colunas => olhar a tabela inteira

COLUNAS ESPECIFICADAS

SELECT colunas FROM tabela;

SELECT Nome_Livro, ID_Autor FROM tbl_livro;

SELECT Nome_Livro, ISBN
FROM tbl_livro;

SELECT Nome_Livro, ISBN, Data_Pub
FROM tbl_livro;

/*
######################################################
# 15 Consulta com Ordenação ############
######################################################
https://www.youtube.com/watch?v=qAtiTGjxrcA&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=15
 */
SELECT * FROM tbl_livro
ORDER BY Nome_livro ASC;

SELECT * FROM tbl_livro
ORDER BY Nome_livro DESC;

-- SELECT colunas FROM tabela
-- ORDER BY coluna_a_ordenar

SELECT Nome_Livro, ID_Editora
FROM tbl_Livro
ORDER BY ID_Editora;

SELECT Nome_Livro, Preco_Livro
FROM tbl_Livro
ORDER BY Preco_Livro DESC;

SELECT Nome_Livro, Preco_Livro
FROM tbl_Livro
ORDER BY Preco_Livro ASC;

/*
######################################################
# 16 INDEXAÇÃO DE TABELAS ############
######################################################
https://www.youtube.com/watch?v=HsZA-pPAt7g&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=16

Índices são empregados em consultas para ajudar a encontrar registros com um valor específico em uma coluna de forma rápida - ou seja, aumentar o desempenho na execução de consultas.

Com índices, o MySQL vai direto a uma linha em vez de buscar toda a tabela até encontrar os registros que importam.

Por padrão, o MySQL cria índices automaticamente para campos de:
- Chave Primária;
- Chave Estrangeira;
- Constraint UNIQUE.

Além disso, podemos criar índices para outras colunas usadas com frequência em buscas ou junções.

Existem dois grandes tipos de índices disponíveis: 1) Índice Clusterizado (chave primária, só pode ter um); 2) Índice não clusterizado.

Criar índices (forma 1):

CREATE [UNIQUE] INDEX nome_índice
ON nome_tabela (
    coluna1 [ASC ! DESC],
    [coluna 2 [ASC | DESC]]
)

Criar índices (forma 1):

ALTER TABLE nome_tabela
ADD INDEX nome_índice (colunas)

É possível também criar o índice junto com a criação da tabela, usando a palavra-chave INDEX.

 */

-- Mostrar os índices:
SHOW INDEX FROM tbl_editoras;

-- EXPLAIN Mostra como vai ser realizado o comando que vem na frente dele (mas NÃO executa o comando para valer):

EXPLAIN SELECT * FROM tbl_editoras
WHERE Nome_Editora = 'Springer';

-- rows = número de linhas lidas

-- Cria o índice:

CREATE INDEX idx_editora
ON tbl_editoras(Nome_Editora);

EXPLAIN SELECT * FROM tbl_editoras
WHERE Nome_Editora = 'Springer';

-- leu menos linhas. Extra = Using index

/* Dica: criar índices nas colunas que são mais acessadas em termos de consulta. Colunas que são muito alteradas nem sempre vão performar bem com índices */

-- Excluir índice:

DROP INDEX idx_editora
ON tbl_editoras;

/* 
######################################################
# 17 Filtragem de linhas com o WHERE ############
######################################################
https://www.youtube.com/watch?v=XytX5Ok9qGU&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=17

SELECT colunas
FROM tabela
WHERE coluna = valor;
 */

SELECT Nome_Livro, Data_Pub
FROM tbl_Livro
WHERE ID_Autor = 1;

SELECT ID_Autor, Nome_Autor
FROM tbl_autores
WHERE Sobrenome_Autor = 'Stanek';

/* 
######################################################
# 18 Filtragem de linhas com o WHERE e 
AND, OR e NOT ############
######################################################
https://www.youtube.com/watch?v=P5RWRi1BvAg&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=18

 */

SELECT *
FROM tbl_livro
WHERE ID_Livro > 2 AND ID_Autor < 3;

SELECT *
FROM tbl_livro
WHERE ID_Livro > 2 OR ID_Autor < 3;

SELECT *
FROM tbl_livro
WHERE ID_Livro > 2 AND NOT ID_Autor < 3;

/* 
######################################################
# 19 Operadores IN e NOT IN ############
######################################################
https://www.youtube.com/watch?v=lZypSFZBrMc&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=19

Filtragem usando listas de valores no MySQL

SELECT coluna(s)
FROM tabela(s)
WHERE expressão | valor IN (lista de valores);

SELECT coluna(s)
FROM tabela(s)
WHERE expressão | valor NOT IN (lista de valores);

 */

SELECT Nome_Livro, ID_Editora
FROM tbl_livro
WHERE ID_Editora IN (2, 4);

SELECT Nome_Livro, ID_Editora
FROM tbl_livro
WHERE ID_Editora NOT IN (2, 4);

-- Se sabe o nome das editoras, mas não os IDs, é possível encontrar os livros, sem fazer o JOIN, mas com subconsultas:
SELECT Nome_Livro, ID_Editora
FROM tbl_livro
WHERE ID_Editora IN (
    SELECT ID_Editora
    FROM tbl_editoras
    WHERE Nome_Editora = 'Wiley' OR Nome_Editora = 'Microsoft Press'
);

/* 
######################################################
# 20 Excluir Registros ############
######################################################
https://www.youtube.com/watch?v=f-r0VqSuT58&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=20

DELETE FROM tabela
WHERE coluna = valor;

 */

DELETE FROM tbl_autores
WHERE ID_Autor = 2;

/* 
TRUNCATE TABLE
- Remove todas as linhas de uma tabela sem registrar as exclusões de linhas individuais;
- TRUNCATE TABLE é como a instrução DELETE sem usar a cláusula WHERE;
- Entretanto, TRUNCATE TABLE é mais rápida e utiliza menos recursos de sistema e log de transações.

SELECT * FROM tbl_teste_incremento;
 */

DELETE FROM tbl_teste_incremento
WHERE Codigo = 90;

TRUNCATE TABLE tbl_teste_incremento;

/* 
######################################################
# 21 Alias ############
######################################################
https://www.youtube.com/watch?v=yEd9wGCb_tI&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=21

Pode-se dar um nome diferente a uma coluna ou tabela em uma consulta.

SELECT colunas
AS alias_coluna
FROM tabela AS alias_tabela;

 */

SELECT Nome_Livro
AS Livro
FROM tbl_livro;

SELECT Nome_Livro
AS Livro
FROM tbl_livro AS MeusLivros;

SELECT
Nome_Livro AS Livro,
Data_Pub AS Publicação
FROM tbl_livro AS MeusLivros;

SELECT
Nome_Livro AS Livros,
Preco_Livro AS Preço
FROM tbl_livro AS MeusLivros;

SELECT
Nome_Livro AS L,
Preco_Livro AS P
FROM tbl_livro AS MeusLivros;

/* 
######################################################
# 22 Funções de Agregação ############
######################################################
https://www.youtube.com/watch?v=RMv2V6RG4vw&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=22

Funções de agregação são funções SQL que permitem executar uma operação aritmética nos valores de uma coluna em todos os registros de uma tabela.
Retornam um valor único baseado em um conjunto de valores.

Sintaxe básica:

função (ALL | DISTINCT expressão)

MIN = Valor Mínimo
MAX = Valor Máximo
AVG = Média Aritmética
SUM = Total (Soma)
COUNT = Contar quantidade de itens

 */

-- Contagem dos registros da tabela
SELECT COUNT(*)
FROM tbl_autores;

-- Contagem do registros distintos da tabela
SELECT COUNT(DISTINCT id_autor)
FROM tbl_Livro;

SELECT COUNT( id_autor)
FROM tbl_Livro;

SELECT MAX(Preco_Livro)
FROM tbl_Livro;

SELECT MIN(Preco_Livro)
FROM tbl_Livro;

SELECT AVG(Preco_Livro)
FROM tbl_Livro;

SELECT SUM(Preco_Livro)
FROM tbl_Livro;

/* 
######################################################
# 23 Renomear Tabelas ############
######################################################
https://www.youtube.com/watch?v=2pRcgyor97I&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=23

RENAME TABLE tabela1 TO tabela2;

CREATE TABLE Clientes (
    ID_Cliente SMALLINT,
    Nome_Cliente VARCHAR(20),
    CONSTRAINT PRIMARY KEY(ID_Cliente)
);

 */

RENAME TABLE Clientes TO Meus_Clientes;

/* 
######################################################
# 24 Atualizar Registros ############
######################################################
https://www.youtube.com/watch?v=0n8_RS-iNr0&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=24
 
UPDATE tabela
SET coluna = novo_valor_armazenado
WHERE coluna = valor_filtro;

Obs.: caso não seja usada a cláusula WHERE para filtrar os registros, todos os dados da coluna serão alterados.

 */

UPDATE tbl_livro
SET Nome_Livro = 'SSH, o Shell Seguro'
WHERE ID_Livro = 2;

/* 
######################################################
# 25 Seleção de intervalos ############
######################################################
https://www.youtube.com/watch?v=lNvzhgT0l28&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=25

SELECT colunas FROM tabela
WHERE coluna BETWEEN valor 1 AND valor2;

 */

SELECT * FROM tbl_livro
WHERE Data_Pub BETWEEN '20040517' AND '20110517';

SELECT
Nome_Livro AS Livro,
Preco_Livro AS Preço
FROM tbl_livro
WHERE Preco_Livro BETWEEN 40.00 AND 60.00;

/* 
######################################################
# 26 LIKE e NOT LIKE ############
######################################################
https://www.youtube.com/watch?v=zyfuDf4atxQ&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=26

Determina se uma cadeia de caracteres específica corresponde a um padrão especificado. Um padrão pode incluir caracteres normais e curingas.

NOT LIKE inverte a comparação, verificando se a cadeia de caracteres NÃO corresponde ao padrão especificado.

Padrões específicos (metacaracteres):

'%' -- Qualquer cadeia de 0 ou mais caracteres;
'_' -- Sublinhado: qualquer caracter único.

 */

SELECT *
FROM tbl_livro
WHERE Nome_Livro LIKE 'F%';

SELECT *
FROM tbl_Livro
WHERE Nome_Livro NOT LIKE 'S%';

SELECT Nome_Livro
FROM tbl_livro
WHERE Nome_Livro LIKE '_i%';

/* 
######################################################
# 27 REGEXP - Expressões regulares ############
######################################################
https://www.youtube.com/watch?v=_YUqYkm8u9o&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=27

O MySQL suporta um tipo de operação de busca de padrões baseada em expressões regulares com o operador REGEXP.

[...] -- Qualquer caracter único no intervalo ou conjunto especificado ([a-h]; [aeiou])

[^...] -- Qualquer caracter único que não esteja no intervalo ou conjunto especificado ([^a-h];[^aeiou])

^ -- Início da string;
$ -- Fim da string;
a|b|c -- Alternação (a ou b ou c)

 */

SELECT Nome_Livro
FROM tbl_livro
WHERE Nome_Livro REGEXP '^[FS]';

SELECT Nome_Livro
FROM tbl_livro
WHERE Nome_Livro REGEXP '^[^FS]';

SELECT Nome_Livro
FROM tbl_livro
WHERE Nome_Livro REGEXP '[ng]$';

SELECT Nome_Livro
FROM tbl_livro
WHERE Nome_Livro REGEXP '^[FS]|Mi';

/* 
######################################################
# 28 Usando o Valor-padrão ############
######################################################
https://www.youtube.com/watch?v=WAAaULNCUyw&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=28

Criar um padrão:

ALTER TABLE nome_tabela
MODIFY COLUMN nome_coluna tipo_dados
DEFAULT 'valor_padrão';

 */

ALTER TABLE tbl_autores
MODIFY COLUMN Sobrenome_Autor VARCHAR(60)
DEFAULT 'da Silva';

-- Inserir dois registros para teste:
INSERT INTO tbl_autores (ID_Autor, Nome_Autor)
VALUES (7, 'João');

INSERT INTO tbl_autores (ID_Autor, Nome_Autor, Sobrenome_Autor)
VALUES (8, 'Rita', 'de Souza');

-- No primeiro caso, não foi especificado o sobrenome do autor; será assumido o valor padrão criado.

-- Verificando o resultado:
SELECT * FROM tbl_autores;

-- Para remover os padrões (ALTER TABLE sem a linha do DEFAULT):

ALTER TABLE tbl_autores
MODIFY COLUMN Sobrenome_Autor VARCHAR(60);

INSERT INTO tbl_autores (ID_Autor, Nome_Autor)
VALUES (9, 'Ana');

-- Verificando o resultado:
SELECT * FROM tbl_autores;

/* 
######################################################
# 29 Backup do Banco de Dados ############
######################################################
https://www.youtube.com/watch?v=0dR1tURsfrM&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=29

Usar o comando mysqldump no terminal:

mysqldump -u root -p nome_banco > backup.sql

 */



/* 
Tem que colocar no PATH do windows a pasta:

- Pesquisar: Sistema;
- Configurações avançadas do sistema;
- Variáveis de Ambiente;
- Path -> Editar;
- Novo -> C:\Program Files\MySQL\MySQL Server 8.0\bin
- OK -> OK -> OK
 */

mysqldump -u root -p db_Biblioteca > "D:\Códigos, Dados, Documentação e Cheat Sheets\codigos_versionados\Python\Banco de Dados\dbBiblioteca.sql"

-- Para restaurar o backup:

/* Crie um banco de dados novo no servidor, de nome teste_restore;
Use o seguinte comando (no terminal):
mysql -u root -p banco_criado < backup.sql

Exemplo: Crie um novo banco (vazio, o comando CREATE DATABASE teste_restore;) denominado teste-restore; digite: */

mysql -u root -p teste_restore < "D:\Códigos, Dados, Documentação e Cheat Sheets\codigos_versionados\Python\Banco de Dados\dbBiblioteca.sql"

/* 
######################################################
# 30 GROUP BY ############
######################################################
https://www.youtube.com/watch?v=RIOTRrTmDwA&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=30

Usamos a cláusula GROUP BY para agrupar registros em subgrupos baseados em colunas ou valores retornados por uma expressão.
Sintaxe básica:

SELECT colunas, função_agregação()
FROM tabela
WHERE filtro
GROUP BY colunas

 */

-- TAbela para teste do GROUP BY
/* 

CREATE TABLE Vendas (
    ID SMALLINT Primary Key,
    Nome_Vendedor VARCHAR(20),
    Quantidade INT,
    Produto VARCHAR(20),
    Cidade VARCHAR(20)
);

INSERT INTO Vendas (ID, Nome_Vendedor, Quantidade, Produto, Cidade)
VALUES (10, 'Jorge', 1400, 'Mouse', 'São Paulo');

INSERT INTO Vendas (ID, Nome_Vendedor, Quantidade, Produto, Cidade)
VALUES (12, 'Tatiana', 1220, 'Teclado', 'São Paulo');

INSERT INTO Vendas (ID, Nome_Vendedor, Quantidade, Produto, Cidade)
VALUES (14, 'Ana', 1700, 'Teclado', 'Rio de Janeiro');

INSERT INTO Vendas (ID, Nome_Vendedor, Quantidade, Produto, Cidade)
VALUES (15, 'Rita', 2120, 'Webcam', 'Recife');

INSERT INTO Vendas (ID, Nome_Vendedor, Quantidade, Produto, Cidade)
VALUES (18, 'Marcos', 980, 'Mouse', 'São Paulo');

INSERT INTO Vendas (ID, Nome_Vendedor, Quantidade, Produto, Cidade)
VALUES (19, 'Carla', 1120, 'Webcam', 'Recife');

INSERT INTO Vendas (ID, Nome_Vendedor, Quantidade, Produto, Cidade)
VALUES (22, 'Roberto', 3145, 'Mouse', 'São Paulo');

filtro para o resultado do grupoby = HAVING

 */

-- Consulta usando agregação para obter o total de vendas de Mouses:
SELECT SUM(Quantidade) AS TotalMouses
FROM Vendas
WHERE Produto = 'Mouse';

-- Consulta totalizando as vendas de todos os produtos por cidade:
SELECT Cidade, SUM(Quantidade) AS Total
FROM Vendas
GROUP BY Cidade;

-- Número de registros de venda por cidade
SELECT Cidade, COUNT(Quantidade) AS Contagem
FROM Vendas
GROUP BY Cidade;

-- ou:
SELECT Cidade, COUNT(*) AS Contagem
FROM Vendas
GROUP BY Cidade;

/* 
######################################################
# 31 HAVING (filtro p/ o GROUP BY) ############
######################################################
https://www.youtube.com/watch?v=W526HRx84oE&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=31

Cláusula usada para especificar condições de filtragem em grupos de registros ou agregações.
É frequentemente usada coma a cláusula GROUP BY para filtrar as colunas agrupadas.
O HAVING é como se fosse uma cláusula WHERE, só que ao invés de mandar com o SELECT, é aplicado ao GROUP BY.

Sintaxe:
SELECT colunas, função_de_agregação()
FROM tabela
GROUP BY
HAVING filtro_agrupamento;

 */

-- Consulta retornando total de vendas das cidades com menos de 2500 produtos vendidos:
SELECT Cidade, SUM(Quantidade) AS Total
FROM Vendas
GROUP BY Cidade
HAVING SUM(Quantidade) < 2500;

-- ou:

SELECT Cidade, SUM(Quantidade) AS Total
FROM Vendas
GROUP BY Cidade
HAVING Total < 2500;

-- Consulta retornando total de vendas do produto 'Teclado' das cidades com menos de 1500 teclados vendidos:

SELECT Cidade, SUM(Quantidade) AS TotalTeclados
FROM Vendas
WHERE Produto = 'Teclado'
GROUP BY Cidade
HAVING SUM(Quantidade) < 1500;

/* 
######################################################
# 32 VIEWS ############
######################################################
https://www.youtube.com/watch?v=m1C8c8QRz4s&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=32

- Uma Exibição (Visão) é uma tabela virtual baseada no conjunto de resultados de uma consulta SQL;
- Contém linhas e colunas como uma tabela real, e pode receber comandos como declarações JOIN, WHERE e funções como uma uma tabela normal;
- Mostra sempre resultados de dados atualizados, pois o motor do banco de dados recria os dados toda vez que um usuário consulta a visão.

CRIAÇÃO DE VIEWS:

CREATE VIEW [Nome_Exibição]
AS SELECT colunas
FROM tabela
WHERE condições

 */


CREATE VIEW vw_LivrosAutores
AS
SELECT
tbl_livro.Nome_Livro AS Livro,
tbl_autores.Nome_Autor AS Autor
FROM tbl_Livro
INNER jOIN tbl_autores
ON tbl_livro.ID_Autor = tbl_autores.ID_Autor;

SELECT Livro, Autor
FROM vw_LivrosAutores
ORDER BY Autor;

-- ALTERAÇÃO DE VIEWS

ALTER VIEW vw_LivrosAutores AS
SELECT
tbl_livro.Nome_Livro AS Livro,
tbl_autores.Nome_Autor AS Autor,
tbl_livro.Preco_Livro AS Valor
FROM tbl_Livro
INNER JOIN tbl_autores
ON tbl_livro.ID_Autor = tbl_autores.ID_Autor;

SELECT *
FROM vw_LivrosAutores
ORDER BY Valor;

-- EXCLUIR A VIEW

DROP VIEW vw_LivrosAutores;

/* 
######################################################
# 33 INNER JOIN ############
######################################################
https://www.youtube.com/watch?v=C_OpAzDImfI&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=33

- A cláusula JOIN é usada para combinar dados provenientes de duas ou mais tabelas, baseado em um relacionamento entre colunas destas tabelas;

- INNER JOIN: Retorna linhas quando houver pelo menos uma correspond~encia em AMBAS as tabelas;
- OUTER JOIN: Retorna linhas mesmo quando não houver pelo menos uma correspondência em uma das das tabelas (ou ambas). o OUTER JOIN divide-se em LEFT JOIN, RIGHT JOIN e FULL JOIN.

SELECT colunas
FROM tabela1
INNER JOIN tabela2
ON tabela1.coluna = tabela2.coluna;

 */

SELECT * FROM tbl_livro
INNER JOIN tbl_autores
ON tbl_livro.ID_Autor = tbl_autores.ID_Autor;

SELECT tbl_livro.Nome_Livro, tbl_livro.ISBN, tbl_autores.Nome_Autor
FROM tbl_livro
INNER JOIN tbl_autores
ON tbl_livro.ID_Autor = tbl_autores.ID_Autor;

-- Usando Aliases e cláusulas WHERE e LIKE:

SELECT
L.Nome_Livro AS Livros,
E.Nome_Editora AS Editoras
FROM tbl_livro AS L
INNER JOIN tbl_editoras AS E
ON L.ID_Editora = E.ID_editora
WHERE E.Nome_Editora LIKE 'M%';

-- INNER JOIN COM TRÊS TABELAS

SELECT
L.Nome_Livro AS Livro,
A.Nome_Autor AS Autor,
E.Nome_Editora AS Editoras
FROM tbl_Livro AS L
INNER JOIN tbl_autores AS A
ON L.ID_Autor = A.ID_Autor
INNER JOIN tbl_editoras AS E
ON L.ID_Editora = E.ID_Editora;

/* 
######################################################
# 34 LEFT e RIGHT JOIN ############
######################################################
https://www.youtube.com/watch?v=4m3HNtsFRoI&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=34

- LEFT JOIN: Retorna todas as linhas da tabela à esquerda, mesmo se não houver nenhuma correspondência na tabela à direita;
- RIGHT JOIN: Retorna as linhas da tabela à direita, mesmo se não houver nenhuma correspond~encia na tabela à esquerda;
- FULL JOIN: Retorna linhas quando houver uma correspondência em qualquer uma das tabelas. É uma combinação de LEFT e RIGHT JOINs.

 */

-- LEFT JOIN
/* 
SELECT coluna
FROM tabela_esq
LEFT JOIN tabela_dir
ON tabela_esq.coluna = tabela_dir.coluna;
 */

SELECT *
FROM tbl_autores
LEFT JOIN tbl_livro
ON tbl_livro.ID_Autor = tbl_autores.ID_Autor;

-- LEFT JOIN - ESCLUINDO AS CORRESPONDÊNCIAS
/* 
SELECT coluna
FROM tabela_esq
LEFT JOIN tabela_dir
ON tabela_esq.coluna = tabela_dir.coluna
WHERE tabela_dir.coluna IS NULL;

Responde à pergunta:
Quais autores não têm nenhum livro cadastrado?
 */

SELECT *
FROM tbl_autores
LEFT JOIN tbl_livro
ON tbl_livro.ID_Autor = tbl_autores.ID_Autor
WHERE tbl_livro.ID_Autor IS NULL;

-- RIGHT JOIN
/* 
SELECT colunas
FROM tabela_esq
RIGHT JOIN tabela_dir
ON tabela_esq.coluna = tabela_dir.coluna;
 */

-- ------------------

/* 
Para auxiliar na visualização:

INSERT INTO tbl_editoras (ID_Editora, Nome_Editora)
VALUES (6, 'Companhia das Letras');

 */

SELECT *
FROM tbl_livro AS Li
RIGHT JOIN tbl_editoras AS Ed
ON Li.ID_editora = Ed.ID_editora;

-- RIGHT JOIN - ESCLUINDO AS CORRESPONDÊNCIAS
/* 
SELECT coluna
FROM tabela_esq
Right JOIN tabela_dir
ON tabela_esq.coluna = tabela_dir.coluna
WHERE tabela_esq.coluna IS NULL;

Responde à pergunta:
Quais editoras não têm nenhum livro cadastrado?
 */

SELECT *
FROM tbl_livro AS Li
RIGHT JOIN tbl_editoras AS Ed
ON Li.ID_editora = Ed.ID_editora
WHERE Li.ID_Editora IS NULL;

/* 
######################################################
# 35 Concatenação de Strings ############
######################################################
https://www.youtube.com/watch?v=xMLXB4N8Ggk&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=35

É possível concatenar strings usando-se a função CONCAT().
Sintaxe:
CONCAT(string | nome_coluna, <string | nome_coluna)


 */

SELECT CONCAT('Fábio ', 'dos Reis') AS 'Meu Nome';

SELECT
CONCAT(Nome_Autor, ' ', Sobrenome_Autor) AS 'Nome Completo'
FROM tbl_autores;

SELECT
CONCAT('Eu gosto do livro ', Nome_Livro)
FROM tbl_livro
WHERE ID_Autor = 2;

CREATE TABLE teste_nulos (
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    item VARCHAR(20),
    quantidade SMALLINT NULL
);

INSERT INTO teste_nulos (id, item, quantidade)
VALUES (1, 'Pendrive', 5);

INSERT INTO teste_nulos (id, item, quantidade)
VALUES (2, 'Monitor', 7);

INSERT INTO teste_nulos (id, item, quantidade)
VALUES (3, 'Teclado', NULL);

SELECT * FROM teste_nulos;

/* 
Se uma string for concatenada com NULL, o resultado retornado será NULL:
 */

SELECT CONCAT('A quantidade adquirida é ', quantidade)
FROM teste_nulos
WHERE item = 'Teclado';

/* 
Para evitar o resultado nulo do comando anterior:

IFNULL(valor, substituição)

COALESCE(valor1, valor2, ..., valorN)
Essa função retornará o primeiro valor não-nulo encontrado em seus argumentos.

A função COALESCE é mais poderosa do que IFNULL.

 */

SELECT
CONCAT('A quantidade adquirida é ', IFNULL(quantidade, 0))
FROM teste_nulos
WHERE item = 'Teclado';

SELECT
CONCAT('A quantidade adquirida é ', COALESCE(NULL,quantidade,NULL, 0))
FROM teste_nulos
WHERE item = 'Teclado';

/* 
######################################################
# 36 Operações matemáticas ############
######################################################
https://www.youtube.com/watch?v=CrIJKQ-d5OI&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=36

É possível realizar operações matemáticas simples nos valores de uma coluna e retornar resultados em uma coluna calculada.
Para isso, usamos os operadores matemáticos comuns:

+ Soma
- Subtração
/ Divisão
* Multiplicação
% ou Mod Resto da divisão
DIV Divisão inteira

 */

SELECT 3 * 9;

SELECT
Nome_livro,
Preco_Livro * 5 AS 'Preço de 5 Unidades'
FROM tbl_livro;

SELECT 2 * 9 / 3;

SELECT
Nome_Livro,
Preco_Livro / 2 AS 'Preço com 50% de desconto'
FROM tbl_livro;

SELECT 10 MOD 3;

SELECT 10 DIV 3;

/* 
FUNÇÕES MATEMÁTICAS:
É possível também utilizar funções matemáticas nos valores de uma coluna.
Abaixo vemos algumas funções matemáticas mais comuns:

CEILING() Arrendodar p/ cima;
FLOOR() Arredondar p/ baixo;
PI() Retorna o valor de Pi;
POW(x,y) Retorna x elevado a y
SQRT() Raiz quadrada de um argumento;
SIN() Retorna o seno de um número dado em radianos;
HEX() Retorna a representação hexadecimal de um valor decimal.
 */

SELECT
Nome_Livro,
CEILING(Preco_Livro * 5) AS 'Preço de 5 arrendodado p/ CIMA'
FROM tbl_livro;

SELECT
Nome_Livro,
FLOOR(Preco_Livro * 5) AS 'Preço de 5 arrendodado p/ BAIXO'
FROM tbl_livro;

SELECT PI();

SELECT POW(2,4);

SELECT SQRT(81);

SELECT SIN(PI());

SELECT HEX(1200);

/* 
######################################################
# 37 Funções e procedimentos ############
######################################################
https://www.youtube.com/watch?v=mzd2W3cwohM&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=37

Funções e Procedimentos:
São dois tipos de rotinas armazenadas, parte da especificação SQL.
São um pouco similares, mas com aplicações diferentes.
São invocadas de formas diferentes tambem (CALL x declaração)

Uma função é usada para gerar um valor que pode ser usado em uma expressão.
O valor é geralmente baseado em um ou mais parâmetros fornecidos à função.
É executada como parte de uma expressão.

SINTAXE DE UMA FUNÇÃO:

CREATE FUNCTION nome_função (parâmetros)
RETURNS tipo_dados
código_da_função;

INVOCANDO UMA FUNÇÃO:
SELECT nome_função(parâmetros);

Deu erro:
18:27:30	CREATE FUNCTION fn_teste (a DECIMAL(10,2), b INT) RETURNS INT RETURN a * b	Error Code: 1418. This function has none of DETERMINISTIC, NO SQL, or READS SQL DATA in its declaration and binary logging is enabled (you *might* want to use the less safe log_bin_trust_function_creators variable)	0.000 sec


SOLUÇÃO:
https://stackoverflow.com/questions/26015160/deterministic-no-sql-or-reads-sql-data-in-its-declaration-and-binary-logging-i

adicionar a linha abaixo de RETURNS ....:
READS SQL DATA DETERMINISTIC
 */

CREATE FUNCTION fn_teste (a DECIMAL(10,2), b INT)
CREATE FUNCTION fn_teste (a DECIMAL(10,2), b INT)
RETURNS INT
READS SQL DATA DETERMINISTIC
RETURN a * b;

-- Invocando a função:
SELECT fn_teste(2.5, 4) AS Resultado;

SELECT
Nome_Livro,
fn_teste(Preco_Livro, 6) AS 'Preço de 6 unidades'
FROM tbl_livro
WHERE ID_Livro = 2;

-- Excluindo uma função
DROP FUNCTION fn_teste;

/* 
######################################################
# 38 Procedimentos armazenados ############
######################################################
https://www.youtube.com/watch?v=w3F4JQ8ndJ0&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=38

Stored Procedures
Um procedimento armazenado é uma sub-rotina disponível para aplicações que acessam sistemas de bancos de dados relacionais.
Podem ser usadas para validação de dados, controle de acesso, execução de declarações SQL complexas e outras situações.
Desde a versão 5.0  MySQL suporta a execução de Stored Procedures.

Sintaxe da criação do Procedimento:
CREATE PROCEDURE nome_procedimento (parâmetros) declarações;

Invocando o Procedimento:

CALL nome_procedimento (parâmetros);

 */

CREATE PROCEDURE verPreço (varLivro SMALLINT)
SELECT CONCAT('O preço é ', Preco_Livro) AS Preço
FROM tbl_Livro
WHERE ID_Livro = varLivro;

-- Invocando o procedimento
CALL verPreço(3);

-- Excluindo Procedimentos:
-- DROP PROCEDURE nome_procedimento;
DROP PROCEDURE verPreço;

/* 
######################################################
# 39 Blocos BEGIN e END em Funções e Procedimentos armazenados ############
######################################################
https://www.youtube.com/watch?v=L32752VIam8&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=39

São "contêiners" usados para delimitar blocos de comandos a serem executados pela função ou stored procedure.
Cada declaração aninhada possui um delimitador (;).
Um bloco BEGIN pode ser aninhado dentro de outros blocos.

Porém o delimitador ; pode ser problemático pois, ao ser encontrado em um procedimento ou função, a finaliza imediatamente. É uma espécie de alias para o comando GO.
Devemos então mudar esse "atalho" e, para isso, usamos o comando DELIMITER para criar rotinas com declarações compostas.

 */

-- Função com BEGIN e END

DELIMITER $$
CREATE FUNCTION aumenta_preco (preco DECIMAL(10,2), taxa DECIMAL(10,2))
RETURNS DECIMAL(10,2)
READS SQL DATA DETERMINISTIC
BEGIN
    RETURN preco + preco * taxa / 100;
END $$
DELIMITER ;

-- Invocando a função para aumentar o preço em 10%:
SELECT aumenta_preco(50.00, 10.00) AS Resultado;

-- Procedimento com BEGIN e END

DELIMITER //
CREATE PROCEDURE verPreço (varLivro SMALLINT)
BEGIN
    SELECT CONCAT('O preço é ', Preco_Livro) AS Preço
    FROM tbl_livro
    WHERE ID_Livro = varLivro;
    SELECT 'Procedimento executado com sucesso!';
END
//
DELIMITER ;

-- Invocando o procedimento
CALL verPreço(3);

/* 
######################################################
# 40 Parâmetros em Stored Procedures ############
######################################################
https://www.youtube.com/watch?v=STetVKOhLkI&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=40

Podemos usar parâmetros para passar argumentos para o procedimento armazenado e obter valores a partir dele.
Em MySQL existem três tipos de parâmetros:
- IN;
- OUT;
- INOUT.

Parâmetro IN
É o modo padrão. Quando você define um parâmetro IN em um SP, o programa chamador tem de passar um argumento ao procedimento armazenado.
Essa passagem de parâmetros é do tipo passagem por valor, portanto o valor do parâmetro fora do procedimetno armazenado permanece inalterado.
São semelhantes aos parâmetros de função.

Parâmetro OUT
O valor de um parâmetro OUT pode ser alterado dentro do procedimento armazenado e seu novo valor é passado de volta ao programador chamador.
O procedimento armazenado não pode acessar o valor inicial do parâmetro OUT quando ele é iniciado, e a variável passada é "limpa".
Procedimentos OUT são similares aos procedimentos INOUT, com uma diferença significativa: no parâmetro OUT, o valor do parâmetro, portanto o valor da variável cujo valor é passado como parâmetro, é ajustado para NULL no início da execução do procedimento.

Parâmetro INOUT
Trata-se de uma combinação dos parâmetros IN e OUT.
Isso significa que o programa chamador deve passar o argumento e o procedimento armazenado pode modificar o parâmetro INOUT e repassar o novo valor de volta ao programa chamador.
Portanto, uma referência à variável externa é passada ao procedimento.

Sintaxe de um Parâmetro:

MODO nome_param tipo_param(tamanho_param)

O modo pode ser IN, OUT, ou INOUT, dependendo do propósito do procedimento armazenado.

Veremos exemplos nos próximos slides.

 */

-- Exemplo 1 (IN):
DELIMITER //
CREATE PROCEDURE editora_livro (IN editora VARCHAR(50))
BEGIN
    SELECT L.Nome_Livro, E.Nome_Editora
    FROM tbl_livro AS L
    INNER JOIN tbl_editoras AS E
    ON L.ID_Editora = E.ID_Editora
    WHERE E.Nome_Editora = editora;
END
//
DELIMITER ;

CALL editora_livro('Willey');

-- Passando por parâmetro:
SET @minhaeditora = 'Willey';
CALL editora_livro(@minhaeditora);


-- Exemplo 2 (IN):

DELIMITER //
CREATE PROCEDURE aumenta_preco (IN codigo INT, taxa DECIMAL(10,2))
BEGIN
    UPDATE tbl_livro
    SET Preco_Livro = tbl_livro.Preco_Livro + tbl_livro.Preco_Livro * taxa / 100
    WHERE ID_Livro = codigo;
END //
DELIMITER ;


-- Testando: vamos aumentar o preço do livro de ID 4 em 20%:
-- Primeiro verificamos o preço atual:
SELECT * FROM tbl_livro WHERE ID_Livro = 4;
-- Aplicamos agora o procedimento de aumento:
SET @livro = 4;
SET @aumento = 20; -- aumetno de 20%
CALL aumenta_preco(@livro, @aumento);

-- Exemplo 1 (OUT):

DELIMITER //
CREATE PROCEDURE teste_out (IN id INT, OUT livro VARCHAR(50))
BEGIN
    SELECT Nome_Livro
    INTO livro
    FROM tbl_livro
    WHERE ID_Livro = id;
END //
DELIMITER ;

CALL teste_out(3, @livro);
SELECT @livro;

/* 
No exempçp a segior, o valor da variável que for passado ao parâmetro "valor" será refletido na própria variável externa, a qual terá seu valor alterado também
 */

DELIMITER //
CREATE PROCEDURE aumento (INOUT valor DECIMAL(10,2), taxa DECIMAL(10,2))
BEGIN
    SET valor = valor + valor * taxa / 100;
END //
DELIMITER ;

/* Testando. Criamos a variável valorinicial, e a usamos para passar o parâmetro valor. Vamos aumentar o valor em 15%: */

SET @valorinicial = 20.00;
SELECT @valorinicial;

CALL aumento(@valorinicial, 15.00);
/* Verificamos agora se a variável externa @valorinicial foi alterada: */
SELECT @valorinicial;

/* 
######################################################
# 41 Escopo das variáveis ############
######################################################
https://www.youtube.com/watch?v=EaU4FKWDhGk&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=41

O escopo de uma variável diz respeito aos locais onde a variável "existe" ou seja, onde ela pode ser acessada.
Níveis de Escopo:
- Global l(acessíveis de qualquer local);
- Sessão (variáveis @ e de sistema);
- Parâmetros (nível de rotinas, criadas quando a rotina é chamada, e destruídas quando a rotina termina);
- Local (limitadas ao bloco BEGIN onde foram declaradas).

Declaração de Variáveis Locais:
Podemos criar variáveis locais em um procedimento ou função usando uma declaração DECLARE dentro de um bloco BEGIN.
A variável pode ser criada e incializada com um valor desejado.
Ficam disponíveis apenas dentro do bloco onde foram criadas, e em blocos que existam dentro do bloco onde a variável foi criada.
Após ter sido executado e encerrrado, a variável é desalocada da memória.

Sintaxe de declaração de variáveis locais:
-- Sintaxe:
DECLARE nome_var1 tipo, nome_var2 tipo
[DEFAULT valor_padrão]

A instrução DECLARE deve vir antes de qualquer outra instrução no bloco BEGIN.
Podemos declarar diversas variáveis numa mesma instruçaão DECLARE, desde que sejam todas do mesmo tipo de dados e valor-padrão.
Como atribuir valores às variáveis: podemos usar a instrução SET ou ainda SELECT ... INTO.

 */

DELIMITER //
CREATE FUNCTION calcula_desconto(livro INT, desconto DECIMAL(10,2))
RETURNS DECIMAL(10,2)
READS SQL DATA DETERMINISTIC
BEGIN
    DECLARE preco DECIMAL(10,2);
    SELECT Preco_Livro FROM tbl_livro
    WHERE ID_Livro = livro INTO preco;
    RETURN preco - desconto;
END//
DELIMITER ;

-- Testando com o livro de ID 4 e desconto de R$ 10,00:

SELECT * FROM tbl_livro WHERE ID_Livro = 4;

SELECT calcula_desconto(4, 10.00);

SELECT * FROM tbl_livro WHERE ID_Livro = 4;

/* 
######################################################
# 42 Blocos condicionais IF - THEN - ELSE e CASE ############
######################################################
https://www.youtube.com/watch?v=xikU6R7vZrs&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=42

Há dois tipos básicos de blocos condicionais:
1. IF ... ELSEIF ... ELSE ... END IF;

2. CASE ... WHEN ... THEN ... ELSE ... ENDE CASE;

Sintaxe de um bloco IF:

IF condição THEN lista_declarações
    [ELSEIF condição THEN lista_declarações]
    ...
    [ELSE lista_declarações]
END IF;

Sintaxe de um bloco CASE:
CASE valor_referência
    WHEN valor_comparado THEN
lista_declarações
    WHEN valor_comparado THEN
lista_declarações
...
    ELSE lista_declarações
END CASE;

 */

-- EXEMPLO USANDO O IF

DELIMITER //
CREATE FUNCTION calcula_imposto(salario DEC(8,2))
RETURNS DEC(8,2)
READS SQL DATA DETERMINISTIC
BEGIN
    DECLARE valor_imposto DEC(8,2);
    IF salario < 1000.00 THEN
        SET valor_imposto = 0.00;
    ELSEIF salario < 2000.00 THEN
        SET valor_imposto = salario * 0.15;
    ELSEIF salario < 3000.00 THEN
        SET valor_imposto = salario * 0.22;
    ELSE
        SET valor_imposto = salario * 0.27;
    END IF;
    RETURN valor_imposto;
END //
DELIMITER ;

/* 
Vamos testar passando valores de salários como parâmetros.
Usaremos valores como 850, 1200, 6000 para testes:
*/

SELECT calcula_imposto(850.00);
SELECT calcula_imposto(1200);
SELECT calcula_imposto(6000);

-- EXEMPLO USANDO O CASE

DELIMITER //
CREATE FUNCTION calcula_imposto_case(salario DEC(8,2))
RETURNS DEC(8,2)
READS SQL DATA DETERMINISTIC
BEGIN
    DECLARE valor_imposto DEC(8,2);
    CASE
    WHEN salario < 1000.00 THEN
        SET valor_imposto = 0.00;
    WHEN salario < 2000.00 THEN
        SET valor_imposto = salario * 0.15;
    WHEN salario < 3000.00 THEN
        SET valor_imposto = salario * 0.22;
    ELSE
        SET valor_imposto = salario * 0.27;
    END CASE;
    RETURN valor_imposto;
END //
DELIMITER ;


SELECT calcula_imposto_case(700);
SELECT calcula_imposto_case(1700);
SELECT calcula_imposto_case(4600);

/* 
######################################################
# 43  SHOW, DESCRIBE  mysqlshow ############
######################################################
https://www.youtube.com/watch?v=5wBm1gQDhig&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=43

São usados para acessar os metadados (dados sobre dados)
Para entrar no prompt do MySQL:

Para ENTRAR no prompt do MySQL:
mysql -u root -p

Para SAIR do prompt do MySQL:
quit

 */

SHOW DATABASES;

USE db_biblioteca;

SHOW TABLES;

-- Código usado para criar a estrutura da tabela tbl_livro:
SHOW CREATE TABLE tbl_livro;

-- Ver o código usado para criar um procedimento:
SHOW CREATE PROCEDURE verpreço;

-- Ver o código usado para criar uma função:
SHOW CREATE FUNCTION calcula_desconto;

-- Informações sobre as colunas de um BD:
SHOW COLUMNS FROM tbl_editoras;

-- Informações COMPLETAS sobre as colunas de um BD:
SHOW FULL COLUMNS FROM tbl_editoras;

-- Filtragem: colunas que começam com a letra i.
SHOW COLUMNS FROM tbl_livro LIKE 'I%';

-- Filtragem: colunas com de um tipo específico:
SHOW COLUMNS FROM tbl_livro WHERE TYPE LIKE 'varchar%';

-- Permissões de um usuário, privilégios de acesso p/ um BD específico:
SHOW GRANTS FOR root@localhost;

-- Atalho p/ SHOW COLUMNS FROM. DESCRIBE NÃO SUPORTA AS CLÁUSULAS WHERE E LIKE.
DESCRIBE tbl_livro;
DESC tbl_livro;

/* 

Documentação:
https://dev.mysql.com/doc/refman/8.0/en/mysqlshow.html#option_mysqlshow_password

mysqlshow: informaçoes sobre os BDs, tabelas e colunas

NÃO roda no prompt do mysql. Roda no shell mesmo.
Deve dar 'quit' primeiro.

SINTAXE:
mysqlshow -y usuario -p [banco_de_dados [tabela [coluna]]]

NÃO precisa colocar ; ao final dos comandos (pois não está dentro do MySQL)

EXEMPLOS:

mysqlshow -y usuario -p [banco_de_dados [tabela [coluna]]]

-- VER OS BANCOS DE DADOS DISPONÍVEIS:
mysqlshow -u root -p

-- VER AS TABELAS DE UM BANCO DE DADOS:
mysqlshow -u root -p db_Biblioteca

-- VER OS CAMPOS PERTENCENTES A UMA TABELA:
mysqlshow -u root -p db_Biblioteca tbl_autores %

-- VISUALIZAR AS TABELAS CONTANDO AS COLUNAS E LINHAS (sem filtro)

mysqlshow -u root -p db_Biblioteca -vv

-- VISUALIZAR AS TABELAS CONTANDO AS COLUNAS E LINHAS (com filtro - tabelas começando com t)

mysqlshow -u root -p db_Biblioteca -vv t*

-- INFORMAÇÕES SOBRE UMA COLUNA ESPECÍFICA DE UMA TABELA:
mysqlshow -u root -p db_Biblioteca tbl_autores ID_Autor

-- NÃO PRECISA DIGITAR SENHA com --password=senha_do_BD

-- INFORMAÇÕES SOBRE UMA COLUNA ESPECÍFICA DE UMA TABELA:
mysqlshow -u root --password=admin db_Biblioteca tbl_autores ID_Autor

mysqlshow -u root --password=admin db_Biblioteca
-- ou:
mysqlshow -u root -padmin db_Biblioteca

 */


/* 
######################################################
# 44 LOOP Estruturas de Reptição: LOOP, REPEAT e WHILE ############
######################################################
https://www.youtube.com/watch?v=gH-jY2fXIJQ&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=44

Um bloco iterativo é um bloco de código que é executado repetidamente por um comando especial até que uma condição de parada o interrompa.
Um bloco interativo pode ser aninhado com outros blocos iterativos.
O MySQL possui três tipos básicos de blocos iterativos:
- LOOP;
- REPEAT;
- WHILE.

SINTAXE DO LOOP

[<rótulo>:] LOOP
declarações
END LOOP [<rótulo>];


 */

DELIMITER //
CREATE PROCEDURE acumula (limite INT)
BEGIN
    DECLARE contador INT DEFAULT 0;
    DECLARE soma INT DEFAULT 0;
    loop_teste: LOOP
        SET contador = contador + 1;
        SET soma = soma + contador;
        IF contador >= limite THEN
            LEAVE loop_teste;
		END IF;
    END LOOP loop_teste;
    SELECT soma;
END//
DELIMITER ;

CALL acumula(10);

/* 
######################################################
# 45 REPEAT ############
######################################################

[<rótulo>:] REPEAT
    declarações
UNTIL condição
END REPEAT [<rótulo>];

 */

-- Código que dá problema no 0
DROP PROCEDURE IF EXISTS acumula_repita;
DELIMITER //
CREATE PROCEDURE acumula_repita (limite TINYINT UNSIGNED)
BEGIN
    DECLARE contador TINYINT UNSIGNED DEFAULT 0;
    DECLARE soma INT DEFAULT 0;
	
    REPEAT
        SET contador = contador + 1;
        SET soma = soma + contador;
    UNTIL contador >= limite
    END REPEAT;
    SELECT soma;
END//
DELIMITER ;

CALL acumula_repita(10);
CALL acumula_repita(0); -- este resulta em valor errado, pois o contador é incrementado ANTES do teste condicional.


-- Código que NÃO dá problema no 0
DROP PROCEDURE IF EXISTS acumula_repita;
DELIMITER //
CREATE PROCEDURE acumula_repita (limite TINYINT UNSIGNED)
main: BEGIN -- colocou rótulo main em todo o bloco BEGIN - END
    DECLARE contador TINYINT UNSIGNED DEFAULT 0;
    DECLARE soma INT DEFAULT 0;
	IF limite < 1 THEN
        SELECT 'O valor deve ser maior que zero.' AS Erro;
        LEAVE main;
    END IF;
    REPEAT
        SET contador = contador + 1;
        SET soma = soma + contador;
    UNTIL contador >= limite
    END REPEAT;
    SELECT soma;
END//
DELIMITER ;

CALL acumula_repita(10);
CALL acumula_repita(0); -- este resulta em valor errado, pois o contador é incrementado ANTES do teste condicional.

/* 
######################################################
# 46 WHILE ############
######################################################
https://www.youtube.com/watch?v=6rZn8hI3FTo&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=46

[<rótulo>:] WHILE condição DO
    declarações
END WHILE [<rótulo>];

 */

DELIMITER //

CREATE PROCEDURE acumula_while (limite TINYINT UNSIGNED)
BEGIN
    DECLARE contador TINYINT UNSIGNED DEFAULT 0;
    DECLARE soma INT DEFAULT 0;

    WHILE contador < limite DO
        SET contador = contador + 1;
        SET soma = soma + contador;
    END WHILE;
    SELECT soma;
END//
DELIMITER ;

CALL acumula_while(10);
CALL acumula_while(0); -- NÃO dá erro

/* 
######################################################
# 47 ITERATE ############
######################################################
https://www.youtube.com/watch?v=etJBUJ6N3iE&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=47

ITERATE significa dentro de uma estrutura de repetição "inicie o loop novamente".
A declaração ITERATE aparece apenas dentro de estruturas LOOP, REPEAT e WHILE.

 */

-- ITERATE como o LOOP

DROP PROCEDURE IF EXISTS acumula_iterate;

DELIMITER //
CREATE PROCEDURE acumula_iterate (limite TINYINT UNSIGNED)
BEGIN

    DECLARE contador TINYINT UNSIGNED DEFAULT 0;
    DECLARE soma INT UNSIGNED DEFAULT 0;
    
    teste: LOOP

        SET contador = contador + 1;
        SET soma = soma + contador;
        
        IF contador < limite THEN
            ITERATE teste;
        END IF;
        LEAVE teste;

    END LOOP teste;
    SELECT soma;

END//
DELIMITER ;

CALL acumula_iterate(10);

-- ITERATE com o WHILE

DELIMITER //
CREATE PROCEDURE pares(limite TINYINT UNSIGNED)
main: BEGIN
    DECLARE contador TINYINT DEFAULT 0;
    meuloop: WHILE contador < limite DO
        SET contador = contador + 1;
        IF MOD(contador, 2)  THEN
            ITERATE meuloop;
        END IF;
        SELECT CONCAT(contador, ' é um número par') AS Valor;
    END WHILE;
END//
DELIMITER ;

CALL pares(20);


/* 
######################################################
# 48 Triggers ############
######################################################
https://www.youtube.com/watch?v=JOnkvqUaNOU&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=48

Triggers

"gatilho"
- Associado a uma tabela;
- Procedimento invocado quando um comando DML (Search, Update ou Delete) é executado.

Usos do trigger:
- Verificação de integridade dos dados;
- Validação dos dados;
- Rastreamento e registro de logs de atividades nas tabelas;
- Arquivamento de registros excluídos.

- Um Trigger é associado a uma tabela;
- Armazenamento no BD como um arquivo separado;
- Não são chamados diretamente, são invocados automaticamente.

SINTAXE dos Triggers:

CREATE TRIGGER nome timing operação
ON tabela
FOR EACH row
declarações

timing = BEFORE | AFTER
operação = INSERT | UPDATE | DELETE


 */

-- Criando tabela p/ visualizar o comportamento do trigger.

CREATE TABLE produto (
    idProduto INT NOT NULL AUTO_INCREMENT,
    Nome_produto VARCHAR(45) NULL,
    Preco_Normal DECIMAL(10,2) NULL,
    Preco_Desconto DECIMAL(10,2) NULL,
    PRIMARY KEY (idProduto)
);

-- Criando o Trigger:
CREATE TRIGGER tr_desconto BEFORE INSERT
ON produto
FOR EACH ROW
SET NEW.Preco_Desconto = (NEW.Preco_Normal * 0.90); -- tem que ter o NEW porque tanto o Preco_Desconto quanto o Preco_Normal ainda NÃO EXISTEM no BD. Os valores estão sendo inseridos.

INSERT INTO produto (Nome_produto, Preco_Normal)
VALUES ('Monitor', 1.00);

INSERT INTO produto (Nome_produto, Preco_Normal)
VALUES ('DVD', 10.00), ('Pendrive',18);

SELECT * FROM produto;

/* 
######################################################
# 49 Gerenciar usuários ############
######################################################
https://www.youtube.com/watch?v=75ucGdMqmds&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=49

No prompt/terminal:
mysql -u root -pSENHA

mysql -u root -padmin

SELECT User FROM mysql.user;

-- p/ saber a partird e qual host os usuários podem se comunicar.

SELECT User, Host FROM mysql.user;

-- Criar usuário

CREATE USER usuário@local IDENTIFIED BY 'senha';

local = local a partir de onde vai se logar (ex.: localhost)

Ex.:

CREATE USER nakashima@localhost IDENTIFIED BY '1234';

-- Criar usuário que tenha acesso a partir de qualquer local, remotamente inclusive (basta não identificar de onde ela se loga):

CREATE USER ana IDENTIFIED BY '1234';

-- Criar usuário sem definir a senha no momento da criação:

CREATE USER marcos@localhost;

-- Configurar uma senha posteriormente:

SET PASSWORD FOR 'marcos'@'localhost' = '1234';

-- Renomear um usuário:

RENAME USER ana TO magali;

-- Excluir um usuário:

DROP USER marcos@localhost;

DROP USER magali;

 */

-- -------------------

/* 
######################################################
# 50 Definindo privilégios - GRANT ############
######################################################
https://www.youtube.com/watch?v=Bi_HAkg_n1Q&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=50

No prompt/terminal:
mysql -u root -pSENHA

mysql -u root -padmin

SELECT User, Host FROM mysql.user;

-- 
SHOW GRANTS FOR pedro;
SHOW GRANTS FOR nakashima@localhost;

-- Criar usuário sem privilégio nenhum:
GRANT USAGE

-- Criar usuário com todos os privilégios:
GRANT ALL

WITH GRANT OPTION

-- Dar privilégios específicos:
GRANT SELECT, INSERT, UPDATE, DELETE
ON db_nome.*
TO fulano@localhost;

* = todas as tabelas.

-- Consultas específicas:
GRANT SELECT(nome_autor, sobrenome_autor), UPDATE(nome_autor)
ON db_Biblioteca.tbl_autores
TO fabio@localhost;

SHOW GRANTS FOR fabio@localhost;

REVOGAR PRIVILÉGIOS (REVOKE)

REVOKE DELETE
ON db_Biblioteca.*
FROM ana@localhost;

SHOW GRANTS FOR ana@localhost;

-- REMOVER TODOS OS PRIVILÉGIOS DE TODOS OS BANCOS DE DADOS, DE DOIS USUÁRIOS DE UMA VEZ:

REVOKE ALL, GRANT OPTION
FROM alexandre, ana@localhost;

SHOW GRANTS FOR alexandre;
SHOW GRANTS FOR ana@localhost;

 */

-- ---

/* 
######################################################
# 55 Campos gerados - VIRTUAL e STORED ############
######################################################
https://www.youtube.com/watch?v=HImNpHfuD6M&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=55

nome_coluna tipo_dados [GENERATED ALWAYS] AS expressão [VIRTUAL | STORED] constraints

VIRTUAL: o valor que vai aparecer na coluna não é efetivamente armazenado no banco físico. Ele é gerado toda vez que uma tabela é acessada, como por um SELECT;
STORED: o valor gerado é armazenado no banco de dados.

 */


CREATE DATABASE Teste_InnoDB;

USE Teste_InnoDB;

-- Exemplo com campo gerado VIRTUAL:

CREATE TABLE tbl_mult (
    ID SMALLINT PRIMARY KEY AUTO_INCREMENT,
    num1 SMALLINT NOT NULL,
    num2 SMALLINT NOT NULL,
    num3 SMALLINT GENERATED ALWAYS AS (num1 * num2) VIRTUAL
);

INSERT INTO tbl_mult (num1, num2)
VALUES (2,1), (2,2), (2,3), (2,4);

SELECT * FROM tbl_mult;

UPDATE tbl_mult
SET num2 = 8
WHERE id = 2;

SELECT * FROM tbl_mult;

-- Exemplo com campo gerado STORED:

CREATE TABLE tbl_Vendas (
    ID_Venda SMALLINT PRIMARY KEY AUTO_INCREMENT,
    Preco_Produto DECIMAL(6,2) NOT NULL,
    Qtde TINYINT NOT NULL,
    Desconto DECIMAL(4,2) NOT NULL,
    Preco_Total DECIMAL(6,2) AS (Preco_Produto * Qtde * (1 - Desconto / 100)) STORED
);

INSERT INTO tbl_vendas (Preco_Produto, Qtde, Desconto) VALUES
(50.00, 2, 20),
(65.00, 3, 15),
(100.00, 1, 12),
(132.00, 3, 18);

SELECT * FROM tbl_Vendas;

/* 
######################################################
# 56 Tipo de Enumeração: ENUM ############
######################################################
https://www.youtube.com/watch?v=Gbc6QkeNlVM&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=56

Cria enumerações (lista de valores permissíveis de valores em uma tabela).
A grande vantagem é economia de espaço, pois quando declara, os dados armazenados vão ocupar 1 ou no máximo 2 bytes, dependendo do tamanho da informação colocada lá dentro.
Fica inviabilizada a inserção que não existe na lista ENUM.

Trabalha de forma semelhante: tipo de dados SET (o professor falou que é o próximo vídeo, mas o próximo vídeo da lista é outra coisa)

 */

CREATE TABLE camisas (
    idCamisa TINYINT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(25),
    tamanho ENUM('pequena', 'média', 'grande', 'extra-grande')
);

INSERT INTO camisas (nome, tamanho) VALUES
('regata', 'grande');

SELECT * FROM camisas;

INSERT INTO camisas (nome, tamanho) VALUES
('social', 'medium'); -- <<<=== erro!

INSERT INTO camisas (nome, tamanho) VALUES
('social', 'média'),
('polo', 'pequena'),
('polo', 'grande'),
('camiseta', 'extra-grande');

-- Para saber quais são os valores que são permissíveis para a coluna:
SHOW COLUMNS
FROM camisas
LIKE 'tamanho';

-- Visualizar números de índice dos valores enumerados:
/* Com a representação abaixo, tamanho+0, é trazida a representação numérica da coluna tamanho. */
SELECT nome, tamanho+0
FROM camisas;

/* Problemas com o ORDER BY */
SELECT * FROM camisas
ORDER BY tamanho;

/* Resolvendo o problema com o ORDER BY */
SELECT * FROM camisas
ORDER BY CAST(tamanho AS CHAR);

/* 
######################################################
# 57 UNION - unir consultas ############
######################################################

Operador UNION
Combina dados provenientes de duas ou mais consultas.
Uma UNION combina as linhas de dois ou mais conjuntos de resultados.
Cada declaração SELECT deve ter o mesmo número de colunas, tipos de dados e ordem das colunas.

Sintaxe:

SELECT declaração1
UNION [ALL]
SELECT declração2
UNION [ALL]
SELECT declaração3 ...
[ORDER BY colunas];

obs.: esse ORDER BY é usando-se as colunas que foram utilizada na primeira declaração SELECT

Exemplo 01:
Retornar nomes de livros e preços dos livros.
Caso o preço do livro seja igual ou superior a R$ 60,00, mostrar a mensagem "Livro Caro" em uma coluna à direita no resultado da consulta.
Caso contrário, mostrar a mensagem "Preço Razoável".
Ordenar por preço, do mais barato para o mais caro.
Essa conslta não é possível de fazer sem o operador UNION, porque na verdade são DUAS consultas: a primeira consulta para verificar se os livros custam mais que R$ 60, e a segunda consulta se eles custam menos que R$ 60.
 */

SELECT * FROM tbl_livros;

-- Exemplo 01:
/* Obs.: nos códigos abaixos, foi utilizado ALIAS implicitamente (sim, é possível usar ALIAS sem o AS) */

use db_biblioteca;

SELECT
Nome_Livro Livro,
Preco_Livro Preço,
'Livro Caro' Resultado
FROM tbl_livro
WHERE Preco_Livro >= 60.00
UNION
SELECT
Nome_Livro Livro,
Preco_Livro Preço,
'Preço Razoável' Resultado
FROM tbl_livro
WHERE Preco_Livro < 60.00
ORDER BY Preço;

/* 
Exemplo 02:
Retornar nomes de livros, preços e datas de publicação dos livros.
Caso a data de publicação seja anterior a 15/04/202, mostrar o preço acrescido de 15% em seu valor.
Caso o livro custe mais de 65 reais, descontar 10% em seu valor.
 */

SELECT
Nome_Livro Livro,
Data_Pub 'Data de Publicação',
Preco_Livro 'Preço Normal',
Preco_Livro * 0.90 'Preço Ajustado'
FROM tbl_livro
WHERE Preco_Livro > 65.00
UNION
SELECT
Nome_Livro Livro,
Data_Pub 'Data de Publicação',
Preco_Livro 'Preço Normal',
Preco_Livro * 1.15 'Preço Ajustado'
FROM tbl_livro
WHERE Data_Pub < '20120415';

/* 
######################################################
# 60 Eventos - agendamento ############
######################################################
https://www.youtube.com/watch?v=98_aPgTlNi8&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=60

São eventos agendados.
Tarefa que é executada de acordo com um agendamento prévio.

O agendamento de um evento pode ser de dois tipos:
- Agendamento único: Ocorre apenas uma vez, em um momento especificado;
- Agendamento recorrente: Se repete em intervalos de tempo configurados.

Variável event_scheduler
Para trabalhar com eventos, é necessário ativar o agendador de eventos (event scheduler). Por padrão, está desligado.

Verificar o estado do agendador de eventos:
SHOW VARIABLES LIKE 'event%';
Variável: event_scheduler

Ativar / desativar o agendador de eventos:
SET GLOBAL event_scheduler = ON | OFF

CREATE EVENT

CREATE EVENT nome_evento
ON SCHEDULE
    {AT timestamp | EVERY intervalo
    [STARTS timestamp] [ENDS timestamp]}
    [ON COMPLETION PRESERVE]
DO
    bloco_comandos_SQL || procedimentos

-- ---------
ALTER EVENT
Podemos alterar um evento já criado por meio da declaração ALTER EVENT

ALTER EVENT nome_evento AÇÃO

Com essa declaração é possível habilitar ou desabilitar um evento, ou renomeá-lo.

AÇÃO inclui DISABLE, ENABLE, RENAME

-- ----------
SHOW EVENTS
A declaração SHOW EVENTS permite visualizar os eventos programados no banco de dados.

Sintaxe:
SHOW EVENTS;
SHOW EVENTS FROM banco_dados;

-- ----------
DROP EVENTS
Podemos excluir um evento com a declaração DROP EVENT.
Sintaxe:
DROP EVENT [IF EXISTS] nome_evento;

 */

SHOW VARIABLES LIKE 'event%';

SET GLOBAL event_scheduler = ON;

SELECT * FROM tbl_editoras;

-- Exemplo 01 - eventos

DELIMITER //
CREATE EVENT insert_imediato
ON SCHEDULE AT CURRENT_TIMESTAMP
DO
BEGIN
     INSERT INTO tbl_editoras(Nome_Editora) VALUES
     ('Bóson Books');
END//
DELIMITER ;

SHOW EVENTS FROM db_biblioteca;

-- Exemplo 02 - Eventos - agendando p/ o futuro
/* ESSE ABAIXO NÃO FUNCIONOU!!!!!!!!!! NÃO IDENTIFICOU NO SHOW EVENTS !!!!!! */

DELIMITER //
CREATE EVENT insert_em_um_mes
ON SCHEDULE AT NOW() + INTERVAL 1 MONTH
DO
BEGIN
     INSERT INTO tbl_editoras(Nome_Editora) VALUES
     ('Tech Books Brazil');
END//
DELIMITER ;

-- É possível ver em:
SHOW EVENTS FROM db_biblioteca;

-- EXEMPLO 03 - Eventos - Mensal
/* ESSE ABAIXO FUNCIONOU!!!!!!!!!! NÃO IDENTIFICOU NO SHOW EVENTS !!!!!! */

DELIMITER //
CREATE EVENT insert_mensal
ON SCHEDULE EVERY 1 MONTH
STARTS '2021-01-30'
ENDS '2021-10-30' -- <<== A DATA DE FIM (essa linha) É OPCIONAL!!!
DO
BEGIN
     INSERT INTO tbl_editoras(Nome_Editora) VALUES
     ('Tech Books Brazil');
END//
DELIMITER ;

SHOW EVENTS FROM db_biblioteca;

-- Para EXCLUIR um evento: (DROP EVENT nome_do_evento;)
DROP EVENT insert_em_um_mes;

/* 
######################################################
# 61 Subconsultas ############
######################################################
https://www.youtube.com/watch?v=2qCLpE1NZ8c&list=PLucm8g_ezqNrWAQH2B_0AnrFY5dJcgOLR&index=61

 */

USE db_biblioteca;

/* 
SINTAXE:

SELECT coluna(s)
FROM tabela(s)
WHERE coluna operador (SELECT coluna FROM tabela WHERE condições)
ORDER BY;

Observações (regras básicas p/ subconsultas):
- sempre entre parênteses;
- dentro da subconsulta, deve ter uma ou mais consultas, que devem corresponder às que estão na cláusula externa;
- não dá pra usar um ORDER BY dentro, mas apenas DEPOIS da subconsulta - a ordenação é sempre feita na consulta externa, não interna.
- não dá pra usar o operador BETWEEN na consulta externa quando tem uma subconsulta, mas dá pra usar dentro da subconsulta;
- as subconsultas podem ser usadas não apenas com INSERT, mas tambem com INSERT, UPDATE e DELETE.
 */

-- exemplos
/* Sei o nome da editora, mas não sei o ID dela
é possível pesquisar ou com JOIN ou também com SUBCONSULTA
*/

SELECT Nome_livro, Preco_livro, ID_Editora
FROM tbl_livro
WHERE ID_Editora = 
    (SELECT ID_Editora
    FROM tbl_editoras
    WHERE Nome_Editora = 'Willey');

-- EXEMPLO 2 (usando UPDATE):
/* Atualizar os livros da editora Microsoft Press
Tenho o ID, mas não o nome.
Dá pra fazer subconsulta ou com join
 */

UPDATE tbl_livro
SET Preco_Livro = Preco_Livro * 1.12
WHERE ID_EDITORA = (
    SELECT ID_Editora
    FROM tbl_editoras
    WHERE Nome_Editora = 'Microsoft Press'
);

