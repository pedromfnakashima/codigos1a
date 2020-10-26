import pandas as pd

class importa():
    
    pasta = r'C:\Users\pedro\bd\TEMÁTICO\TSE\consulta_cand_2018'
    arquivo = r'\consulta_cand_2018_MS.csv'
    caminho_completo = (pasta + arquivo).replace("\\", "/")
    
    def importa_csv(self, lista):
        df = pd.read_csv(self.caminho_completo,
                         usecols = lista,
                         encoding = 'latin',
                         delimiter = ';')
        return df



class tse_colunas():
    lista1 = [
        'ANO_ELEICAO',
        'NR_TURNO',
        'DT_ELEICAO',
        'DS_CARGO',
        'NM_CANDIDATO',
        'NM_URNA_CANDIDATO',
        'NR_CPF_CANDIDATO',
        'NM_EMAIL',
        'TP_AGREMIACAO',
        'NR_PARTIDO',
        'SG_PARTIDO',
        'NM_PARTIDO',
        'NM_COLIGACAO',
        'DS_COMPOSICAO_COLIGACAO',
        'SG_UF_NASCIMENTO',
        'NM_MUNICIPIO_NASCIMENTO',
        'DT_NASCIMENTO',
        'DS_GENERO',
        'DS_GRAU_INSTRUCAO',
        'DS_ESTADO_CIVIL',
        'DS_COR_RACA',
        'DS_OCUPACAO',
        'DS_SIT_TOT_TURNO',
        'ST_REELEICAO'
    ]
    
    lista2 = [
        'ANO_ELEICAO',
        'NR_TURNO',
        'DT_ELEICAO'
    ]




del lista1, lista2

df_tse_1 = pd.read_csv(caminho_completo,
                       usecols = lista1,
                       encoding = 'latin',
                       delimiter = ';')

df_tse_2 = pd.read_csv(caminho_completo,
                       usecols = lista2,
                       encoding = 'latin',
                       delimiter = ';')

df_tse_3 = pd.read_csv(caminho_completo,
                       usecols = lambda x: x not in lista1,
                       encoding = 'latin',
                       delimiter = ';')


del df_tse_1

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 


import pandas as pd
from pathlib import Path
caminho = Path(r'C:\Users\pedro\bd\TEMÁTICO\TSE\consulta_cand_2018\consulta_cand_2018_MS.csv')
caminho


#f1 = lambda x: pd.to_numeric(x.replace("R$ ","").replace(",","."), errors="coerce")
converte_data = lambda x: pd.to_datetime(x, format='%d/%m/%Y', errors='coerce')


df_tse_1 = pd.read_csv(caminho,
                       usecols = tse_colunas.lista1,
                       encoding = 'latin',
                       dtype = {'DS_CARGO': 'category',
                                'TP_AGREMIACAO': 'category',
                                'NM_PARTIDO': 'category',
                                 'NM_COLIGACAO': 'category',
                                 'DS_COMPOSICAO_COLIGACAO': 'category',
                                 'SG_UF_NASCIMENTO': 'category',
                                 'NM_MUNICIPIO_NASCIMENTO': 'category',
                                 'DS_GENERO': 'category',
                                 'DS_GRAU_INSTRUCAO': 'category',
                                 'DS_ESTADO_CIVIL': 'category',
                                 'DS_COR_RACA': 'category',
                                 'DS_OCUPACAO': 'category',
                                 'DS_SIT_TOT_TURNO': 'category'},
                       delimiter = ';',
                       converters={"DT_NASCIMENTO": converte_data},
                       true_values=["S"],
                       false_values=["N"],
                       engine = "python")

# Funcionou com o Path!
df_tse_1.dtypes
print(df_tse_1.head())

########################################################

df_tse_1 = pd.read_csv(caminho,
                       usecols = tse_colunas.lista1,
                       encoding = 'latin',
                       delimiter = ';',
                       converters={"DT_NASCIMENTO": converte_data},
                       true_values=["S"],
                       false_values=["N"],
                       engine = "python")

# Funcionou com o Path!
df_tse_1.dtypes
print(df_tse_1.head())


##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

## Filtros

df_tse_1.loc[df_tse_1['NM_CANDIDATO'].str.contains("PICARELLI")]

resultado1 = df_tse_1.loc[df_tse_1['NM_URNA_CANDIDATO']
    .str.contains("BARBOSINHA"),
    ['NM_CANDIDATO', 'NM_URNA_CANDIDATO']]


resultado1 = df_tse_1.loc[df_tse_1['DS_CARGO'].str.contains("ESTADUAL"),
    ['DS_CARGO', 'NM_URNA_CANDIDATO', 'SG_PARTIDO', 'DT_NASCIMENTO', 'DS_GENERO', 'DS_GRAU_INSTRUCAO', 'DS_ESTADO_CIVIL', 'DS_SIT_TOT_TURNO']]


resultado1 = df_tse_1.loc[(df_tse_1['DS_CARGO'].str.contains("ESTADUAL"),
                          df_tse_1['DS_SIT_TOT_TURNO'] == 'ELEITO'),
    ['DS_CARGO', 'NM_URNA_CANDIDATO', 'SG_PARTIDO', 'DT_NASCIMENTO', 'DS_GENERO', 'DS_GRAU_INSTRUCAO', 'DS_ESTADO_CIVIL', 'DS_SIT_TOT_TURNO']]

resultado1 = df_tse_1.loc[:,['DS_CARGO', 'NM_URNA_CANDIDATO']]
resultado2 = df_tse_1.loc[:,['DS_CARGO', 'NM_URNA_CANDIDATO', 'SG_PARTIDO', 'DT_NASCIMENTO', 'DS_GENERO', 'DS_GRAU_INSTRUCAO', 'DS_ESTADO_CIVIL', 'DS_SIT_TOT_TURNO']]\
    .loc[df_tse_1['DS_CARGO'].str.contains("ESTADUAL")]\
    .loc[df_tse_1['DS_SIT_TOT_TURNO'] == 'ELEITO']

##########################################

resultado1 = df_tse_1.loc[:, ['DS_CARGO',
                              'NM_URNA_CANDIDATO',
                              'SG_PARTIDO',
                              'DT_NASCIMENTO',
                              'DS_GENERO',
                              'DS_GRAU_INSTRUCAO',
                              'DS_ESTADO_CIVIL',
                              'DS_SIT_TOT_TURNO']]\
.loc[df_tse_1['DS_CARGO'].str.contains("ESTADUAL")]\
.loc[df_tse_1['DS_SIT_TOT_TURNO'] == 'SUPLENTE']

##########################################

resultado1 = df_tse_1.loc[:, ['NM_URNA_CANDIDATO',
                              'SG_PARTIDO',
                              'DT_NASCIMENTO',
                              'DS_GENERO',
                              'DS_GRAU_INSTRUCAO',
                              'DS_ESTADO_CIVIL',
                              'DS_SIT_TOT_TURNO']]\
.loc[df_tse_1['DS_CARGO'].str.contains('ESTADUAL')]\
.loc[df_tse_1['DS_SIT_TOT_TURNO'].str.contains('^ELEITO', regex=True)]

len(resultado1)

##########################################











