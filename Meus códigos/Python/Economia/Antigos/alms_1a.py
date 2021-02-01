
import pandas as pd
from pathlib import Path

arquivoxlsx = Path(r'F:\bd\TEMÁTICO\Legislativo MS\alms_bd.xlsx')

L10_Deps = pd.read_excel(arquivoxlsx, sheet_name='Leg10_Deputados')
L10_Deps['_key'] = L10_Deps['_key'].str.replace('"','')
L10_Deps['Nome'] = L10_Deps['Nome'].str.replace('"','')

Comissoes = pd.read_excel(arquivoxlsx, sheet_name='Comissoes')
Comissoes['_key'] = Comissoes['_key'].str.replace('"','')
Comissoes['Nome'] = Comissoes['Nome'].str.replace('"','')

Partidos = pd.read_excel(arquivoxlsx, sheet_name='Partidos')
Partidos['_key'] = Partidos['_key'].str.replace('"','')
Partidos['Nome'] = Partidos['Nome'].str.replace('"','')


SL2018_Comissoes = pd.read_excel(arquivoxlsx, sheet_name='2018_Comissoes')
SL2018_Comissoes['_from'] = SL2018_Comissoes['_from'].str.replace('"','')
SL2018_Comissoes['_to'] = SL2018_Comissoes['_to'].str.replace('"','')
SL2018_Comissoes['Titular'] = SL2018_Comissoes['Titular'].str.replace('"','')
SL2018_Comissoes['Cargo'] = SL2018_Comissoes['Cargo'].str.replace('"','')
SL2018_Comissoes['Tipo'] = SL2018_Comissoes['Tipo'].str.replace('"','')

SL2018_Comissoes['_from'] = SL2018_Comissoes['_from'].str.replace('.*/','', regex=True)
SL2018_Comissoes['_to'] = SL2018_Comissoes['_to'].str.replace('.*/','', regex=True)

del SL2018_Comissoes['Tipo']

Do_Partido = pd.read_excel(arquivoxlsx, sheet_name='Rel_Partidos')

Do_Partido['_from'] = Do_Partido['_from'].str.replace('"','')
Do_Partido['_to'] = Do_Partido['_to'].str.replace('"','')

del Do_Partido['Tipo']

arquivoxlsx = Path(r'F:\bd\TEMÁTICO\Legislativo MS\alms_bd_novo.xlsx')

with pd.ExcelWriter(arquivoxlsx) as writer:
    L10_Deps.to_excel(writer, sheet_name='PESSOAS', index=False)
    Comissoes.to_excel(writer, sheet_name='COMISSOES', index=False)


converte_data = lambda x: pd.to_datetime(x, format='%d/%m/%Y', errors='coerce')

############################################################
############################################################
############################################################


arquivo = Path(r'F:\bd\TEMÁTICO\TSE\consulta_cand_2018\consulta_cand_2018_MS.csv')

df_tse = pd.read_csv(arquivo,
                       encoding = 'latin',
                       delimiter = ';',
                       engine = "python")


df_tse.dtypes

df_tse['NR_CPF_CANDIDATO'].duplicated().sum()

duplicados = df_tse[df_tse['NR_CPF_CANDIDATO'].duplicated()]

Pessoas = df_tse.loc[:,['NM_CANDIDATO', 'NM_URNA_CANDIDATO', 'NR_CPF_CANDIDATO', 'NM_EMAIL', 'SG_UF_NASCIMENTO', 'NM_MUNICIPIO_NASCIMENTO', 'DT_NASCIMENTO', 'NR_IDADE_DATA_POSSE', 'NR_TITULO_ELEITORAL_CANDIDATO', 'DS_GENERO', 'DS_GRAU_INSTRUCAO', 'CD_ESTADO_CIVIL', 'DS_COR_RACA', 'DS_OCUPACAO']]

Pessoas.duplicated(keep = False)


Pessoas['DS_OCUPACAO'].value_counts(normalize=True)































