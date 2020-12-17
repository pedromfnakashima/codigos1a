# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:23:47 2020

@author: pedro-salj
"""





# Exporta csv
df.to_csv('cnae2_corresp.csv', sep=';', decimal=',', index=False)

pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca-15'
df_ipca15 = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)

# Lidando com encoding diferente

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



pasta = caminho_base / 'Dados' / 'Fgv'
arq_nome = 'IGP-DI.csv'

try:  
    df = pd.read_csv(pasta / arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0)
except UnicodeDecodeError: # ocorre exceção
    df = pd.read_csv(pasta / arq_nome, encoding = 'latin', header=0, sep=';', decimal=',', quotechar='"', skiprows=0)
else: # Sem exceções
    pass
finally: # sempre fazer isso
    pass


# pdf

import tabula

df = tabula.read_pdf(caminho_wd / 'LOA 2020.pdf', pages=[10])



