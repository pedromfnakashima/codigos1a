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
# 63 Choosing ARIMA
# -------------------------

"""
Pyramid ARIMA
# pip install pmdarima
auto-arima
"""

import pandas as pd
import numpy as np

# Load a non-stationary dataset
df1 = pd.read_csv('airline_passengers.csv', index_col='Month', parse_dates=True)
df1.index.freq = 'MS'

# Load a stationary dataset
df2 = pd.read_csv('DailyTotalFemaleBirths.csv', index_col='Date', parse_dates=True)
df2.index.freq = 'D'

# pip install pmdarima

from pmdarima import auto_arima
help(auto_arima)

# Ignore harmless warnings
import warnings
warnings.filterwarnings('ignore')

"""
Dados estacionários
"""

stepwise_fit = auto_arima(df2['Births'], start_p=0, start_q=0, max_p=6, max_q=3, seasonal=False, trace=True)

print(stepwise_fit.summary())

"""
Dados não estacionários
"""

stepwise_fit = auto_arima(df1['Thousands of Passengers'], start_p=0, start_q=0, max_p=4, max_q=4, seasonal=True, trace=True, m=12)

print(stepwise_fit.summary())

"""
"""
import pandas as pd
import numpy as np

# Ignore harmless warnings
import warnings
warnings.filterwarnings('ignore')

from statsmodels.tsa.arima_model import ARMA, ARIMA, ARMAResults, ARIMAResults

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

from pmdarima import auto_arima

df1 = pd.read_csv('DailyTotalFemaleBirths.csv', index_col='Date', parse_dates=True)
df1.index.freq = 'D'
df1 = df1[:120]

df2 = pd.read_csv('TradeInventories.csv', index_col='Date', parse_dates=True)
df2.index.freq = 'MS'

"""
"""

df1['Births'].plot(figsize=(12,5))

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


adf_test(df1['Births'])

print(auto_arima(df1['Births'], seasonal=False).summary())

"""
"""

train = df1.iloc[:90]
test = df1.iloc[90:]

model = ARMA(train['Births'], order=(2,2))

results = model.fit()

print(results.summary())


"""
"""
start = len(train)
end = len(train) + len(test) - 1

predictions = results.predict(start, end).rename('ARMA (2,2) Predictions')

print(test)
print(predictions)

test['Births'].plot(figsize=(12,8), legend=True)
predictions.plot(legend=True)

print(test.mean())
print(predictions.mean())


"""
65 ARIMA
"""

df2.plot(figsize=(12,8))

from statsmodels.tsa.seasonal import seasonal_decompose

result = seasonal_decompose(df2['Inventories'], model='add')

result.plot()

print(auto_arima(df2['Inventories'], seasonal=False).summary())

"""
https://people.duke.edu/~rnau/411arim3.htm
https://otexts.com/fpp2/arima-r.html
"""
from statsmodels.tsa.statespace.tools import diff

df2['Diff_1'] = diff(df2['Inventories'], k_diff=1)

adf_test(df2['Diff_1'])

plot_acf(df2['Inventories'], lags=40)

plot_pacf(df2['Inventories'], lags=40)

stewise_fit = auto_arima(df2['Inventories'], start_p=0, start_q=0, max_p=2, max_q=2, seasonal=False, trace=True)

print(stewise_fit.summary())

"""
"""
print(len(df2))

train = df2.iloc[:252]
test = df2.iloc[252:]

model = ARIMA(train['Inventories'], order=(1,1,1))
results = model.fit()
print(results.summary())

"""
Previsões
"""
start = len(train)
end = len(train) + len(test) - 1

predictions = results.predict(start=start, end=end, typ='levels').rename('ARIMA(1,1,1) Predictions')

print(predictions)

print(test)

# Performance das previsões
test['Inventories'].plot(legend=True, figsize=(12,8))
predictions.plot(legend=True)

from statsmodels.tools.eval_measures import rmse

error = rmse(test['Inventories'], predictions)
print(error)

print(test['Inventories'].mean())
"""
A magnitude do rmse é em milhares, enquanto
a magnitude da média é de milhões.
Ou seja, o erro é muito pequeno.
"""


"""
FORECAST INTO UNKNOWN FUTURE
"""
model = ARIMA(df2['Inventories'], order=(1,1,1))
results = model.fit()

fcast = results.predict(start=len(df2), end=len(df2)+11, typ='levels').rename('ARIMA(1,1,1) FORECAST')

