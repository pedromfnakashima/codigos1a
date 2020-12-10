# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:04:46 2020

@author: pedro-salj
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
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv'
os.chdir(caminho_wd)
import numpy as np
import pandas as pd

##########################################################################################################
##########################################################################################################
##########################################################################################################



#######################################################################################################

#def cgd_01a(uf, início, final, agregação):

uf = 'BR'
início='2020-10'
final='2020-10'
agregação = 'cnae_seção_cod'
#agregação = 'cnae_divisão_cod'
#agregação='cnae_grupo_cod'
#agregação='cnae_classe_cod'
#agregação='cnae_subclasse_cod'

# ----------------------------------------------------------------------------------------
pasta = caminho_base / 'Dados'
df_municipios = pd.read_excel(pasta/'municipios.xlsx', sheet_name='municipios')
df_municipios = df_municipios[['mun_cod_ibge','uf_sigla']]
# ----------------------------------------------------------------------------------------
pasta = caminho_base / 'Dados' / 'cnae e ncm'
arq_nome = 'cnae_corresp_curto.csv'
cnae_corresp_curto = pd.read_csv(pasta / arq_nome,
                              delimiter = ';',
                              decimal=',',
                              dtype='str')
arq_nome = 'cnae_corresp_longo.csv'
cnae_corresp_longo = pd.read_csv(pasta / arq_nome,
                              delimiter = ';',
                              decimal=',',
                              dtype='str')
# ----------------------------------------------------------------------------------------

def g_nome_arq(início, final, prefixo, sufixo):
    if início == final:
        arq_nome = prefixo + início.replace('-','') + sufixo
        li_arqs_nomes = [arq_nome]
    else:
        li_arqs_nomes = []
        início_com_dia = início + '-01'
        final_com_dia = final + '-01'
        df_datas = pd.to_datetime(np.arange(início_com_dia, final_com_dia, 1, dtype='datetime64[M]')).to_frame()#.reset_index()
        df_datas.rename(mapper={0:'col_data'},axis=1,inplace=True)
        
        nova_linha = pd.DataFrame({'col_data': pd.date_range(start=df_datas['col_data'].iloc[-1], periods=2, freq='MS', closed='right')})
        df_datas = df_datas.append(nova_linha)
        
        df_datas['col_data'] = df_datas['col_data'].astype('str')
        df_datas['col_data'] = (df_datas['col_data'].str.slice(0,4) + df_datas['col_data'].str.slice(4,7)).str.replace('-','')
        for index, row in df_datas.iterrows():
            arq_nome = prefixo + row['col_data'] + sufixo
            li_arqs_nomes.append(arq_nome)
    ## Retorna ##
    #print(li_arqs_nomes)
    return li_arqs_nomes

li_arquivos = g_nome_arq(início=início, final=final, prefixo='CAGEDMOV', sufixo='.csv')

