# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 11:16:28 2020

@author: pedro

Nesse arquivo, há metodologia de busca nas colunas.
No arquivo ifgf_01b.py, não há.
"""
#############################
##### CONFIGURAÇÃO GERAL ####
#############################
globals().clear()
""" Mudar diretório """
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    print('\nLogado de casa')
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('\nLogado da salj-alems')
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados' / 'Firjan'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())
##########################################################################################################
##########################################################################################################
##########################################################################################################

import numpy as np
import pandas as pd


ifgf_2019_capitais = pd.read_excel('Ranking-IFGF-2019_capitais.xlsx', sheet_name='IFGF Geral', skiprows=1)
print(ifgf_2019_capitais.dtypes)
ifgf_2019_capitais.rename(columns={'Município':'mun_nome', 'Ranking IFGF Geral':'rk_geral','Unnamed: 1': 'rk_estadual'}, inplace=True)
ifgf_2019_capitais.drop([0], axis=0, inplace=True)
ifgf_2019_capitais['mun_nome'] = ifgf_2019_capitais['UF'] + '-' + ifgf_2019_capitais['mun_nome']
ifgf_2019_capitais['rk_geral'] = ifgf_2019_capitais['rk_geral'].astype('int')
ifgf_2019_capitais['rk_estadual'] = ifgf_2019_capitais['rk_estadual'].astype('int')

# Colocar os códigos dos municípios
pasta = caminho_wd = caminho_base / 'Dados'
municipios = pd.read_excel(pasta / 'municipios.xlsx', sheet_name='municipios', skiprows=0, dtype={'capital': np.bool})
print(municipios.dtypes)

# Fazer o merge dos datasets
ifgf_2019_capitais = ifgf_2019_capitais.merge(municipios, how='left', left_on='mun_nome', right_on='mun_nome')

###########################################
## REPLICANDO #############################
###########################################

'''
TESTES
Nomes dos arquivos .csv nos .zip:
RGF: finbraRGF.csv
RREO: finbraRREO.csv
Contas anuais: finbra.csv
'''


###########################################
## REPLICANDO ## AUTONOMIA ################
###########################################
"""
Capacidade de financiar a estrutura administrativa
(Receita Local - Estrut Admin) / Receita Corrente Líquida
"""

import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    print('\nLogado de casa')
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('\nLogado da salj-alems')
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

caminho_wd = caminho_base / 'Dados' / 'Siconfi' / 'Contas Anuais - Municípios' / 'Despesas por Função'
os.chdir(caminho_wd)

def gera_df(nome_zip, caminho):
    import zipfile
    import io
    #from pathlib import Path
    import pandas as pd
    
    caminho = Path(caminho) / nome_zip
    
    #os.chdir(caminho)
    
    #print(nome_zip)
    #print(caminho)
    
    
    with zipfile.ZipFile(caminho, 'r') as zf:
        csv_nome = zf.namelist()[0]
        with io.TextIOWrapper(zf.open(csv_nome), encoding="latin") as f:
            f_contents = f.readline()
            lista = [f_contents]
            contador = 0
            while f_contents.find(';') == -1:
                contador += 1
                f_contents = f.readline()
                lista.append(f_contents)
    df = pd.read_csv(caminho, compression='zip', header=0, sep=';', decimal=',', quotechar='"', encoding = 'latin', skiprows=contador)
    
    li_exercicio = lista[0].replace('\n','').split(':')
    li_exercicio = [elemento.strip() for elemento in li_exercicio]
    ano = li_exercicio[1]
    
    df['exercicio'] = int(ano)
    
    bool_RGF = csv_nome.find('RGF')
    bool_RREO = csv_nome.find('RREO')
    
    if bool_RGF > 0 or bool_RREO > 0:
        #print('Ou é RGF ou é RREO.')
        
        li_periodo = lista[1].replace('\n','').split(':')
        li_periodo = [elemento.strip() for elemento in li_periodo]
        li_periodo = li_periodo[1]
        li_periodo = li_periodo.split('.')
        li_periodo = [elemento.strip() for elemento in li_periodo]
        periodo_num = li_periodo[0][0]
        periodo_unidade = li_periodo[1]
        
        # Adiciona unidade ao DF (ex.: bimestre, quadrimestre)
        df[periodo_unidade] = int(periodo_num)
    else:
        #print('É contas anuais.')
        pass
    # Manipula coluna Instituição
    """ Usando regex """
    df['Instituição'] = df['Instituição'].str.replace('\sdo[\s\w]+', '')
    """ Usando filtro """
    filtro = df['Instituição'].str.contains('Justiça Militar')
    df.loc[filtro, 'Instituição'] = 'Tribunal de Justiça Militar'
    
    return df
    
    

#df_siconfi = gera_df('2018.zip')
#df_siconfi.rename('outro')
#print(dir(df_siconfi))


def processa_arquivos_zip(arquivo = 'todos', caminho = os.getcwd()):
    
    import zipfile
    import io
    from pathlib import Path
    
    print('Adicionados:')
    
    if arquivo == 'todos':
        import glob
        dicionario = {}
        
        for arq_nome in glob.glob('*.zip'):
            pos_ponto = arq_nome.find('.zip')
            df_nome = f'df_{arq_nome[0:pos_ponto]}'
            
            #print(f'  {df_nome}')
            print(f'  {arq_nome}')
            
            dicionario[df_nome] = gera_df(arq_nome)
        
        i = 1
        for key in dicionario.keys():
            
            if i == 1:
                novo_df = dicionario[key]
            else:
                novo_df = novo_df.append(dicionario[key])
            i += 1
    else:
        novo_df = gera_df(arquivo, caminho)
        print(f'  {arquivo}')
        
    return novo_df

#dic = processa_arquivos()

ca2018_desp_função = processa_arquivos_zip(arquivo='2018.zip',
                                           caminho=r'D:\Códigos, Dados, Documentação e Cheat Sheets\Dados\Siconfi\Contas Anuais - Municípios\Despesas por Função')

ca2018_desp_função.rename(columns={'Cod.IBGE':'mun_cod_ibge'}, inplace=True)
ca2018_desp_função = ca2018_desp_função.merge(municipios, how='left', left_on='mun_cod_ibge', right_on='mun_cod_ibge')
ca2018_desp_função = ca2018_desp_função[ca2018_desp_função['capital'] == True]
ca2018_desp_função.drop(['capital'], axis=1, inplace=True)



"""
Capacidade de financiar a estrutura administrativa
(Receita Local - Estrut Admin) / Receita Corrente Líquida

