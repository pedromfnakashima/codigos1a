# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:11:51 2020

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
#pip install tensorflow
#pip install keras

import keras
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# y = mx + b + noise
m = 2
b = 3
x = np.linspace(0,50,100)

np.random.seed(101)
noise = np.random.normal(loc=0, scale=4, size=len(x))

print(x)

y = 2 * x + b + noise
print(y)

plt.plot(x,y,'*')

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

"""
Adicionando 3 camadas
"""

model.add(Dense(4, input_dim=1, activation='relu'))

model.add(Dense(4, activation='relu'))

model.add(Dense(1, activation='linear'))

model.compile(loss='mse', optimizer='adam')

print(model.summary())

print(model.fit(x,y,epochs=200))

print(model.history.history['loss'])

loss = model.history.history['loss']
epochs = range(len(loss))

plt.plot(epochs, loss)

"""
Previsões
"""

x_for_predictions = np.linspace(0,50,100)

y_pred = model.predict(x_for_predictions)

print(y_pred)

plt.plot(x,y,'*')
plt.plot(x_for_predictions, y_pred, 'r')

"""
Avaliação do modelo
"""

from sklearn.metrics import mean_squared_error

print(mean_squared_error(y, y_pred))

"""
#83
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Alcohol_Sales.csv', index_col='DATE', parse_dates=True)
df.index.freq = 'MS'

print(df.head())

df.columns = ['Sales']

df.plot(figsize=(12,8))

from statsmodels.tsa.seasonal import seasonal_decompose

results = seasonal_decompose(df['Sales'])

results.plot()

results.seasonal.plot(figsize=(12,8))

print(results.seasonal)

"""
Train-Test split
Previsão 12 meses a frente
"""
print(len(df)) # 325
print(325-12) # 313

train = df.iloc[:313]
test = df.iloc[313:]

print(len(test)) # 12

ser = np.array([23,56,2,13,14])

print(ser.max()) # 56 (fit)

"""
Normalizando
Dividindo pelo maior valor
Todos os números entre 0 e 1
"""
print(ser/ser.max()) # (transform)


"""
Escalar automaticamente usando
sklearn
"""
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

"""
IMPORTANTE
fit apenas para dados train
(caso contrário, assumiria
 que há informação sobre o
 futuro, é pra usar o fit
 apenas para dados conhecidos)
"""
print(scaler.fit(train)) # finds the max value in train data

scaled_train = scaler.transform(train)
scaled_test = scaler.transform(test)

"""
#84
"""
from keras.preprocessing.sequence import TimeseriesGenerator

print(scaled_train)

print(scaled_test)

print(scaled_train[:5])

n_input = 3
n_features = 1

generator = TimeseriesGenerator(scaled_train, scaled_train, length=n_input, batch_size=1)

print(len(scaled_train)) # 313
print(len(generator)) # 310

print(generator[0])

X,y = generator[0]

print(X.shape)

print(X)
print(y)

"""
#85
"""
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

n_input = 12 # 12 meses
n_features = 1 # 1 coluna de dados

train_generator = TimeseriesGenerator(scaled_train, scaled_train, length=n_input, batch_size=1)

model = Sequential()

model.add(LSTM(150, activation='relu', input_shape=(n_input, n_features)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

print(model.summary())

model.fit_generator(train_generator, epochs=25)

print(model.history.history.keys())

#plt.plot(range(len(model.history.history['loss'])), model.history.history['loss'])
myloss = model.history.history['loss']
plt.plot(range(len(myloss)), myloss)

# 12 history steps ---> step 13
# last 12 points train --> pt 1 of test data

first_eval_batch = scaled_train[-12:]

print(first_eval_batch)

first_eval_batch.reshape((1,n_input,n_features))

print(first_eval_batch.reshape((1,n_input,n_features)))

first_eval_batch = first_eval_batch.reshape((1,n_input,n_features))

print(model.predict(first_eval_batch))

print(scaled_test)

"""
FORECAST USING RNN MODEL
"""
#holding my predictions
test_predictions = []

# Las n_input points from the training set
first_eval_batch = scaled_train[-n_input:]
# reshape this to the format RNN wants (same format as TimeseriesGenerator)
current_batch = first_eval_batch.reshape((1,n_input,n_features))

# how far into the future will I forecast?
# len(test) --> 24
for i in range(len(test)):
    
    # One timestep ahead of historical 12 points
    current_pred = model.predict(current_batch)[0]
    
    # store that prediction
    test_predictions.append(current_pred)
    
    # UPDATE current batch to include prediction
    current_batch = np.append(current_batch[:,1:,:],[[current_pred]], axis=1)

#holding my predictions
test_predictions = []

# Las n_input points from the training set
first_eval_batch = scaled_train[-n_input:]
# reshape this to the format RNN wants (same format as TimeseriesGenerator)
current_batch = first_eval_batch.reshape((1,n_input,n_features))

print(model.predict(current_batch)[0])

my_first_pred = model.predict(current_batch)[0]
print(my_first_pred)

print(current_batch)

print(current_batch.shape)

print(current_batch[:,1:,:])

print(np.append(current_batch[:,1:,:], [[my_first_pred]], axis=1))

"""
"""
#holding my predictions
test_predictions = []

# Las n_input points from the training set
first_eval_batch = scaled_train[-n_input:]
# reshape this to the format RNN wants (same format as TimeseriesGenerator)
current_batch = first_eval_batch.reshape((1,n_input,n_features))

# how far into the future will I forecast?
# len(test) --> 24
for i in range(len(test)):
    
    # One timestep ahead of historical 12 points
    current_pred = model.predict(current_batch)[0]
    
    # store that prediction
    test_predictions.append(current_pred)
    
    # UPDATE current batch to include prediction
    current_batch = np.append(current_batch[:,1:,:],[[current_pred]], axis=1)

print(test_predictions)

# Inverter o escalonamento

true_predictions = scaler.inverse_transform(test_predictions)

print(true_predictions)

print(test)

test['Predictions'] = true_predictions

print(test)

test.plot(figsize=(12,8))

"""
"""
model.save('mycoolmodel.h5')

"""
"""
from keras.models import load_model
new_model = load_model('mycoolmodel.h5')

print(new_model.summary())

"""
FORECAST INTO UNKNOWN FUTURE
"""
#holding my predictions
test_predictions = []

# Las n_input points from the training set
first_eval_batch = scaled_train[-n_input:]
# reshape this to the format RNN wants (same format as TimeseriesGenerator)
current_batch = first_eval_batch.reshape((1,n_input,n_features))

# how far into the future will I forecast?
# len(test) --> 24
for i in range(50):
    
    # One timestep ahead of historical 12 points
    current_pred = model.predict(current_batch)[0]
    
    # store that prediction
    test_predictions.append(current_pred)
    
    # UPDATE current batch to include prediction
    current_batch = np.append(current_batch[:,1:,:],[[current_pred]], axis=1)

print(test_predictions)

# Inverter o escalonamento

true_predictions = scaler.inverse_transform(test_predictions)

print(true_predictions)








"""
"""