for index_arq, arq_nome in enumerate(li_arquivos):
    print(arq_nome)
    
    #arq_nome = 'CAGEDMOV202009.csv'
    
    pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
    
    
    dtype = {'cnae_subclasse_cod':'str','cnae_classe_cod':'str', 'competência':'str'}
    df = pd.read_csv(pasta / arq_nome,
                     delimiter = ';',
                     decimal=',',
                     dtype=dtype)
    
    df = df.merge(df_municipios,how='left',left_on='mun_cod_ibge',right_on='mun_cod_ibge')
    
    if uf != 'BR':
        cond1 = df['uf_sigla'] == uf
        df = df.loc[cond1, :]
    
    df['year'] = df['competência'].str.slice(0,4)
    df['month'] = df['competência'].str.slice(4,6)
    df['day'] = 1
    df['dt'] = pd.to_datetime(df[['year', 'month', 'day']])
    df.drop(['year','month','day','competência'],axis=1,inplace=True)
    
    df_cnae_corresp_curto = df.merge(cnae_corresp_curto, how='left',left_on='cnae_subclasse_cod',right_on='cnae_subclasse_cod')
    df_cnae_corresp_longo = df.merge(cnae_corresp_longo, how='left',left_on='cnae_subclasse_cod',right_on='cnae_subclasse_cod')
    
    df_agregado_cnae_corresp_curto = df_cnae_corresp_curto.groupby(['dt',agregação])['saldomovimentação'].sum().to_frame().reset_index()
    df_agregado_cnae_corresp_longo = df_cnae_corresp_longo.groupby(['dt',agregação])['saldomovimentação'].sum().to_frame().reset_index()
    
    soma_df = df['saldomovimentação'].sum()
    soma_sm_cnae_corresp_curto = df_agregado_cnae_corresp_curto['saldomovimentação'].sum()
    soma_sm_cnae_corresp_longo = df_agregado_cnae_corresp_longo['saldomovimentação'].sum()
    
    print('\nSoma de saldomovimentação')
    print(f' - df: {soma_df}')
    print(f'\nSoma de saldomovimentação (Agreg: {agregação})')
    print(f' - df_cnae_corresp_curto: {soma_sm_cnae_corresp_curto}')
    print(f' - df_cnae_corresp_longo: {soma_sm_cnae_corresp_longo}\n')
    
    df_agregado_comparação = df_agregado_cnae_corresp_longo.copy()
    df_agregado_comparação = df_agregado_comparação.merge(df_agregado_cnae_corresp_curto, how='left', left_on=['dt',agregação], right_on=['dt',agregação])
    
    df_agregado_comparação['diferença'] = df_agregado_comparação['saldomovimentação_x'] - df_agregado_comparação['saldomovimentação_y']
    
    print(df_agregado_comparação['saldomovimentação_x'].sum())
    print(df_agregado_comparação['saldomovimentação_y'].sum())

    cond1 = df_agregado_comparação['diferença'] != 0
    df_agregado_comparação = df_agregado_comparação.loc[cond1,:]

    print(df_agregado_comparação['saldomovimentação_x'].sum())
    print(df_agregado_comparação['saldomovimentação_y'].sum())



















        # ATENÇÃO!!! AQUI (df_agregado) A SOMA TOTAL NÃO ESTÁ BATENDO!!!!!!!!!!!!!!!!!!!!!!
        df_agregado = df.groupby(['dt',agregação])['saldomovimentação'].sum().to_frame().reset_index()
        print(df_agregado['saldomovimentação'].sum())
        # A diferença abaixo deveria dar ZERO!!!!
        print(df_agregado['saldomovimentação'].sum() - df['saldomovimentação'].sum())
        
        
        
        df_agregado.rename(mapper={'saldomovimentação':'soma_errada'},axis=1,inplace=True)
        df2 = df.merge(df_agregado,how='outer',left_on='cnae_classe_cod',right_on='cnae_classe_cod')
        
        df2 = df2.groupby(['cnae_classe_cod'])
        
        if index_arq == 0:
            df_bruto = df_agregado.copy()
        else:
            df_bruto = df_bruto.append(df_agregado)
    
    df_bruto.index = range(len(df_bruto))
    
    return df_bruto
#######################################################################################################

df = cgd_01a(uf='BR', início='2020-10', final='2020-10', agregação='cnae_grupo_cod')

cond1 = df['dt'].dt.year == 2020
filtro = df.loc[cond1,:]
print(filtro['saldomovimentação'].sum())




#cond1 = df['cnae23_Subclasse_cod7'].isnull()
#filtro = df.loc[cond1,:]