df2['Inventories'].plot(legend=True, figsize=(12,8))
fcast.plot(legend=True)

"""
#66 SARIMA
"""
import pandas as pd
import numpy as np

# Ignore harmless warnings
import warnings
warnings.filterwarnings('ignore')

from statsmodels.tsa.statespace.sarimax import SARIMAX

from statsmodels.tsa.seasonal import seasonal_decompose

from pmdarima import auto_arima

df = pd.read_csv('co2_mm_mlo.csv')
print(df.head())

"""
Montar datetime a partir dos componentes
ano e mês
"""
#dict('year':df['year'], 'month':df['month'], 'day':1)
df['date'] = pd.to_datetime({'year':df['year'], 'month':df['month'], 'day':1})
print(df.head())
print(df.info())
df = df.set_index('date')
print(df.head())
df.index.freq = 'MS'

df['interpolated'].plot(figsize=(12,8))

result = seasonal_decompose(df['interpolated'], model='add')
result.plot()
result.seasonal.plot(figsize=(12,8))

"""
autoarima sarima
"""
auto_arima(df['interpolated'], seasonal=True, m=12)

print(auto_arima(df['interpolated'], seasonal=True, m=12).summary())


"""
"""
print(len(df))

train = df.iloc[:717]
test = df.iloc[717:]

model = SARIMAX(train['interpolated'], order=(2, 1, 1), seasonal_order=(1, 0, 1, 12))
"""
ver arquivo: aula66_sarima_results.txt
"""
results = model.fit()
print(results.summary())

"""
valores previstos
"""
start= len(train)
end = len(train) + len(test) - 1

predictions = results.predict(start, end, typ='levels').rename('SARIMA Predictions')

test['interpolated'].plot(legend=True, figsize=(12,8))
predictions.plot(legend=True)

"""
Performance do modelo
"""

from statsmodels.tools.eval_measures import rmse

error = rmse(test['interpolated'], predictions)

print(error)

print(test['interpolated'].mean())

"""
# FORECAST INTO THE UNKNOWN FUTURE
"""
model = SARIMAX(df['interpolated'], order=(2, 1, 1), seasonal_order=(1, 0, 1, 12))

results = model.fit()

fcast = results.predict(len(df), len(df)+11, typ='levels').rename('SARIMA FORECAST') # previsões p/ 1 ano à frente

df['interpolated'].plot(legend=True, figsize=(12,8))
fcast.plot(legend=True)

"""
#68 SARIMAX
"""
import pandas as pd
import numpy as np

# Ignore harmless warnings
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('RestaurantVisitors.csv', index_col='date', parse_dates=True)
df.index.freq = 'D'
print(df.head())
print(df.tail())

df1 = df.dropna()

print(df1.columns)
cols = ['rest1', 'rest2', 'rest3', 'rest4', 'total']

for column in cols:
    df1[column] = df1[column].astype(int)

print(df1.head())

df1['total'].plot(figsize=(16,5))

ax = df1['total'].plot(figsize=(16,5))

"""
Abaixo, retorna apenas as datas em que
onde df1 é holiday. Em formato SQL:
"""
print(df1.query('holiday==1').index)
"""
Outra forma de retornar os index em que
há holiday
"""
print(df1[df1['holiday']==1].index)
"""
Para cada feriado, adicionar uma reta
vertical ao gráfico
"""
ax = df1['total'].plot(figsize=(16,5))
for day in df1.query('holiday==1').index:
    ax.axvline(x=day, color='black', alpha=0.8)

"""
"""

from statsmodels.tsa.seasonal import seasonal_decompose

results = seasonal_decompose(df1['total'])

results.plot()

results.seasonal.plot(figsize=(18,5))

"""
CLÁSSICO SARIMA (SEM VARIÁVEIS EXÓGENAS)
"""
print(len(df1))

train = df1.iloc[:436]
test = df1.iloc[436:]

from pmdarima import auto_arima

"""
P/ pegar as ordens, é bom passar todo o
dataset. No entanto, para avaliar as previsões
do modelo que utilizamos o dataset test.
"""
print(auto_arima(df1['total'], seasonal=True, m=7).summary())

"""
"""
from statsmodels.tsa.statespace.sarimax import SARIMAX

# ValueError: non-invertible starting MA parameters found
model = SARIMAX(train['total'], order=(1,0,0), seasonal_order=(2,0,0,7),
                enforce_invertibility=False)

results = model.fit()

