# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:58:38 2020

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
import numpy as np
import pandas as pd
df = pd.read_csv('airline_passengers.csv', index_col='Month', parse_dates=True)

""" O passo abaixo é fundamental
para se rodar statsmodels """
df.index.freq = 'MS'

print(df.head())
print(df.tail())

"""
Test Train Split
The size of the test set is
tipically about 20% of total sample,
although this value depends on
how long the sample is and how
far ahead you want to forecast.
The test set should ideally be
at least as large as the maximum
forecast horizon required.
Lembrar que:
O final é não inclusivo e o
início é inclusivo.
"""
train_data = df.iloc[:109] #.loc[:'1940-01-01']
test_data = df.iloc[108:]

from statsmodels.tsa.holtwinters import ExponentialSmoothing

"""
Holt Winters
(Triple Smoothing)
"""
fitted_model = ExponentialSmoothing(train_data['Thousands of Passengers'],
                        seasonal_periods=12).fit()

"""
Cada linha é 1 mês. Assim:
1 ano = 12 períodos
3 anos = 36 períodos
"""
test_predictions = fitted_model.forecast(36) # Previsão para 3 anos

print(test_predictions)

# --------------------- Gráfico com todos os dados
train_data['Thousands of Passengers'].plot(legend=True, label='TRAIN', figsize=(12,8))
test_data['Thousands of Passengers'].plot(legend=True, label='TEST', figsize=(12,8))
test_predictions.plot(legend=True, label='PREDICTION')

# --------------------- Delimita gráfico (apenas com o período que tem previsão)
train_data['Thousands of Passengers'].plot(legend=True, label='TRAIN', figsize=(12,8))
test_data['Thousands of Passengers'].plot(legend=True, label='TEST', figsize=(12,8))
test_predictions.plot(legend=True, label='PREDICTION', xlim=['1958-01-01', '1961-01-01'])

###################################
# EVALUATING FORECAST PREDICTIONS #
###################################

"""
Mean Absolute Error
Mean Squared Error
Root Mean Square Error
"""

print(test_data.describe())

from sklearn.metrics import mean_squared_error, mean_absolute_error

print(mean_absolute_error(test_data, test_predictions))

print(mean_squared_error(test_data, test_predictions))

print(np.sqrt(mean_squared_error(test_data, test_predictions)))


"""
Modelo final para previsões
fora da amostra
"""
final_model = ExponentialSmoothing(df['Thousands of Passengers'], trend='mul', seasonal='mul', seasonal_periods=12).fit()

forecast_predictions = final_model.forecast(36)

# Gráfico com dados originais:
df['Thousands of Passengers'].plot(figsize=(12,8))
# Gráfico com dados originais + Previsões:
df['Thousands of Passengers'].plot(figsize=(12,8))
forecast_predictions.plot()

####################################
# ESTACIONARIEDADE E DIFERENCIAÇÃO #
####################################

"""
Estacionariedade: sem tendência
ou sazonalidade.
Flutuações devido apenas a
forças externas e ruídos.
"""

df2 = pd.read_csv('samples.csv', index_col=0, parse_dates=True)

print(df2.head())

"""
Dados estacionários:
"""
df2['a'].plot()

"""
Dados não estacionários:
"""
df2['b'].plot()

"""
Diferenciação de primeira ordem
MANUALMENTE
"""
from statsmodels.tsa.statespace.tools import diff

print(df2['b'])

print(df2['b'] - df2['b'].shift(1))

"""
Diferenciação de primeira ordem
COM STATSMODELS
De primeira ordem: k_diff=1
"""
print(diff(df2['b'], k_diff=1))

"""
Abaixo:
Após a primeira diferenciação,
a série parece ficar estacionária.
Não tem mais tendência.
"""
diff(df2['b'], k_diff=1).plot()

#############################
####### ACF e PACF ##########
#############################
import numpy as np
import pandas as pd

import statsmodels.api as sm
from statsmodels.tsa.stattools import acovf, acf, pacf, pacf_yw, pacf_ols

