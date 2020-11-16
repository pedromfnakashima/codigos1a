# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:36:31 2020

@author: pedro
"""

globals().clear()
""" Mudar diretório """
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

import pandas as pd


pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'DTP e Apuração do Cumprimento do Limite Legal'
df = processa_arquivos_zip(arquivo='2020q2.zip',
                                           caminho=pasta,
                                           pasta=True)

instituicoes = ['Assembleia Legislativa', 'Governo', 'Tribunal de Contas', 'Tribunal de Justiça', 'Ministério Público']

cond1 = df['UF'] == 'MS'
cond2 = df['Coluna'].str.contains('%', case=False)
cond3 = df['Conta'].str.contains('total', case=False)
cond4 = df['exercicio'] >= 2018 # a partir desse ano, o percentual da RCL é ajustado
cond5 = df['Instituição'] == 'Assembleia Legislativa'
cond = cond1 & cond2 & cond3 & cond4
filtro = df.loc[cond, :]
filtro = df.loc[cond, ['exercicio', 'periodo', 'Valor']]
filtro.rename(columns={'Valor':'Assembleia Legislativa'}, inplace=True)

df2 = filtro.copy()

cond1 = df['UF'] == 'MS'
cond2 = df['Coluna'].str.contains('%', case=False)
cond3 = df['Conta'].str.contains('total', case=False)
cond4 = df['exercicio'] >= 2018 # a partir desse ano, o percentual da RCL é ajustado
cond5 = df['Instituição'] == 'Governo'
cond = cond1 & cond2 & cond3 & cond4 & cond5
filtro = df.loc[cond, :]
filtro = df.loc[cond, ['exercicio', 'periodo', 'Valor']]
filtro.rename(columns={'Valor':'Governo'}, inplace=True)

df2 = df2.merge(filtro, how='left', left_on=['exercicio','periodo'], right_on=['exercicio','periodo'])


def gera_series_perc_rcl():
    
    pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'DTP e Apuração do Cumprimento do Limite Legal'
    df = processa_arquivos_zip(arquivo='2020q2.zip',
                                               caminho=pasta,
                                               pasta=True)
    
    instituicoes = ['Assembleia Legislativa', 'Governo', 'Tribunal de Contas', 'Tribunal de Justiça', 'Ministério Público']
    
    for index, instituicao in enumerate(instituicoes):
        print(instituicao)
        
        cond1 = df['UF'] == 'MS'
        cond2 = df['Coluna'].str.contains('%', case=False)
        cond3 = df['Conta'].str.contains('total', case=False)
        cond4 = df['exercicio'] >= 2016 # a partir desse ano, o percentual da RCL é ajustado
        cond5 = df['Instituição'] == instituicao
        cond = cond1 & cond2 & cond3 & cond4 & cond5
        filtro = df.loc[cond, ['exercicio', 'periodo', 'Valor']]
        filtro.rename(columns={'Valor':instituicao}, inplace=True)
        
        if index == 0:
            df_final = filtro.copy()
        else:
            df_final = df_final.merge(filtro, how='left', left_on=['exercicio','periodo'], right_on=['exercicio','periodo'])
    
    return df_final

series_perc_rcl = gera_series_perc_rcl()


pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    series_perc_rcl.to_excel(writer, sheet_name='perc_rcl', index=False)









series_perc_rcl.set_index(['exercicio','periodo'], inplace=True)

#series_perc_rcl.set_index(['exercicio','periodo'], inplace=True)
#series_perc_rcl['Assembleia Legislativa'].plot()

g = series_perc_rcl['Assembleia Legislativa']

ax = g.plot(marker='.') # https://www.w3schools.com/python/matplotlib_markers.asp
ax.set_xticks(range(len(g)));
ax.set_xticklabels(["%s-%02d" % item for item in g.index.tolist()], rotation=45);
ax.xaxis.grid(True)














ax.set_xticklabels(rotation=45)


ax.set_xticks(np.arange(2016,2020,1))



ax.set_xticks(np.arange(2016,2020,1))

ax.xaxis.set_major_locator(matplotlib.ticker.FixedLocator([1,3]))


ax.set_xticks(series_perc_rcl['periodo'], minor=True)
ax.set_xticks(series_perc_rcl['exercicio'], minor=False)









from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter
ax.xaxis.set_minor_locator(AutoMinorLocator())






ax.xaxis.set_major_locator(plt.MultipleLocator(series_perc_rcl['exercicio']))







ax.xaxis.set_major_locator(matplotlib.ticker.FixedLocator([220, 100]))



ax.xaxis.set_major_locator(matplotlib.ticker.FixedLocator(series_perc_rcl['exercicio'])) 




ax.xaxis.set_major_locator(series_perc_rcl['exercicio'])
#ax.xaxis.set_major_formatter(dates.DateFormatter('%d'))

ax.xaxis.set_minor_locator(series_perc_rcl['periodo'])
ax.xaxis.set_minor_formatter('\n\n') #\n representa uma nova linha


dims = (15,5)
fig, ax = plt.subplots(figsize=dims)
ax.plot(pt)

months = MonthLocator(range(1, 13), bymonthday=1, interval=1)
monthsFmt = DateFormatter("%b '%y")
ax.xaxis.set_major_locator(months) #adding this makes the month ints disapper
ax.xaxis.set_major_formatter(monthsFmt)
handles, labels = ax.get_legend_handles_labels() #legend is nowhere on the plot
ax.legend(handles, labels)







from matplotlib import dates

ax = df['Close'].plot(xlim=['2017-01-01','2017-03-01'], ylim=[50,60], figsize=(12,5))
ax.set(xlabel='')

ax.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=0))
ax.xaxis.set_major_formatter(dates.DateFormatter('%d'))

ax.xaxis.set_minor_locator(dates.MonthLocator())
ax.xaxis.set_minor_formatter(dates.DateFormatter('\n\n%b')) #\n representa uma nova linha


