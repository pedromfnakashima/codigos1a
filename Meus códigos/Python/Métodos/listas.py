# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 21:25:35 2020

@author: pedro
"""

# Gera lista, e manipula cada elemento, por looping de uma linha
li_datas_str = [str(dt.year) + str(dt.month).zfill(2) for dt in li_datas_pdDateTime]