"""
NÃO ESTACIONÁRIO
"""
df1 = pd.read_csv('airline_passengers.csv', index_col='Month', parse_dates=True)
df1.index.freq = 'MS'

"""
ESTACIONÁRIO
"""
df2 = pd.read_csv('DailyTotalFemaleBirths.csv', index_col='Date', parse_dates=True)
df2.index.freq = 'D'

print(df1.head())
print(df2.head())

"""
"""

import warnings
warnings.filterwarnings('ignore')

"""
"""
df = pd.DataFrame({'a':[13,5,11,12,9]})
print(df)

print(acf(df['a']))

print(pacf_yw(df['a'], nlags=4, method='mle'))

print(pacf_yw(df['a'], nlags=4, method='unbiased')) # padrão

print(pacf_ols(df['a'], nlags=4))

"""
"""
from pandas.plotting import lag_plot

lag_plot(df1['Thousands of Passengers'])
"""
Acima,
Fortes indícios de autocorrelação
Abaixo, dados estacionários
"""
lag_plot(df2['Births'])

"""
"""
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

df1.plot()
# ACF - não estacionário:
plot_acf(df1, lags=40)

df2.plot()
# ACF - estacionário:
plot_acf(df2, lags=40)

"""
"""
plot_pacf(df2, lags=40, title='Daily Female Births')

############################
######### ARIMA ############
############################

############################
######### 56 AR ############
############################

import numpy as np
import pandas as pd

from statsmodels.tsa.ar_model import AR, ARResults

df = pd.read_csv('uspopulation.csv', index_col='DATE', parse_dates=True)
df.index.freq = 'MS'

print(df.head())
df.plot(figsize=(12,8))

"""
"""
print(len(df))
print(96-12)

train = df.iloc[:84]
test = df.iloc[84:]

import warnings
warnings.filterwarnings('ignore')

"""
"""
model = AR(train['PopEst'])

AR1fit = model.fit(maxlag=1)

print(AR1fit.aic)

print(AR1fit.k_ar)

print(AR1fit.params)

"""
"""
start = len(train)
end = len(train) + len(test) - 1
print(start)
print(end)

"""
"""
predictions1 = AR1fit.predict(start=start, end=end)
print(predictions1)
predictions1 = predictions1.rename('AR(1) Predictions')
print(predictions1)

test.plot(figsize=(12,8), legend=True)
predictions1.plot(legend=True)

"""
"""
model = AR(train['PopEst'])
AR2fit = model.fit(maxlag=2)
print(AR2fit.params)

predictions2 = AR2fit.predict(start, end)
predictions2 = predictions2.rename('AR(2) Predictions')

"""
"""
test.plot(figsize=(12,8), legend=True)
predictions1.plot(legend=True)
predictions2.plot(legend=True)

"""
Auto
"""
model = AR(train['PopEst'])
ARfit = model.fit(ic='t-stat')
print(ARfit.params)
predictions8 = ARfit.predict(start, end)
predictions8 = predictions8.rename('AR(8) Predictions')
"""
"""
from sklearn.metrics import mean_squared_error
labels = ['AR1', 'AR2', 'AR8']

preds = [predictions1, predictions2, predictions8]

for i in range(3):
    # np.sqrt()
    error = mean_squared_error(test['PopEst'], preds[i])
    print(f'{labels[i]} MSE was: {error}')

"""
"""
test.plot(figsize=(12,8), legend=True)
predictions1.plot(legend=True)
predictions2.plot(legend=True)
predictions8.plot(legend=True)

"""
Previsões p/ o futuro
FORECASTING FUTURE
(com todos os dados)
sem maxlag, deixamos no auto
"""
model = AR(df['PopEst'])
ARfit = model.fit()
forecasted_values = ARfit.predict(start=len(df), end=len(df)+12).rename('Forecast') # Previsão para 12 meses
"""
"""
df['PopEst'].plot(figsize=(12,8), legend=True)
forecasted_values.plot(legend=True)

############################
## DESCRIPTIVE STATISTICS ##
## AND TESTS ###############
############################