def cgd_01b(uf, início, final, agregação):
    
    #df = cgd_01a(uf='BR', início='2020-09', final='2020-10', agregação='cnae_grupo_cod')
    
    df = cgd_01a(uf=uf, início=início, final=final, agregação=agregação)
    
    #print(df1.dtypes)
    
    #######################################################################################################
    #######################################################################################################
    #######################################################################################################
    #######################################################################################################
    #######################################################################################################
    #agregação='cnae_grupo_cod'
    
    dicionário1 = {}
    df_cp = df.copy()
    #print(df_cp.dtypes)
    
    ######################################################################################################
    ########## Mensal - Valor ############################################################################
    ######################################################################################################
    
    tot_mensal = df_cp.groupby(['dt'])['saldomovimentação'].sum().to_frame()
    tot_mensal.rename(mapper={'saldomovimentação':'total'},axis=1,inplace=True)
    tot_mensal.index.freq = 'MS'
    #dicionário1['Mensal - Valor'] = tot_mensal
    unicos = list(df_cp[agregação].unique())
    for index_unico, unico in enumerate(unicos):
        cond1 = df_cp[agregação] == unico
        filtro = df_cp.loc[cond1,['dt','saldomovimentação']]
        filtro.rename(mapper={'saldomovimentação':unico},axis=1,inplace=True)
        filtro.set_index('dt',inplace=True)
        tot_mensal = tot_mensal.merge(filtro,how='left',left_index=True,right_index=True)
    tot_mensal.fillna(0,inplace=True)
    
    # Adiciona ao dicionário
    dicionário1['Mensal - Valor'] = tot_mensal.copy()
    
    '''
    # Gera mês em string
    tot_mensal['dt_ano_mes'] = tot_mensal.index.year.astype('str') + '_' + tot_mensal.index.month.astype('str')
    # Pega o últim mês, em string, para a ordenação do df transposto com base no último mês
    ultimo = dicionário1['Mensal - Valor'].iloc[-1,-1]
    # Ordena o df em ordem decrescente
    tot_mensal.sort_index(ascending=False, inplace=True)
    # Coloca no index a variável de mês str
    tot_mensal.set_index(['dt_ano_mes'], inplace=True)
    # Transpõe DF
    df_longo = tot_mensal.T
    # Deleta a linha de total
    df_longo.drop(['total'],axis=0,inplace=True)
    # Ordena valores com base no último mês
    df_longo.sort_values(by=[ultimo],ascending=[False],inplace=True)
    '''
    
    ######################################################################################################
    ########## Acumulado no Ano - Valor ##################################################################
    ######################################################################################################
    
    df_acumAno = dicionário1['Mensal - Valor'].copy()
    df_acumAno['dt_ano'] = df_acumAno.index.year
    colunas = list(set(list(df_acumAno.columns)) - {'dt_ano'})
    for coluna in colunas:
        df_acumAno[coluna] = df_acumAno.groupby(['dt_ano'])[coluna].cumsum()
    df_acumAno.drop(['dt_ano'],axis=1,inplace=True)
    #     --->>>> Coloca no dicionário1 <<<<< ---   #
    dicionário1['Acumulado no Ano - Valor'] = df_acumAno
    
    ######################################################################################################
    ########## Acumulado em 12 meses - Valor #############################################################
    ######################################################################################################
    
    df_acum12m = dicionário1['Mensal - Valor'].copy()
    colunas = list(df_acum12m.columns)
    for coluna in colunas:
        df_acum12m[coluna] = df_acum12m[coluna].rolling(12).sum()
    df_acum12m.dropna(thresh=1, inplace=True)
    #     --->>>> Coloca no dicionário1 <<<<< ---   #
    dicionário1['Acumulado em 12 meses - Valor'] = df_acum12m
    
    ######################################################################################################
    ########## Média Móvel de 12 meses - Valor ###########################################################
    ######################################################################################################
    df_media12m = dicionário1['Mensal - Valor'].copy()
    colunas = list(df_media12m.columns)
    for coluna in colunas:
        df_media12m[coluna] = df_media12m[coluna].rolling(12).mean()
    df_media12m.dropna(thresh=1, inplace=True)
    
    #     --->>>> Coloca no dicionário1 <<<<< ---   #
    dicionário1['Média Móvel de 12 meses - Valor'] = df_media12m
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Entradas do dicionário1 até aqui \/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    l_variaveis = pd.Series(['Mensal - Valor','Acumulado no Ano - Valor','Acumulado em 12 meses - Valor','Média Móvel de 12 meses - Valor'])
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Participação /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    colunas = list(set(list(dicionário1['Mensal - Valor'].columns)) - {'total'})
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Participação')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        
        df_part = dicionário1[l_variavel].copy()
        for coluna in colunas:
            df_part[coluna] = (df_part[coluna] / df_part['total']) * 100
        
        df_part.dropna(thresh=1, inplace=True)
        df_part['total'] = 100
        #     --->>>> Coloca no dicionário1 <<<<< ---   #
        dicionário1[novo_nome] = df_part
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Variação Bruta com relação ao ano anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Variação Bruta com relação ao ano anterior')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        
        df_varB = dicionário1[l_variavel].copy()
        df_varB_L12 = df_varB.shift(periods=12)
        colunas = list(df_varB.columns)
        
        for coluna in colunas:
            df_varB[coluna] = df_varB[coluna] - df_varB_L12[coluna]
        df_varB.dropna(thresh=1, inplace=True)
        #     --->>>> Preenche NA com 0 <<<<< ---   #
        df_varB.fillna(0, inplace=True)
        #     --->>>> Coloca no dicionário1 <<<<< ---   #
        dicionário1[novo_nome] = df_varB
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Variação Percentual com relação ao ano anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Variação Percentual com relação ao ano anterior')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        
        df_varP = dicionário1[l_variavel].copy()
        df_varP_L12 = df_varP.shift(periods=12)
        colunas = list(df_varP.columns)
        
        for coluna in colunas:
            df_varP[coluna] = ((df_varP[coluna] - df_varP_L12[coluna]) / df_varP_L12[coluna]) * 100
        df_varP.dropna(thresh=1, inplace=True)
        #     --->>>> Preenche NA com 0 <<<<< ---   #
        df_varP.fillna(0, inplace=True)
        #     --->>>> Coloca no dicionário1 <<<<< ---   #
        dicionário1[novo_nome] = df_varP
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Variação Bruta com relação ao mês anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Variação Bruta com relação ao mês anterior')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        
        df_varB = dicionário1[l_variavel].copy()
        df_varB_L1 = df_varB.shift(periods=1)
        colunas = list(df_varB.columns)
        
        for coluna in colunas:
            df_varB[coluna] = df_varB[coluna] - df_varB_L1[coluna]
        df_varB.dropna(thresh=1, inplace=True)
        #     --->>>> Preenche NA com 0 <<<<< ---   #
        df_varB.fillna(0, inplace=True)
        #     --->>>> Coloca no dicionário1 <<<<< ---   #
        dicionário1[novo_nome] = df_varB
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Variação Percentual com relação ao mês anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Variação Percentual com relação ao mês anterior')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        
        df_varP = dicionário1[l_variavel].copy()
        df_varP_L1 = df_varP.shift(periods=1)
        colunas = list(df_varP.columns)
        
        for coluna in colunas:
            df_varP[coluna] = ((df_varP[coluna] - df_varP_L1[coluna]) / df_varP_L1[coluna]) * 100
        df_varP.dropna(thresh=1, inplace=True)
        #     --->>>> Preenche NA com 0 <<<<< ---   #
        df_varP.fillna(0, inplace=True)
        #     --->>>> Coloca no dicionário1 <<<<< ---   #
        dicionário1[novo_nome] = df_varP
    
    ######################################################################################################################
    ############################## Função que retorna duas listas com as variáveis mais e menos importantes ##############
    ######################################################################################################################
    
    #df = dicionário1['Acumulado em 12 meses - Valor'].copy()
    
    
    def mais_relevantes(df):
        # Copia o data frame
        df_cp = df.copy()
        # Cria coluna do mês por extenso
        df_cp['dt_ano_mes'] = df_cp.index.year.astype('str') + '_' + df_cp.index.month.astype('str')
        # Deleta coluna do total
        df_cp.drop(['total'],axis=1,inplace=True)
        # Pega o último mês, que vai servir de referência para a ordenação
        ultimo = df_cp.iloc[-1,-1]
        # Ordena o index por ordem decrescente
        df_cp.sort_index(ascending=False, inplace=True)
        # Coloca o mês string no índice
        df_cp.set_index('dt_ano_mes',inplace=True)
        # Transpõe o df
        df_longo = df_cp.T
        # Ordena pela coluna do último mês
        df_longo.sort_values(by=[ultimo],ascending=[False],inplace=True)
        # Seleciona os setores MAIS e MENOS importantes
        df_crescimento10Mais = df_longo.iloc[0:10,:]
        df_crescimentoMenos = df_longo.iloc[10:,:]
        df_crescimento10Menos = df_longo.iloc[-10:,:]
        df_crescimentoMais = df_longo.iloc[0:-10,:]
        # Coloca na lista as variáveis dos setores MAIS e MENOS importantes (usado nos loopings do próximo bloco)
        li_crescimento10Mais_variaveis = list(df_crescimento10Mais.copy().reset_index()['index'])
        li_crescimentoMenos_variaveis = list(df_crescimentoMenos.copy().reset_index()['index'])
        li_crescimento10Menos_variaveis = list(df_crescimento10Menos.copy().reset_index()['index'])
        li_crescimentoMais_variaveis = list(df_crescimentoMais.copy().reset_index()['index'])
        
        return li_crescimento10Mais_variaveis, li_crescimentoMenos_variaveis, li_crescimento10Menos_variaveis, li_crescimentoMais_variaveis, ultimo
    
    li_12m_crescimento10Mais_variaveis, li_12m_crescimentoMenos_variaveis, li_12m_crescimento10Menos_variaveis, li_12m_crescimentoMais_variaveis, ultimo = mais_relevantes(dicionário1['Acumulado em 12 meses - Valor'])
    li_1m_crescimento10Mais_variaveis, li_1m_crescimentoMenos_variaveis, li_1m_crescimento10Menos_variaveis, li_1m_crescimentoMais_variaveis, ultimo = mais_relevantes(dicionário1['Mensal - Valor'])
    
    
    ########################################################################################################
    ########### Top: Mensal, Acumulado no ano, acumulado em 12 meses, e média móvel de 12 meses ############
    ########################################################################################################
    
    
    # Coloca na lista as variáveis dos setores MAIS e MENOS importantes
    
    li_variaveis = pd.Series(['Mensal - Valor','Acumulado no Ano - Valor','Acumulado em 12 meses - Valor', 'Média Móvel de 12 meses - Valor'])
    
    # ------------------------------------------------------------------------------------------------------
    
    parametro = '1m'
    
    if parametro == '12m':
        li_crescimento10Mais_variaveis = li_12m_crescimento10Mais_variaveis
        li_crescimentoMenos_variaveis = li_12m_crescimentoMenos_variaveis
        li_crescimento10Menos_variaveis = li_12m_crescimento10Menos_variaveis
        li_crescimentoMais_variaveis = li_12m_crescimentoMais_variaveis
    elif parametro == '1m':
        li_crescimento10Mais_variaveis = li_1m_crescimento10Mais_variaveis
        li_crescimentoMenos_variaveis = li_1m_crescimentoMenos_variaveis
        li_crescimento10Menos_variaveis = li_1m_crescimento10Menos_variaveis
        li_crescimentoMais_variaveis = li_1m_crescimentoMais_variaveis
    
    
    #print(agregação) # cnae_grupo_cod
    
    import re
    arq_nome = re.sub(r'_cod', "_desc.csv", agregação)
    #print(arq_nome)
    
    pasta = caminho_base / 'Dados' / 'cnae e ncm'
    
    #arq_nome = 'cnae2_grupo_desc.csv'
    
    df_desc = pd.read_csv(pasta / arq_nome,
                     delimiter = ';',
                     decimal=',',
                     dtype='str')
    
    desc_agregação = re.sub(r'_cod', "_desc", agregação)
    #print(desc_agregação)
    
    
    df_desc.set_index(agregação,inplace=True)
    
    dicionário2 = {}
    
    for vl_variavel in li_variaveis:
        
        #vl_variavel = 'Acumulado em 12 meses - Valor'
        #vl_variavel = 'Mensal - Valor'
        
        # Copia o df
        df_cp = dicionário1[vl_variavel].copy()
        # Deleta coluna das exportações ou importações
        df_cp.drop(['total'],axis=1,inplace=True)
        # Cria coluna do mês por extenso
        df_cp['dt_ano_mes'] = df_cp.index.year.astype('str') + '_' + df_cp.index.month.astype('str')
        # Ordena o index por ordem decrescente
        df_cp.sort_index(ascending=False, inplace=True)
        # Coloca o mês string no índice
        df_cp.set_index('dt_ano_mes',inplace=True)
        # Transpõe o df
        df_longo = df_cp.T
        # Ordena pela coluna do último mês
        df_longo.sort_values(by=[ultimo],ascending=[False],inplace=True)
        
        # Seleciona os setores MAIS e MENOS importantes
            # Maiores crescimentos
        df_crescimento10Mais = df_longo.copy().loc[li_crescimento10Mais_variaveis,:]
        df_crescimentoMenos = df_longo.copy().loc[li_crescimentoMenos_variaveis,:]
            # Menores crescimentos
        df_crescimento10Menos = df_longo.copy().loc[li_crescimento10Menos_variaveis,:]
        df_crescimentoMais = df_longo.copy().loc[li_crescimentoMais_variaveis,:]
        
        # Ordena o df curto pelos mais importantes
        df_crescimento10Mais.sort_values(by=[ultimo],ascending=[False],inplace=True)
        df_crescimento10Menos.sort_values(by=[ultimo],ascending=[True],inplace=True)
        
        # Soma (ao longo das linhas), para cada mês (nas colunas), o valor dos setores menos importantes
        df_crescimentoMenos_soma = df_crescimentoMenos.sum(axis=0).to_frame().T
        df_crescimentoMais_soma = df_crescimentoMais.sum(axis=0).to_frame().T
        
        # Renomeia a linha da soma para 'Outros'
        df_crescimentoMenos_soma.rename(mapper={0:'Outros'},axis=0,inplace=True)
        df_crescimentoMais_soma.rename(mapper={0:'Outros'},axis=0,inplace=True)
            
        # Junta a soma dos valores menos importantes aos setores mais importantes
        df_crescimento10Mais = df_crescimento10Mais.append(df_crescimentoMenos_soma)
        df_crescimento10Menos = df_crescimento10Menos.append(df_crescimentoMais_soma)
        
        # Cria linha com total geral
        df_crescimento10Mais.loc['Total Geral',:] = df_crescimento10Mais.sum(axis=0)
        df_crescimento10Menos.loc['Total Geral',:] = df_crescimento10Menos.sum(axis=0)
        
        # Coloca nomes descrição
        df_crescimento10Mais = df_crescimento10Mais.merge(df_desc,how='left',left_index=True,right_index=True)
        df_crescimento10Mais.loc['Outros',desc_agregação] = 'Outros'
        df_crescimento10Mais.loc['Total Geral',desc_agregação] = 'Total Geral'
        # ------------
        df_crescimento10Menos = df_crescimento10Menos.merge(df_desc,how='left',left_index=True,right_index=True)
        df_crescimento10Menos.loc['Outros',desc_agregação] = 'Outros'
        df_crescimento10Menos.loc['Total Geral',desc_agregação] = 'Total Geral'
        
        # Coloca na primeira coluna
        df_meses = df_crescimento10Mais.filter(regex='^2',axis=1)
        df_crescimento10Mais = df_crescimento10Mais[desc_agregação].to_frame()
        df_crescimento10Mais = df_crescimento10Mais.merge(df_meses,how='left',left_index=True,right_index=True)
        # ------------
        df_meses = df_crescimento10Menos.filter(regex='^2',axis=1)
        df_crescimento10Menos = df_crescimento10Menos[desc_agregação].to_frame()
        df_crescimento10Menos = df_crescimento10Menos.merge(df_meses,how='left',left_index=True,right_index=True)
        
        # Define novos nomes
        nome_longo_maioresCrescimentos = vl_variavel + ' - Maiores crescimentos (longo)'
        nome_curto_maioresCrescimentos = vl_variavel + ' - Maiores crescimentos (curto)'
        nome_curto_menoresCrescimentos = vl_variavel + ' - Menores crescimentos (curto)'
        
        # Adiciona a dicionário2
        dicionário2[nome_longo_maioresCrescimentos] = df_longo.copy()
        dicionário2[nome_curto_maioresCrescimentos] = df_crescimento10Mais.copy()
        dicionário2[nome_curto_menoresCrescimentos] = df_crescimento10Menos.copy()
        #####################################################################################
    return dicionário1, dicionário2
    ####################################################################################################




#dic1_MS, dic2_MS = cgd_01b(uf='MS', início='2018-01', final='2020-10', agregação='cnae_grupo_cod')

dic1_BR, dic2_BR = cgd_01b(uf='BR', início='2018-01', final='2020-10', agregação='cnae_grupo_cod')













