# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 17:39:25 2020

@author: pedro
"""

# https://www.youtube.com/watch?v=k8asfUbWbI4&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=48

########################################################

"""
Meses para pagar uma dívida.
"""

globals().clear()

import datetime
import calendar

dívida = 10000
interest_rate = 13 * .01
monthly_payment = 1000

today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
days_till_end_month = days_in_current_month - today.day

start_date = today + datetime.timedelta(days=days_till_end_month + 1)
end_date = start_date

while dívida > 0:
    interest_charge = (interest_rate / 12) * dívida
    dívida += interest_charge
    dívida -= monthly_payment

    dívida = round(dívida, 2)
    if dívida < 0:
        dívida = 0
        
    print(end_date, dívida)

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_in_current_month)

########################################################

"""
Meses para chegar num peso.
obs.: o peso está em pounds (libras).
"""

globals().clear()

import datetime

current_weight = 220
goal_weight = 180
avg_lbs_week = 2

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_lbs_week

print(end_date)
print(f'Reached goal in {(end_date - start_date).days // 7} weeks')

########################################################

"""
Dia que vai atingir um certo número de seguidores na
rede social.
"""


import datetime
import math

goal_subs = 150000
current_subs = 85000
subs_to_go = goal_subs - current_subs

avg_subs_day = 200
days_to_go = math.ceil(subs_to_go / avg_subs_day)

today = datetime.date.today()

print(today + datetime.timedelta(days=days_to_go))