RECEITA LOCAL:
Impostos
Receita Patrimonial
Receita Agropecuária
Receita Industrial
Receita de Serviços
Cota-parte do ICMS
Cota-parte do IPVA
Cota-parte do IPI - Municípios
-> Dedução do percentual destinado ao Fundeb
    
ESTRUTURA ADMINISTRATIVA: Funções:
Administrativa
Judiciária
Essencial à Justiça
Administração

"""
######################################
# RECEITA LOCAL ######################
######################################

ca2018_rec_orc = processa_arquivos_zip(arquivo='2018.zip',
                                           caminho=r'D:\Códigos, Dados, Documentação e Cheat Sheets\Dados\Siconfi\Contas Anuais - Municípios\Receitas Orçamentárias')

ca2018_rec_orc.rename(columns={'Cod.IBGE':'mun_cod_ibge'}, inplace=True)
ca2018_rec_orc = ca2018_rec_orc.merge(municipios, how='left', left_on='mun_cod_ibge', right_on='mun_cod_ibge')
ca2018_rec_orc = ca2018_rec_orc[ca2018_rec_orc['capital'] == True]
ca2018_rec_orc.drop(['capital'], axis=1, inplace=True)

# Valores da coluna Coluna
tipos = ca2018_rec_orc['Coluna'].unique()

# Coluna da descrição: Conta

cond1 = ca2018_rec_orc['Conta'].str.contains('pat', case=False)
cond = cond1
df_filtro = ca2018_rec_orc.loc[cond, ['Conta']]

# Coluna da descrição: Conta - busca com regex

cond1 = ca2018_rec_orc['Conta'].str.contains('rece.+pa', case=False)
cond2a = ca2018_rec_orc['Coluna'].str.contains('bruta', case=False)
cond2b = ca2018_rec_orc['Coluna'].str.contains('fundeb', case=False)
cond3 = ca2018_rec_orc['mun_nome'].str.contains('belo', case=False)
cond = cond1 & (cond2a | cond2b) & cond3
df_filtro = ca2018_rec_orc.loc[cond, ['mun_nome', 'Conta', 'Coluna', 'Valor']]

del cond2

'''
Despesa LIQUIDADA
Valor na coluna :

Valores na coluna Conta:
1.1.1.0.00.0.0 - Impostos
1.3.0.0.00.0.0 - Receita Patrimonial
1.4.0.0.00.0.0 - Receita Agropecuária
1.5.0.0.00.0.0 - Receita Industrial
1.6.0.0.00.0.0 - Receita de Serviços
1.7.1.8.01.5.0 Cota-Parte do Imposto Sobre a Propriedade Territorial Rural
1.7.1.8.06.0.0 Transferência Financeira do ICMS ¿ Desoneração ¿ L.C. Nº 87/96
1.7.2.8.01.1.0 Cota-Parte do ICMS
1.7.2.8.01.2.0 Cota-Parte do IPVA
1.7.2.8.01.3.0 Cota-Parte do IPI - Municípios
'''

# 1.1.1.0.00.0.0 - Impostos e deduções
'''
Valores nas colunas:
Conta: 1.1.1.0.00.0.0 - Impostos
Colunas: Receitas Brutas Realizadas
'''

cond1 = ca2018_rec_orc['Conta'].str.contains('1.1.1.0.00.0.0 - Impostos', case=False)
cond2a = ca2018_rec_orc['Coluna'].str.contains('bruta', case=False)
cond2b = ca2018_rec_orc['Coluna'].str.contains('fundeb', case=False)
cond3 = ca2018_rec_orc['mun_nome'].str.contains('campo', case=False)
cond = cond1 & (cond2a | cond2b)# & cond3
df_filtro = ca2018_rec_orc.loc[cond, ['mun_nome', 'mun_cod_ibge', 'Conta', 'Coluna', 'Valor']]

# 1.3.0.0.00.0.0 - Receita Patrimonial
'''
Valores nas colunas:
Conta: 1.3.0.0.00.0.0 - Receita Patrimonial
Colunas:
    Receitas Brutas Realizadas
    Deduções - FUNDEB
'''
cond1 = ca2018_rec_orc['Conta'].str.contains('rec.+pat', case=False)
cond2a = ca2018_rec_orc['Coluna'].str.contains('bruta', case=False)
cond2b = ca2018_rec_orc['Coluna'].str.contains('fundeb', case=False)
cond3 = ca2018_rec_orc['mun_nome'].str.contains('campo', case=False)
cond = cond1 & (cond2a | cond2b) & cond3
df_filtro = ca2018_rec_orc.loc[cond, ['mun_nome', 'mun_cod_ibge', 'Conta', 'Coluna', 'Valor']]

# 1.4.0.0.00.0.0 - Receita Agropecuária
'''
Valores nas colunas:
Conta: 1.4.0.0.00.0.0 - Receita Agropecuária
Colunas:
    Receitas Brutas Realizadas

Das capitais, só Belo Horizonte tem

'''
cond1 = ca2018_rec_orc['Conta'].str.contains('rec.+agro', case=False)
cond2a = ca2018_rec_orc['Coluna'].str.contains('bruta', case=False)
cond2b = ca2018_rec_orc['Coluna'].str.contains('fundeb', case=False)
cond3 = ca2018_rec_orc['mun_nome'].str.contains('campo', case=False)
cond = cond1 & (cond2a | cond2b)# & cond3
df_filtro = ca2018_rec_orc.loc[cond, ['mun_nome', 'mun_cod_ibge', 'Conta', 'Coluna', 'Valor']]

# 1.5.0.0.00.0.0 - Receita Industrial
'''
Valores nas colunas:
Conta: 1.5.0.0.00.0.0 - Receita Industrial
Colunas:
    Receitas Brutas Realizadas

Das capitais, têm:
    Salvador,
    Rio (tem também "Conta" intraorçamentárias),
    Campo Grande,
    Rio Branco

'''
cond1 = ca2018_rec_orc['Conta'].str.contains('rec.+ind', case=False)
cond2a = ca2018_rec_orc['Coluna'].str.contains('bruta', case=False)
cond2b = ca2018_rec_orc['Coluna'].str.contains('fundeb', case=False)
cond3 = ca2018_rec_orc['mun_nome'].str.contains('campo', case=False)
cond = cond1 & (cond2a | cond2b)# & cond3
df_filtro = ca2018_rec_orc.loc[cond, ['mun_nome', 'mun_cod_ibge', 'Conta', 'Coluna', 'Valor']]

# 1.6.0.0.00.0.0 - Receita de Serviços
'''
Valores nas colunas:
Conta: 1.6.0.0.00.0.0 - Receita de Serviços
Colunas:
    Receitas Brutas Realizadas

Das capitais, têm:
    Várias

Várias também tem intraorçamentárias
'''
cond1 = ca2018_rec_orc['Conta'].str.contains('rec.+serv', case=False)
cond2a = ca2018_rec_orc['Coluna'].str.contains('bruta', case=False)
cond2b = ca2018_rec_orc['Coluna'].str.contains('fundeb', case=False)
cond3 = ca2018_rec_orc['mun_nome'].str.contains('campo', case=False)
cond = cond1 & (cond2a | cond2b)# & cond3
df_filtro = ca2018_rec_orc.loc[cond, ['mun_nome', 'mun_cod_ibge', 'Conta', 'Coluna', 'Valor']]

# 1.7.1.8.01.5.0 Cota-Parte do Imposto Sobre a Propriedade Territorial Rural
'''
Valores nas colunas:
Conta: 1.7.1.8.01.5.0 Cota-Parte do Imposto Sobre a Propriedade Territorial Rural
Colunas:
    Receitas Brutas Realizadas
    Deduções - FUNDEB

Das capitais, têm:
    Praticamente todas

Nenhuma tem intraorçamentárias
'''
cond1 = ca2018_rec_orc['Conta'].str.contains('cota.+territorial', case=False)
cond2a = ca2018_rec_orc['Coluna'].str.contains('bruta', case=False)
cond2b = ca2018_rec_orc['Coluna'].str.contains('fundeb', case=False)
cond3 = ca2018_rec_orc['mun_nome'].str.contains('campo', case=False)
cond = cond1 & (cond2a | cond2b)# & cond3
df_filtro = ca2018_rec_orc.loc[cond, ['mun_nome', 'mun_cod_ibge', 'Conta', 'Coluna', 'Valor']]

df_filtro.sort_values(['mun_nome', 'Conta', 'Coluna'], ascending=[True, True, False], inplace=True)

cond1 = df_filtro['Coluna'].str.contains('receitas', case=False)
cond = cond1
df_filtro.loc[cond,'rb'] = df_filtro['Valor']

cond1 = df_filtro['Coluna'].str.contains('fundeb', case=False)
cond = cond1
df_filtro.loc[cond,'ded_fundeb'] = df_filtro['Valor']

df_rb = df_filtro[['mun_nome', 'mun_cod_ibge', 'rb']]
df_rb.dropna(inplace=True)

df_ded_fundeb = df_filtro[['mun_nome', 'mun_cod_ibge', 'ded_fundeb']]
df_ded_fundeb.dropna(inplace=True)

df_rb = df_rb.merge(df_ded_fundeb, how='left', left_on='mun_cod_ibge', right_on='mun_cod_ibge')

df_rb['final'] = df_rb['rb'] - df_rb['ded_fundeb']



'''
VERIFICAR POR QUE NÃO HÁ DADOS DE RECEITAS DE IMPOSTOS DE
BOA VISTA, PALMAS, SÃO PAULO, BRASÍLIA
mun_nome:

RR-Boa Vista
TO-Palmas
SP-São Paulo
DF-Brasília

Já sei: não tem os dados, nenhum dado desses municípios.

O IFGF SÓ PODE TER PEGO OS DADOS DO RGF E DO RREO

'''

cond1 = ca2018_rec_orc['Conta'].str.contains('rece.+pa', case=False)
cond2a = ca2018_rec_orc['Coluna'].str.contains('bruta', case=False)
cond2b = ca2018_rec_orc['Coluna'].str.contains('fundeb', case=False)
cond3 = ca2018_rec_orc['mun_nome'].str.contains('TO-Palmas', case=False)
cond = cond3
df_filtro = ca2018_rec_orc.loc[cond, ['mun_nome', 'Conta', 'Coluna', 'Valor']]





rreo2018_desp_função = processa_arquivos_zip(arquivo='2018.zip',
                                           caminho=r'D:\Códigos, Dados, Documentação e Cheat Sheets\Dados\Siconfi\Contas Anuais - Municípios\Despesas por Função')














