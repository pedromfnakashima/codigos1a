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

from dateutil.relativedelta import relativedelta

def f(nascimento):
    r = relativedelta(pd.to_datetime('today'), nascimento) 
    return r.years

df_tse_1['idade'] = df_tse_1['DT_NASCIMENTO'].apply(f)


############################################################

colunas = ['NM_URNA_CANDIDATO',
           'DT_NASCIMENTO',
           'idade',
           'DS_CARGO',
           'SG_PARTIDO',
           'DT_NASCIMENTO',
           'DS_SIT_TOT_TURNO']

filtro = df_tse_1['DS_SIT_TOT_TURNO'].str.contains('^eleito', case=False, regex=True)
eleitos = df_tse_1.loc[filtro, :]

eleitos.set_index('NM_CANDIDATO', inplace=True)

eleitos.loc['ONEVAN JOSÉ DE MATOS']

eleitos.sort_values('idade', ascending=False, inplace=True)

eleitos.iloc[0:11, 0:2]

quem = ['LONDRES MACHADO',
        'ONEVAN JOSÉ DE MATOS']

eleitos.loc[quem, ['idade','DS_CARGO', 'SG_PARTIDO']]

############################################################

caminho = Path(r'C:\Users\pedro\bd\TEMÁTICO\TSE\votacao_secao_2018_MS.csv')
caminho


resultado = pd.read_csv(caminho,
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

resultado.dtypes

# Deleta nulos e votos de partido

"""
NÃO DELETOU:
filtro = resultado.NM_VOTAVEL.str.contains('voto|partido', case=False, regex=True)
resultado = resultado.loc[~filtro,:]
"""
filtro = resultado.NM_VOTAVEL.str.contains('voto|partido', case=False, regex=True)
resultado = resultado.drop(resultado[filtro].index)
# NÃO DELETOU TAMBÉM!

"""
resultado.set_index('NM_VOTAVEL', inplace=True)
resultado.reset_index(inplace=True)

filtro = resultado['NM_VOTAVEL'].str.contains('^onevan', case=False, regex=True)
resultado.loc[filtro, ['NM_VOTAVEL', 'NR_SECAO', 'QT_VOTOS']]

resultado.loc['ONEVAN JOSÉ DE MATOS']
"""


def minha_agregacao(x):
    novo = {
        'soma_votos': x['QT_VOTOS'].sum()
        }
    return pd.Series(novo)

qtd_votos = resultado.groupby(['NM_VOTAVEL']).apply(minha_agregacao)

qtd_votos.sort_values('soma_votos', ascending=False)

############################################################

tudo = pd.merge(eleitos, qtd_votos, left_index=True, right_index=True)

tudo = tudo.sort_values('soma_votos', ascending=False)
