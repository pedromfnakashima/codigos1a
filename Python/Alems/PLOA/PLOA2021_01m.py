# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 20:31:40 2020

@author: pedro
"""

########################### IPCA #########################################
def g_deflator(base = 'último'):
    pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
    df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
    df_ipca.index.freq = 'MS'
    
    if base == 'último':
        base_escolhida = df_ipca.loc[df_ipca.index.max(), 'Índice']
    else:
        base = '2020-08-01'
        cond = df_ipca.index == base
        filtro = df_ipca.loc[cond, :]
        filtro.reset_index(inplace=True)
        base_escolhida = filtro.loc[0,'Índice']
    
    df_ipca['deflator'] = base_escolhida / df_ipca['Índice']
    df_ipca = df_ipca['deflator']
    return df_ipca

df_ipca = g_deflator()
df_ipca = g_deflator(base='2020-08-01')

##########################################################################

def deflaciona_dic(dic, base = 'último'):
    
    df_ipca = g_deflator(base=base)
    
    dic_series_mensais = dic.copy()
    
    for key in dic_series_mensais.keys():
        print(key)

        
        dic_series_mensais[key] = dic_series_mensais[key].mul(df_ipca, axis=0)
        
        dic_series_mensais[key].dropna(axis=0, thresh=1, inplace=True)
        
    return dic_series_mensais


dic_series_mensais = g_series_mensais() # arquivo PLOA2021_01l.py

#dicionario_deflacionado = deflaciona_dic(dic=dic_series_mensais, base='2020-08-01')

dicionario_deflacionado = deflaciona_dic(dic=dic_series_mensais)


def g_var_percent():

    import pandas as pd
    
    colunas = ['recCorr', 'itcm', 'icms', 'ipva', 'itcd', 'irrf', 'contrib', 'transfCorr', 'fpe', 'transfFundeb']
    ufs = ['MS', 'MT', 'AM', 'RO', 'BA', 'SP', 'SC', 'GO', 'ES', 'PA', 'TO', 'PR', 'PE', 'AP',
     'SE', 'PB', 'MA', 'CE', 'RJ', 'PI', 'AC', 'RS', 'RR', 'MG', 'RN', 'AL', 'DF']
    
    dicionario = {}
    
    #uf = 'MS'
    #coluna = 'recCorr'
    
    for coluna in colunas:
        
        df_varPercent = pd.DataFrame(columns=['UF','var_percent'])
        
        for index, uf in enumerate(ufs):
            
            
            
            df_uf = dicionario_deflacionado[uf][coluna].copy().to_frame()
            df_uf['ano'] = df_uf.index.year
            df_uf['mês'] = df_uf.index.month
            cond1a = df_uf['ano'] == 2019
            cond1b = df_uf['ano'] == 2020
            cond2 = df_uf['mês'] <= 8
            cond = (cond1a | cond1b) & cond2
            filtro = df_uf.loc[cond,:]
            somas = filtro.groupby(['ano'])[coluna].sum()
            soma_2019 = somas.loc[2019]
            soma_2020 = somas.loc[2020]
            var_percent = ((soma_2020 - soma_2019)/soma_2019) * 100
            df_varPercent.loc[index,'UF'] = uf
            df_varPercent.loc[index,'var_percent'] = var_percent
            df_varPercent.sort_values(by=['var_percent'], ascending=[True], inplace=True)
            df_varPercent.index = range(len(df_varPercent))
            
        dicionario[coluna] = df_varPercent
    
    return dicionario

dic_varPercents = g_var_percent()


pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    dic_varPercents['contrib'].to_excel(writer, sheet_name='vp_contrib', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    dic_varPercents['fpe'].to_excel(writer, sheet_name='vp_fpe', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    dic_varPercents['icms'].to_excel(writer, sheet_name='vp_icms', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    dic_varPercents['ipva'].to_excel(writer, sheet_name='vp_ipva', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    dic_varPercents['irrf'].to_excel(writer, sheet_name='vp_irrf', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    dic_varPercents['itcd'].to_excel(writer, sheet_name='vp_itcd', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    dic_varPercents['itcm'].to_excel(writer, sheet_name='vp_itcm', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    dic_varPercents['recCorr'].to_excel(writer, sheet_name='vp_recCorr', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    dic_varPercents['transfCorr'].to_excel(writer, sheet_name='vp_transfCorr', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    dic_varPercents['transfFundeb'].to_excel(writer, sheet_name='vp_transfFundeb', index=False)


























