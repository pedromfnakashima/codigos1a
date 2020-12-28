# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:13:07 2020

@author: pedro
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

'''
competência;
mun_cod_ibge;
cbo_ocupação_cod;
cnae_subclasse_cod;
horascontratuais;
graudeinstrução;
idade;salário;
saldomovimentação
'''

def transf_arqs(início, final, salva=False):
    
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
    
    #início = '2019-12'
    #final = '2019-12'
    #início = '2020-01'
    #final = '2020-01'
    li_arquivos_txt = g_nome_arq(início=início, final=final, prefixo='CAGEDMOV', sufixo='.txt')
    li_arquivos_csv = g_nome_arq(início=início, final=final, prefixo='CAGEDMOV', sufixo='.csv')
    
    pasta_origem = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv'
    pasta_destino = pasta_origem.parent / 'csv_processados'
    
    for arq_nome_txt, arq_nome_csv in zip(li_arquivos_txt, li_arquivos_csv):
        print(f'Lendo {arq_nome_txt}')
        na_values = ['{ñ', '{ñ c','00000-1', '0000-1', '000-1', '{с class}']
        
        try:  
            # A partir de janeiro de 2020
            dtype = {'competência':'str','município':'str','subclasse':'str','horascontratuais':'float64','saldomovimentação':pd.Int64Dtype(),'cbo2002ocupação':'str','graudeinstrução':pd.Int64Dtype(),'idade':pd.Int64Dtype(),'salário':'float64'}
            df = pd.read_csv(pasta_origem / arq_nome_txt, header=0, sep=';', decimal='.', quotechar='"', skiprows=0, dtype=dtype, na_values=na_values)
            mapper = {'município':'mun_cod_ibge','cbo2002ocupação':'cbo_ocupação_cod','subclasse':'cnae_subclasse_cod','seção':'cnae_seção_cod'}
            colunas = ['competência','mun_cod_ibge','cbo_ocupação_cod','cnae_subclasse_cod','cnae_seção_cod','horascontratuais','graudeinstrução','idade','salário','saldomovimentação']

        except UnicodeDecodeError:  
            # Até dezembro de 2019
            dtype = {'Competência Declarada':'str','Município':'str','CNAE 2.0 Subclas':'str','Qtd Hora Contrat':'float64','Saldo Mov':pd.Int64Dtype(),'CBO 2002 Ocupação':'str','Grau Instrução':pd.Int64Dtype(),'Idade':pd.Int64Dtype(),'CNAE 2.0 Classe':'str'}
            df = pd.read_csv(pasta_origem / arq_nome_txt, encoding = 'latin', header=0, sep=';', decimal='.', quotechar='"', skiprows=0, dtype=dtype, na_values=na_values)
            df['Salário Mensal'] = df['Salário Mensal'].str.replace(',','.').astype(np.float64)
            mapper = {'Competência Declarada':'competência','Município':'mun_cod_ibge','CNAE 2.0 Subclas':'cnae_subclasse_cod','Qtd Hora Contrat':'horascontratuais','Saldo Mov':'saldomovimentação','CBO 2002 Ocupação':'cbo_ocupação_cod','Grau Instrução':'graudeinstrução','Idade':'idade','Salário Mensal':'salário','CNAE 2.0 Classe':'cnae_classe_cod'}
            colunas = ['competência','mun_cod_ibge','cbo_ocupação_cod','cnae_subclasse_cod','cnae_classe_cod','horascontratuais','graudeinstrução','idade','salário','saldomovimentação']
        else:  
            # Sem exceções
            pass
        finally:
            # sempre fazer isso
            pass
            #print(df.dtypes)
        
        df.rename(mapper=mapper,axis=1,inplace=True)
        df = df.loc[:, colunas]
        #print(df.dtypes)
        
        # Coloca um 0 na frente da coluna cnae_subclasse_cod quando ela tiver 6 dígitos
        df['len'] = df['cnae_subclasse_cod'].str.len()
        cond1 = df['len'] == 6
        df.loc[cond1, 'cnae_subclasse_cod'] = '0' + df['cnae_subclasse_cod']
        df.drop(['len'],axis=1,inplace=True)
        # Muda códigos que não existem
        cond1 = df['cnae_subclasse_cod'] == '8630505'
        df.loc[cond1, 'cnae_subclasse_cod'] = '8630504'
        # Salva se verdadeiro
        if salva == True:
            df.to_csv(pasta_destino / arq_nome_csv, sep=';', decimal=',', index=False)
            print(f'Salvo {arq_nome_csv}')
        
    return df
    print('Tarefa completada')


df = transf_arqs(início='2020-01', final='2020-10', salva=True)

del df







df = pd.read_csv(pasta_origem / arq_nome_txt, header=0, sep=';', decimal='.', quotechar='"', skiprows=0, dtype=dtype, na_values=na_values)






df['len'] = df['cnae_subclasse_cod'].str.len()
#print(df['len'].value_counts())
cond1 = df['len'] == 6
filtro = df.loc[cond1,:]
print(f'Linhas com subclasses de 6 dígitos: {cond1.sum()}')

df.loc[cond1, 'cnae_subclasse_cod'] = '0' + df['cnae_subclasse_cod']

df['len'] = df['cnae_subclasse_cod'].str.len()
cond1 = df['len'] == 6
filtro = df.loc[cond1,:]
print(f'Linhas com subclasses de 6 dígitos: {cond1.sum()}')

df.drop(['len'],axis=1,inplace=True)


##########################################################################################
##########################################################################################
##########################################################################################

def valida_caged(início, final):
    
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
    #início = '2020-01'
    #final = '2020-01'
    #li_arquivos_txt = g_nome_arq(início=início, final=final, prefixo='CAGEDMOV', sufixo='.txt')
    li_arquivos_csv = g_nome_arq(início=início, final=final, prefixo='CAGEDMOV', sufixo='.csv')
    
    pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
    
    index_arq = -1
    for arq_nome_csv in li_arquivos_csv:
        index_arq += 1
        print(f'Lendo {arq_nome_csv}')
        
        dtype = {'cnae_subclasse_cod':'str','cnae_classe_cod':'str', 'competência':'str'}
        df = pd.read_csv(pasta / arq_nome_csv,
                         delimiter = ';',
                         decimal=',',
                         dtype=dtype)
        
        if index_arq == 0:
            df_todos = df.copy()
        else:
            df_todos = df_todos.append(df)
    print('Tarefa completada')
    return df_todos


df_todos = valida_caged(início='2020-10', final='2020-10')

print(df_todos['saldomovimentação'].sum()) # 394989

pasta = caminho_base / 'Dados' / 'cnae e ncm'
arq_nome = 'cnae_corresp.csv'
df_cnae_corresp = pd.read_csv(pasta / arq_nome,
                              delimiter = ';',
                              decimal=',',
                              dtype='str')

df_todos = df_todos.merge(df_cnae_corresp,how='left',left_on='cnae_subclasse_cod',right_on='cnae_subclasse_cod')

print(df_todos['saldomovimentação'].sum())

cond1 = df_todos['cnae_grupo_cod'] == '782'
filtro = df_todos.loc[cond1,:]
print(filtro['saldomovimentação'].sum())





print(df_todos.dtypes)