print(results.summary())

"""
Avaliação
"""
start = len(train)
end = len(train) + len(test) - 1

predictions = results.predict(start, end).rename('SARIMA Model')

test['total'].plot(legend=True, figsize=(15,8))
predictions.plot(legend=True)

"""
Ver se tem feriados no gráfico acima
"""
ax = test['total'].plot(legend=True, figsize=(15,8))
predictions.plot(legend=True)
for day in df1.query('holiday==1').index:
    ax.axvline(x=day, color='black', alpha=0.9)

"""
rmse do SARIMA sem variáveis exógenas
"""
from statsmodels.tools.eval_measures import rmse

print(rmse(test['total'], predictions))
# rmse = 41,26

"""
média
"""
print(test['total'].mean())

"""
#69 SARIMA
CLÁSSICO SARIMA (COM VARIÁVEIS EXÓGENAS)
Em exógenous, tem que ter 2 colchetes,
para tornar dataframe
"""

print(df1['holiday']) # série
print(df1[['holiday']]) # dataframe

print(auto_arima(df1['total'], exogenous=df1[['holiday']], seasonal=True, m=7).summary())


"""
TRAIN our SARIMAX
"""
model = SARIMAX(train['total'], exog=train[['holiday']], order=(1,0,1), seasonal_order=(1,0,1,7), enforce_invertibility=False)

result = model.fit()

print(result.summary())

"""
Valores previstos
"""
start = len(train)
end = len(train) + len(test) - 1

"""
OBSERVAÇÃO IMPORTANTE:
o modelo result NÃO sabe os valores de fato
dos totais do futuro, mas ele SABE os valores
das variáveis exógenas.
"""
predictions = result.predict(start, end, exog=test[['holiday']]).rename('SARIMAX with Exog')

predictions.plot(figsize=(12,8), legend=True)
test['total'].plot(legend=True)

#

ax = test['total'].plot(legend=True)
predictions.plot(figsize=(12,6), legend=True)
for day in test.query('holiday==1').index:
    ax.axvline(x=day, color='black', alpha=0.9)

"""
rmse do SARIMA com variáveis exógenas
"""
from statsmodels.tools.eval_measures import rmse

print(rmse(test['total'], predictions))
# SEM EXÓGENAS: rmse = 41,26
# COM EXÓGENAS: rmse = 22,49

"""
Acima, a queda do rmse é um grande indicativo
de que vale a pena adicionar as variáveis
exógenas do futuro.
Modelo completo abaixo.
"""
model = SARIMAX(df1['total'], exog=df1[['holiday']], order=(1,0,1), seasonal_order=(1,0,1,7), enforce_invertibility=False)

results = model.fit()

print(df.tail())

print(df[477:])

exog_forecast = df[478:][['holiday']] # dois colchetes: dataframe e não series
print(exog_forecast)

"""
PREVISÃO PARA O FUTURO NÃO CONHECIDO
"""
fcast = results.predict(len(df1), len(df1)+38, exog=exog_forecast).rename('FINAL SARIMAX FORECAST')

df1['total'].plot(figsize=(15,8), legend=True)
fcast.plot(legend=True)

# Adicionando ao gráfico as linhas dos feriados

ax = df1['total'].plot(figsize=(15,8), legend=True)
fcast.plot(legend=True)
for day in df.query('holiday==1').index:
    ax.axvline(x=day, color='black', alpha=0.8)

# Zoom no gráfico: a partir de 2017-01-01

ax = df1['total'].loc['2017-01-01':].plot(figsize=(15,8), legend=True)
fcast.plot(legend=True)
for day in df.query('holiday==1').index:
    ax.axvline(x=day, color='black', alpha=0.8)


"""
#71 VAR
"""

import pandas as pd
import numpy as np

# Ignore harmless warnings
import warnings
warnings.filterwarnings('ignore')

# Load specific forecasting tools
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller
from statsmodels.tools.eval_measures import rmse

# Load datasets
df = pd.read_csv('M2SLMoneyStock.csv', index_col=0, parse_dates=True)
df.index.freq = 'MS'

sp = pd.read_csv('PCEPersonalSpending.csv', index_col=0, parse_dates=True)
sp.index.freq = 'MS'

print(df.head())
print(sp.head())

print(df.join(sp))

df = df.join(sp)

print(df)

print(df.shape)
df = df.dropna()
print(df.shape)

df.plot(figsize=(10,8))

