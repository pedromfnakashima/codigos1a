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

type(df_tse_1)