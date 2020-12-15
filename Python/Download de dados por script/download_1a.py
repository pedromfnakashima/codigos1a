# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 19:13:57 2020

@author: pedro
"""

# ipeadatapy
# https://github.com/luanborelli/ipeadatapy
pip install ipeadatapy

import ipeadatapy

ipeadatapy.list_series()

igpdi = ipeadatapy.timeseries('IGP12_IGPDI12')

# sidrapy
# https://pypi.org/project/sidrapy/
# https://github.com/AlanTaranti/Sidrapy

pip install sidrapy

import sidrapy

data = sidrapy.get_table(table_code="1419", territorial_level="1", ibge_territorial_code="all", period="last 12")

data = sidrapy.get_table(table_code="1419", territorial_level="1", ibge_territorial_code="all", period="all")

data = sidrapy.get_table(table_code="7060", territorial_level="1", ibge_territorial_code="all", period="all")