"""
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

adf_test(df['Money']) # não estacionário
adf_test(df['Spending']) # não estacionário

print(df.diff())

df_transformed = df.diff() # Diferenciação de primeira ordem

adf_test(df_transformed['Money']) # não estacionário
adf_test(df_transformed['Spending']) # estacionário

df_transformed = df_transformed.diff().dropna() # Diferenciação de segunda ordem

print(df_transformed)

adf_test(df_transformed['Money']) # estacionário
adf_test(df_transformed['Spending']) # estacionário

print(df_transformed.head())
print(df_transformed.shape) # 250 x 2

"""
"""

# Num of Observations
nobs = 12
train = df_transformed[:-nobs] # start = beginning of DF -->> -12 from the end
test = df_transformed[-nobs:] # start -12 from the end of DF --> go to the end of DF

print(test)

"""
Escolher a ordem do VAR
GRIDSEARCH FOR ORDER p AR of VAR model
NÃO funciona o auto_arima!
Tem que fazer por looping
"""
model = VAR(train)

for p in [1,2,3,4,5,6,7]: # range(8)
    
    results = model.fit(p)
    print(f'ORDER {p}')
    print(f'AIC: {results.aic}')
    print('\n')

results = model.fit(5)

print(results.summary())


"""
#72 VAR
"""

# Grab 5 lagged values, right before the test starts!
# Numpy array

print(train.values.shape) # 238 x 2

print(train.values[-5:].shape) # 5 x 2

lagged_values = train.values[-5:]

print(results.forecast(y=lagged_values, steps=12))

z = results.forecast(y=lagged_values, steps=12)

print(z)

idx = pd.date_range('2015-01-01', periods=12, freq='MS')

print(idx)
print(test)

df_forecast = pd.DataFrame(data=z, index=idx, columns=['Money_2d', 'Spending_2d'])
print(df_forecast)

print(test)

"""
Invert the Transformation
Remember that the forecasted values represent second-order differences. To compare them to the original data we have to roll back each difference. To roll back a first-order difference we take the most recent value on the training side of the original series, and add it to a cumulative sum of forecasted values. When working with second-order differences we first must perform this operation on the most recent first-order difference.

Here we'll use the nobs variable we defined during the train/test/split step.
"""
################# MONEY
# Add the most recent first difference from the training side of the original dataset to the forecast cumulative sum
df_forecast['Money1d'] = (df['Money'].iloc[-nobs-1]-df['Money'].iloc[-nobs-2]) + df_forecast['Money_2d'].cumsum()

# Now build the forecast values from the first difference set
df_forecast['MoneyForecast'] = df['Money'].iloc[-nobs-1] + df_forecast['Money1d'].cumsum()

################# SPENDING
# Add the most recent first difference from the training side of the original dataset to the forecast cumulative sum
df_forecast['Spending1d'] = (df['Spending'].iloc[-nobs-1]-df['Spending'].iloc[-nobs-2]) + df_forecast['Spending_2d'].cumsum()

# Now build the forecast values from the first difference set
df_forecast['SpendingForecast'] = df['Spending'].iloc[-nobs-1] + df_forecast['Spending1d'].cumsum()

print(df.head())

print(df_forecast.head())


"""
"""
print(test)

print(df[-nobs:])

test_range = df[-nobs:]

#
test_range.plot()

#
test_range.plot(figsize=(12,8))

#
print(df_forecast.columns)

df_forecast[['MoneyForecast', 'SpendingForecast']].plot(figsize=(12,8))


"""
COMPARAÇÃO GRÁFICA DAS PREVISÕES
"""
# Money
test_range['Money'].plot(legend=True, figsize=(12,8))
df_forecast['MoneyForecast'].plot(legend=True)

# Spending
test_range['Spending'].plot(legend=True, figsize=(12,8))
df_forecast['SpendingForecast'].plot(legend=True)

"""
AVALIAÇÃO DAS PREVISÕES PELO RMSE
"""
# Money - rmse = 43.7
print(rmse(test_range['Money'], df_forecast['MoneyForecast']))
print(test_range['Money'].mean())

# Spending - rmse = 37.0
print(rmse(test_range['Spending'], df_forecast['SpendingForecast']))
print(test_range['Spending'].mean())

"""
#74 VARMA
copiado do jupyter notebook
"""





"""
"""


"""
"""



"""
"""



"""
"""



"""
"""



"""
"""


"""
"""


"""
"""


"""
"""


"""
"""


"""
"""


