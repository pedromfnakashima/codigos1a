class tse_colunas():
    candidatos = [
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
    
    votacao = [
        'ANO_ELEICAO',
        'NR_TURNO',
        'DT_ELEICAO',
        'CD_MUNICIPIO',
        'NM_MUNICIPIO',
        'NR_ZONA',
        'NR_SECAO',
        'DS_CARGO',
        'NR_VOTAVEL',
        'NM_VOTAVEL',
        'QT_VOTOS'
    ]

#############################################################
import pandas as pd
from pathlib import Path
caminho = Path(r'C:\Users\pedro\bd\TEMÁTICO\TSE\consulta_cand_2018\consulta_cand_2018_MS.csv')
caminho


#f1 = lambda x: pd.to_numeric(x.replace("R$ ","").replace(",","."), errors="coerce")
converte_data = lambda x: pd.to_datetime(x, format='%d/%m/%Y', errors='coerce')


df_tse_1 = pd.read_csv(caminho,
                       usecols = tse_colunas.candidatos,
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

############################################################

dep_est_eleitos = df_tse_1.loc[:, ['DS_CARGO',
                                    'NM_URNA_CANDIDATO',
                                    'SG_PARTIDO',
                                    'DS_CARGO',
                                    'DT_NASCIMENTO',
                                    'DS_SIT_TOT_TURNO']]\
.loc[df_tse_1['DS_CARGO'].str.contains('ESTADUAL')]\
.loc[df_tse_1['DS_SIT_TOT_TURNO'].str.contains('^ELEITO', regex=True)]

############################################################
############################################################

caminho = Path(r'C:\Users\pedro\bd\TEMÁTICO\TSE\votacao_secao_2018_MS.csv')
caminho


df_tse_2 = pd.read_csv(caminho,
                       usecols = tse_colunas.votacao,
                       encoding = 'latin',
                       dtype = {'NM_MUNICIPIO': 'category',
                                'DS_CARGO': 'category',
                                'NM_PARTIDO': 'category',
                                'NM_VOTAVEL': 'category'},
                       delimiter = ';',
                       converters={"DT_NASCIMENTO": converte_data},
                       true_values=["S"],
                       false_values=["N"],
                       engine = "python")

df_tse_2.dtypes
print(df_tse_2.head())

##########################################
##########################################

dep_est_votos = df_tse_2.loc[:, ['NM_MUNICIPIO',
                                    'NR_ZONA',
                                    'NR_SECAO',
                                    'DS_CARGO',
                                    'NR_VOTAVEL',
                                    'NM_VOTAVEL',
                                    'QT_VOTOS']]\
.loc[df_tse_2['DS_CARGO'].str.contains('ESTADUAL')]\
.groupby('NM_VOTAVEL').agg({'QT_VOTOS': 'sum'})\
.sort_values(['QT_VOTOS'], ascending=[False])

dep_est_votos.head(10)

##########################################
##########################################

dep_est_votos = df_tse_2.loc[:, ['NM_MUNICIPIO',
                                    'NR_ZONA',
                                    'NR_SECAO',
                                    'DS_CARGO',
                                    'NR_VOTAVEL',
                                    'NM_VOTAVEL',
                                    'QT_VOTOS']]\
.loc[df_tse_2['DS_CARGO'].str.contains('ESTADUAL')]\
.groupby(['NM_VOTAVEL']).agg({'QT_VOTOS': ['sum', 'max']})\
.sort_values([('QT_VOTOS','sum'),('QT_VOTOS','max')], ascending=[False,False])

dep_est_votos.head(10)

##########################################

dep_est_votos = df_tse_2.loc[:, ['NM_MUNICIPIO',
                                    'NR_ZONA',
                                    'NR_SECAO',
                                    'DS_CARGO',
                                    'NR_VOTAVEL',
                                    'NM_VOTAVEL',
                                    'QT_VOTOS']]\
.loc[df_tse_2['DS_CARGO'].str.contains('ESTADUAL')]\
.groupby(['NM_VOTAVEL']).agg({'QT_VOTOS': ['sum', 'max']})\
.sort_values([('QT_VOTOS','sum'),('QT_VOTOS','max')], ascending=[False,False])

dep_est_votos.head(10)


##########################################

grupo_deps = df_tse_2.loc[:, ['NM_MUNICIPIO',
                                    'NR_ZONA',
                                    'NR_SECAO',
                                    'DS_CARGO',
                                    'NR_VOTAVEL',
                                    'NM_VOTAVEL',
                                    'QT_VOTOS']]\
.loc[df_tse_2['DS_CARGO'].str.contains('ESTADUAL')]\
.groupby(['NM_VOTAVEL']).agg({'QT_VOTOS': ['sum', 'max']})

contar = grupo_deps.get_group('RENAN BARBOSA CONTAR')


##########################################
##########################################
##########################################


dep_est_votos = df_tse_2.loc[:, ['NM_MUNICIPIO',
                                    'NR_ZONA',
                                    'NR_SECAO',
                                    'DS_CARGO',
                                    'NR_VOTAVEL',
                                    'NM_VOTAVEL',
                                    'QT_VOTOS']]\
.loc[df_tse_2['DS_CARGO'].ne('VOTO BRANCO')]\
.loc[df_tse_2['DS_CARGO'].str.contains('ESTADUAL')]



dep_est_votos.head(10)


def f_agrega(x):
    nomes = {
        'Votos soma': x['QT_VOTOS'].sum(),
        'Votos média': x['QT_VOTOS'].mean(),
        'Votos DP':  x['QT_VOTOS'].std(),
        'Votos Max':  x['QT_VOTOS'].max()
        }

    return pd.Series(nomes)


#dep_est_votos.groupby('NM_VOTAVEL').apply(f_agrega)


agregado = dep_est_votos.groupby('NM_VOTAVEL').apply(f_agrega)\
.sort_values(['Votos soma'], ascending=[False])

##########################################
##########################################
##########################################

agregado.head(5)
agregado.head(1)

teste = agregado.filter(items=['VOTO BRANCO','VOTO NULO','Partido'], axis=0)

teste = agregado.filter(like='Partido', axis=0)
teste = agregado.filter(like='VOTO', axis=0)
teste = agregado.filter(like='média', axis=1)


teste = agregado.loc[agregado.index == 'VOTO BRANCO']
teste = agregado.loc[agregado.index == 'VOTO NULO']

teste = agregado.loc[agregado.index.str.contains('VOTO')]
teste = agregado.loc[agregado.index.str.contains('Partido')]

teste = agregado.loc[agregado.index.str.contains('voto')] # nada retorna
teste = agregado.loc[agregado.index.str.contains('voto', case=False)] # retorna VOTO

teste = agregado.loc[agregado.index.str.contains('(voto|partido)', case=False, regex=True)]
teste = agregado.loc[agregado.index.str.contains('voto|partido', case=False, regex=True)]

import re
teste = agregado.loc[agregado.index.str.contains('voto|partido', flags=re.IGNORECASE, regex=True)]

teste = agregado.loc[agregado.index.str.replace('VOTO','votação')]

"""
MENSAGEM DE ALTERTA:
__main__:1: FutureWarning: 
Passing list-likes to .loc or [] with any missing label will raise
KeyError in the future, you can use .reindex() as an alternative.

See the documentation here:
https://pandas.pydata.org/pandas-docs/stable/indexing.html#deprecate-loc-reindex-listlike
"""
# ver arquivo: pandas_index.py

teste = agregado.reindex(agregado.index.str.replace('VOTO','escolhas'), axis="rows")






























