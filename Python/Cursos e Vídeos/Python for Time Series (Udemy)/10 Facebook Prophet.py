# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:41:18 2020

@author: pedro
Instalar o pystan pelo conda antes
do fpprophet
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
caminho_wd = caminho_base / 'Dados' / 'Cursos e Livros' / 'Python for time series (Udemy)' / 'Data'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

"""
"""
import pandas as pd
from fbprophet import Prophet

df = pd.read_csv('BeerWineLiquor.csv')

print(df.head())
print(df.info())

"""
É necessário que a coluna de
data seja ds e a outra y.
Dados diários.
"""
df.columns = ['ds', 'y']

df['ds'] = pd.to_datetime(df['ds'])

m = Prophet()

m.fit(df)

# PLACEHOLDER TO HOLD OUR FUTURE PREDICTIONS

#df.index.freq = ""
future = m.make_future_dataframe(periods=24, freq='MS')

print(future)
print(future.tail())
print(df.tail())

print(len(df))
print(len(future))

forecast = m.predict(future)

print(forecast)

print(forecast.columns)

print(forecast[['ds', 'yhat_lower', 'yhat_upper', 'yhat']].tail(12))

import matplotlib.pyplot as plt

m.plot(forecast)
plt.xlim('2014-01-01', '2021-01-01')
# não funcionou a última linha

forecast.plot(x='ds', y='yhat', figsize=(8,10))

m.plot_components(forecast)

"""
#92 Evaluation
"""

df = pd.read_csv('Miles_Traveled.csv')

print(df.info())

df.columns = ['ds', 'y']

df['ds'] = pd.to_datetime(df['ds'])

print(df.head())

df.plot(x='ds', y='y')

"""
"""
print(len(df))

train = df.iloc[:576]
test = df.iloc[576:]

m = Prophet()
m.fit(train)
future = m.make_future_dataframe(periods=12, freq='MS')
forecast = m.predict(future)

print(forecast.tail())

print(test)

ax = forecast.plot(x='ds', y='yhat', label='Predictions', legend=True, figsize=(12,8))
test.plot(x='ds', y='y', label='True Test Data', legend=True, ax=ax, xlim=('2018-01-01', '2019-01-01'))

from statsmodels.tools.eval_measures import rmse

predictions = forecast.iloc[-12:]['yhat']
print(predictions)
print(test['y'])

print(rmse(predictions, test['y']))
print(test.mean())

"""
"""
from fbprophet.diagnostics import cross_validation, performance_metrics
from fbprophet.plot import plot_cross_validation_metric

pd.Timedelta
# INITIAL
initial = 5 * 365
initial = str(initial) + ' days'
print(initial)

# PERIOD
period = 5 * 365
period = str(period) + ' days'

# HORIZON
horizon = 365
horizon = str(horizon) + ' days'

df_cv = cross_validation(m, initial=initial, period=period, horizon=horizon)

print(df_cv.head())

print(len(df_cv))

"""
"""

print(performance_metrics(df_cv))

plot_cross_validation_metric(df_cv, metric='rmse')

plot_cross_validation_metric(df_cv, metric='mape')


"""
#93 Changing Trend
"""
import pandas as pd
from fbprophet import Prophet

df = pd.read_csv('HospitalityEmployees.csv')

df.columns = ['ds', 'y']

df['ds'] = pd.to_datetime(df['ds'])

df.plot(x='ds', y='y', figsize=(12,10))

m = Prophet()

m.fit(df)

future = m.make_future_dataframe(periods=12, freq='MS')

from fbprophet.plot import add_changepoints_to_plot

fig = m.plot(forecast)
a = add_changepoints_to_plot(fig.gca(), m, forecast)

"""
#94 Changing Seasonality
"""
import pandas as pd
from fbprophet import Prophet

df = pd.read_csv('airline_passengers.csv')

print(df.head())

df.columns = ['ds', 'y']

df['ds'] = pd.to_datetime(df['ds'])

m = Prophet()
m.fit(df)
future = m.make_future_dataframe(50, freq='MS')
forecast = m.predict(future)
fig = m.plot(forecast)

fig = m.plot_components(forecast)

"""
"""
from fbprophet.plot import add_changepoints_to_plot
fig = m.plot(forecast)
a = add_changepoints_to_plot(fig.gca(), m, forecast)

"""
Mudando a sazonalidade p/
multiplicativo
"""
m = Prophet(seasonality_mode='multiplicative')
m.fit(df)
future = m.make_future_dataframe(50, freq='MS')
forecast = m.predict(future)
fig = m.plot(forecast)

"""
"""

fig = m.plot_components(forecast)