import numpy as np
import pandas as pd

# Ignore harmless warnings
import warnings
warnings.filterwarnings('ignore')

# Load a seasonal dataset
df1 = pd.read_csv('airline_passengers.csv', index_col='Month', parse_dates=True)
df1.index.freq = 'MS'

# Load a nonseasonal dataset
df2 = pd.read_csv('DailyTotalFemaleBirths.csv', index_col='Date', parse_dates=True)
df2.index.freq = 'D'

"""
"""
df1.plot()

"""
"""
from statsmodels.tsa.stattools import adfuller

print(adfuller(df1['Thousands of Passengers']))

dftest = adfuller(df1['Thousands of Passengers'])

dfout = pd.Series(dftest[0:4], index=['ADF Test Statistic', 'p-value', '# Lags Used', '# Observations'])

for key, val in dftest[4].items():
    dfout[f'critical value ({key})'] = val

print(dfout)

"""
Function for running the augmented Dickey-Fuller test¶
Since we'll use it frequently in the upcoming forecasts, let's define a function we can copy into future notebooks for running the augmented Dickey-Fuller test. Remember that we'll still have to import adfuller at the top of our notebook.
"""
from statsmodels.tsa.stattools import adfuller

def adf_test(series,title=''):
    """
    Pass in a time series and an optional title, returns an ADF report
    """
    print(f'Augmented Dickey-Fuller Test: {title}')
    result = adfuller(series.dropna(),autolag='AIC') # .dropna() handles differenced data
    
    labels = ['ADF test statistic','p-value','# lags used','# observations']
    out = pd.Series(result[0:4],index=labels)

    for key,val in result[4].items():
        out[f'critical value ({key})']=val
        
    print(out.to_string())          # .to_string() removes the line "dtype: float64"
    
    if result[1] <= 0.05:
        print("Strong evidence against the null hypothesis")
        print("Reject the null hypothesis")
        print("Data has no unit root and is stationary")
    else:
        print("Weak evidence against the null hypothesis")
        print("Fail to reject the null hypothesis")
        print("Data has a unit root and is non-stationary")

adf_test(df1['Thousands of Passengers'])
df1.plot()
adf_test(df2['Births'])

"""
TESTE DE CAUSALIDADE DE GRANGER
"""
df3 = pd.read_csv('samples.csv', index_col=0, parse_dates=True)
df3.index.freq = 'MS'

print(df3)

df3[['a', 'd']].plot(figsize=(12,8))

df3['a'].iloc[2:].plot(figsize=(12,8), legend=True)
df3['d'].shift(2).plot(figsize=(12,8), legend=True)

"""
o gráfico acima mostra que há
fortes evidências que d causa a.
Fazendo abaixo o teste de
causalidade de Granger.
"""
from statsmodels.tsa.stattools import grangercausalitytests

print(grangercausalitytests(df3[['a', 'd']], maxlag=3));

print(grangercausalitytests(df3[['b', 'd']], maxlag=3));

"""
"""
np.random.seed(42)
df = pd.DataFrame(np.random.randint(20,30,(50,2)), columns=['test', 'predictions'])
print(df.head())
df.plot(figsize=(12,8))

"""
"""
from statsmodels.tools.eval_measures import mse, rmse, meanabs

print(rmse(df['test'], df['predictions']))

"""
Procurando a sazonalidade
Indica, abaixo, que há aumento
em julho e dezembro
"""
df = pd.read_csv('airline_passengers.csv', index_col='Month', parse_dates=True)
df.index.freq = 'MS'
df.plot()

from statsmodels.graphics.tsaplots import month_plot, quarter_plot

month_plot(df['Thousands of Passengers']);

"""
Transformando para trimestral
Aumento no terceiro trimestre
"""
dfq = df['Thousands of Passengers'].resample(rule='Q').mean()

quarter_plot(dfq)

# -------------------------
# 61 ARIMA Theory Preview
# -------------------------

"""
"""


"""
"""


"""
"""


"""
"""


