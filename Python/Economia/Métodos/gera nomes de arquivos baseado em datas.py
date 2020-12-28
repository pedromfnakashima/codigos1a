# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:52:28 2020

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
caminho_wd = caminho_base / 'Dados'
os.chdir(caminho_wd)

#import numpy as np


#################################################################
#################################################################
#################################################################

def g_li_datas(início, final, extensão=False):
    
    import pandas as pd
    import re
    from datetime import datetime
    
    # início = '200605'
    # final = '201203'    
    
    # início = '2006b1'
    # final = '2012b4'
    
    # início = '2006q1'
    # final = '2012q2'
    
    matched = re.match('\d{4}\-?\d{2}', início, re.IGNORECASE)
    eh_mensal = bool(matched)
    
    matched = re.match('\d{4}b\d', início, re.IGNORECASE)
    eh_bimestral = bool(matched)
    
    matched = re.match('\d{4}q\d', início, re.IGNORECASE)
    eh_quadrimestral = bool(matched)
    
    início_ano = int(início[0:4])
    final_ano = int(final[0:4])
    
    if eh_mensal == False:
        início_per = int(início[-1])
        final_per = int(final[-1])
    else:
        início_mês = int(início[-2:])
        final_mês = int(final[-2:])
        freq = 'MS'
    
    dicBimMês = {1:2,2:4,3:6,4:8,5:10,6:12}
    dicQuadMês = {1:4,2:8,3:12}
    
    dicMêsBim = {'2':'1','4':'2','6':'3','8':'4','10':'5','12':'6'}
    dicMêsQuad = {'4':'1','8':'2','12':'3'}
    
    if eh_bimestral == True:
        freq = '2MS'
        sigla = 'b'
        início_mês = dicBimMês[início_per]
        final_mês = dicBimMês[final_per]
    elif eh_quadrimestral == True:
        freq = '4MS'
        sigla = 'q'
        início_mês = dicQuadMês[início_per]
        final_mês = dicQuadMês[final_per]
    
    data1 = datetime(início_ano, início_mês, 1)
    data2 = datetime(final_ano, final_mês, 1)
    
    pdData = pd.date_range(start=data1, end=data2, freq=freq).to_frame()
    
    pdData.rename(mapper={0:'dt'},axis=1,inplace=True)
    
    pdData['dt_mês'] = pdData['dt'].dt.month.astype(str)
    pdData['dt_ano'] = pdData['dt'].dt.year.astype(str)
    
    def retornaPeríodo(int1):
        if eh_bimestral == True:
            período = dicMêsBim[int1]
        elif eh_quadrimestral == True:
            período = dicMêsQuad[int1]
        return período
    
    if eh_mensal == False:
        li_períodos = [retornaPeríodo(int1) for int1 in pdData['dt_mês']]
        pdData['dt_per'] = li_períodos
        pdData['período'] = pdData['dt_ano'] + sigla + pdData['dt_per']
    else:
        pdData['dt_mês'] = pdData['dt_mês'].apply(lambda x: x.zfill(2))
        pdData['período'] = pdData['dt_ano'] + pdData['dt_mês']
    
    if extensão != False:
        pdData['período'] = pdData['período'] + extensão
    
    return pdData['período']

# li_períodos = g_li_datas('2006b1', '2006b1')

# li_períodos = g_li_datas('2006b1', '2012b4')

# li_períodos = g_li_datas('200605', '201203')

# li_períodos = g_li_datas('2006b1', '2012b4', extensão='.zip')

# li_períodos = g_li_datas('200605', '201203', extensão='.csv')

# li_períodos = g_li_datas('2006q1', '2012q2', extensão='.zip')

# li_períodos = g_li_datas('2006q1', '2006q1')

# li_períodos = li_períodos + prefixo








#################################################################
#################################################################
#################################################################

import re
from datetime import datetime

# início = '2006b1'
# final = '2012b4'

início = '2006q1'
final = '2012q2'

matched = re.match('\d{4}b\d', início, re.IGNORECASE)
eh_bimestral = bool(matched)

matched = re.match('\d{4}q\d', início, re.IGNORECASE)
eh_quadrimestral = bool(matched)

início_ano = int(início[0:4])
final_ano = int(final[0:4])
início_per = int(início[-1])
final_per = int(final[-1])

dicBimMês = {1:2,2:4,3:6,4:8,5:10,6:12}
dicQuadMês = {1:4,2:8,3:12}

dicMêsBim = {'2':'1','4':'2','6':'3','8':'4','10':'5','12':'6'}
dicMêsQuad = {'4':'1','8':'2','12':'3'}

if eh_bimestral == True:
    freq = '2MS'
    sigla = 'b'
    início_mês = dicBimMês[início_per]
    final_mês = dicBimMês[final_per]
elif eh_quadrimestral == True:
    freq = '4MS'
    sigla = 'q'
    início_mês = dicQuadMês[início_per]
    final_mês = dicQuadMês[final_per]

data1 = datetime(início_ano, início_mês, 1)
data2 = datetime(final_ano, final_mês, 1)

pdData = pd.date_range(start=data1, end=data2, freq=freq).to_frame()

pdData.rename(mapper={0:'dt'},axis=1,inplace=True)

pdData['dt_mês'] = pdData['dt'].dt.month.astype(str)
pdData['dt_ano'] = pdData['dt'].dt.year.astype(str)

def retornaPeríodo(int1):
    if eh_bimestral == True:
        período = dicMêsBim[int1]
    elif eh_quadrimestral == True:
        período = dicMêsQuad[int1]
    return período

li_períodos = [retornaPeríodo(int1) for int1 in pdData['dt_mês']]

pdData['dt_per'] = li_períodos

pdData.drop(['dt_mês'],axis=1,inplace=True)

pdData['período'] = pdData['dt_ano'] + sigla + pdData['dt_per']

pdData.drop(['dt_ano','dt_per','dt'],axis=1,inplace=True)



























