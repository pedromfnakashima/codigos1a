# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 11:42:00 2020

@author: pedro

https://www.youtube.com/watch?v=Pkvdc2Z6eBg&list=PLK0ACuwY6WaoE-YfzsxnkBw6udvWUTNAi&index=6&t=294s

https://github.com/Pitsillides91/Python-Tutorials/blob/master/Seaborn%20Tutorial/Python%20Seaborn%20Tutorial%20for%20Beginners%20v2.ipynb

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
caminho_wd = caminho_base / 'Dados' / 'Cursos e Livros' / 'Data 360 YP (Youtube)' / 'Seaborn'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

##########################################################################################################
##########################################################################################################
##########################################################################################################

import os #provides functions for interacting with the operating system
import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns

'''
1. Loading the Raw Data
'''
# Loading the data

raw_data = pd.read_csv("Marketing Raw Data.csv")
# runs all the data
print(raw_data)

print(raw_data.shape)

#runs the first 5 rows
print(raw_data.head())

'''
2. Line Gragh
'''
# Example 1 - Simple 1 line graph
# Assuming we want to investigate the Revenue by Date
ax = sns.lineplot(x='Week_ID', y='Revenue', data = raw_data)

# Notes: error bands show the confidence interval

# Example 2 - Adding Categories

# By Promo
ax = sns.lineplot(x='Week_ID', y='Revenue', hue = 'Promo', data = raw_data)

# Example 3 - By Promo with style
ax = sns.lineplot(x='Week_ID', y='Revenue', hue = 'Promo', style = 'Promo', data = raw_data)

# Example 4 - By Promo with style & Increase the size & Remove error bars

# increase the size, remove ci
sns.set(rc={'figure.figsize':(12,10)})
ax = sns.lineplot(x='Week_ID', y='Revenue', hue = 'Promo', style = 'Promo', data = raw_data, ci=None)

# Example 5 - By Promo with style & Increase the size & Remove error bars & adding markers & by month
ax = sns.lineplot(x='Month_ID', y='Revenue', hue = 'Promo', style = 'Promo', data = raw_data, ci=None,  markers=True)

# Example 6 - By Day_Name with style & Increase the size & Remove error bars & adding markers & by month
ax = sns.lineplot(x='Month_ID', y='Revenue', hue = 'Day_Name', style = 'Promo', data = raw_data, ci=None,  markers=True)

# Example 7 - By Year with style & Increase the size & Remove error bars & adding markers & by month
ax = sns.lineplot(x='Year', y='Revenue', hue = 'Day_Name', style = 'Promo', data = raw_data, ci=None,  markers=True)

'''
3. Bar Plots
'''
# Example 1 - Total Revenue by Month

ax = sns.barplot(x="Month_ID", y="Revenue", data=raw_data)

# Notes: 
# 1 - the lines signify the confidence interval
# 2 - Takes mean by default

raw_data[['Month_ID', 'Revenue']].groupby('Month_ID', as_index = False).agg({'Revenue':'mean'})

# Example 2 - Total Revenue by Month - Remove the Confidence Interval
ax = sns.barplot(x="Month_ID", y="Revenue", data=raw_data, ci=False)

# Example 3 - Total Revenue by Month - Remove the Confidence Interval - By Promo
ax = sns.barplot(x="Month_ID", y="Revenue", data=raw_data, ci=False, hue = 'Promo')

# Example 4 - Total Revenue by Month - Remove the Confidence Interval - By Promo - Changing direction
ax = sns.barplot(x="Revenue", y="Year", ci=False, hue = 'Promo', orient = 'h', data=raw_data)

# Example 5 - Total Revenue by Month - Remove the Confidence Interval - By Promo - Changing direction - Changing Colour
ax = sns.barplot(x="Revenue", y="Year", ci=False, hue = 'Promo', orient = 'h', data=raw_data, color="#1CB3B1")

# Cool Way to pick colours
# https://htmlcolorcodes.com/color-picker/

'''
4. Histograms
'''
# Example 1 - Investigating the distribution of Revenue

x = raw_data['Revenue'].values

sns.distplot(x, color = 'blue');

# As you can see, it's a bit imbalance. Right skewd distribution as the mean is to the right

# Example 2 - Investigating the distribution of Revenue, adding the mean

x = raw_data['Revenue'].values

sns.distplot(x, color = 'blue');

# Calculating the mean
mean = raw_data['Revenue'].mean()

#ploting the mean
plt.axvline(mean, 0,1, color = 'red')

# Example 3 - Investigating the distribution of Visitors, adding the mean

x = raw_data['Visitors'].values

sns.distplot(x, color = 'red');

# Calculating the mean
mean = raw_data['Visitors'].mean()

#ploting the mean
plt.axvline(mean, 0,1, color = 'blue')

'''
5. Box Plots
'''
# Example 1 - Investigating the distribution of Revenue

x = raw_data['Revenue'].values

ax = sns.boxplot(x)

print('The meadian is: ', raw_data['Revenue'].median())

# Notes:
# The line signifies the median
# The box in the middle show the beginning of Q1 (25th percentile) and the end of the Q3 (75th percentile)
# The whiskers (left - right) show the minimum quartile and maximum quartile
# The dots on the right are "outliers"

# More Details

PATH = "F:\\Github\\Python tutorials\\Introduction to Seaborn\\"
Image(filename = PATH + "Seaborn boxplot.png", width=900, height=900)

# More details here: https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51
# Credits: Michael Galarnyk

# Example 2 - Investigating the distribution of Revenue by Day

ax = sns.boxplot(x="Day_Name", y="Revenue", data=raw_data)

# Example 3 - Investigating the distribution of Revenue by Day - Horizontal - change color

ax = sns.boxplot(x="Revenue", y="Day_Name", data=raw_data, color = '#EE67CF')

# Cool Way to pick colours
# https://htmlcolorcodes.com/color-picker/

# Example 4 - Investigating the distribution of Revenue by Day - changing color - adding hue

ax = sns.boxplot(x="Day_Name", y="Revenue", data=raw_data, color="#B971E7", hue = 'Promo')

# Cool Way to pick colours
# https://htmlcolorcodes.com/color-picker/

# Example 5 - Investigating the distribution of Revenue by Day - by color - by data points

ax = sns.boxplot(x="Day_Name", y="Revenue", data=raw_data, color = '#D1EC46')
ax = sns.swarmplot(x="Day_Name", y="Revenue", data=raw_data, color="red")

'''
6. ScatterPlots
'''
print(raw_data.columns)
# Example 1 - Relationship between Marketing Spend and Revenue

ax = sns.scatterplot(x="Marketing Spend", y="Revenue", data=raw_data, color = 'green')

ax = sns.scatterplot(x="Marketing Spend", y="Revenue", data=raw_data, color = 'green', hue = 'Promo', style = 'Promo')

# Example 3 - Relationship between Marketing Spend and Revenue - changing color & hue - adding size

ax = sns.scatterplot(x="Marketing Spend", y="Revenue", data=raw_data, color = 'green', hue = 'Promo', size = 'Revenue',
                    sizes=(20, 200))

# Example 4 - Relationship between Marketing Spend and Revenue - changing color & hue - adding size - by day

ax = sns.scatterplot(x="Visitors", y="Revenue", data=raw_data, color = 'green', hue = 'Day_Name', size = 'Revenue',
                    sizes=(20, 200))

'''
7. lmPlots
'''
# Example 1 - Relationship between Marketing Spend and Revenue

ax = sns.lmplot(x="Marketing Spend", y="Revenue", data=raw_data, height=9)

# Notes:
# What is Linear Regression: It is a predictive statistical method for modelling the relationship between x (independent variable) & y (dependent V).
# How it works (cost function MSE): https://towardsdatascience.com/machine-learning-fundamentals-via-linear-regression-41a5d11f5220


# Example 2 - Relationship between Marketing Spend and Revenue - changing color, hue & Style

ax = sns.lmplot(x="Marketing Spend", y="Revenue", data=raw_data, hue = 'Promo', ci= False, height=9, markers=["o", "x", "+"])


# Example 3 - Relationship between Marketing Spend and Revenue - by column

ax = sns.lmplot(x="Marketing Spend", y="Revenue", data=raw_data, col = 'Promo', ci= False, height=5, 
                line_kws={'color': 'red'}, 
                scatter_kws={'color':'#ADC11E'})

# Example 4 - Relationship between Marketing Spend and Revenue - by column - by day - add Jitter too

ax = sns.lmplot(x="Visitors", y="Revenue", data=raw_data, col = 'Day_Name', ci= False, height=4, 
                line_kws={'color': '#031722'}, 
                scatter_kws={'color':'#1E84C1'},
               col_wrap=3,
               x_jitter=.3)

'''
8. SubPlots
'''
# Set up the matplotlib figure
fig, axes = plt.subplots(2, 2, figsize=(12, 7))

a = raw_data['Revenue'].values
b = raw_data['Visitors'].values
c = raw_data['Marketing Spend'].values


# plot 1
sns.distplot(a, color = 'blue', ax=axes[0,0])

# plot 2
sns.distplot(b, color = 'blue', ax=axes[0,1])

# plot 3
sns.distplot(c, color = 'blue', ax=axes[1,0])

# plot 4
sns.boxplot(x="Revenue", y="Day_Name", data=raw_data, color = '#52F954', ax=axes[1,1])
sns.swarmplot(x="Revenue", y="Day_Name", data=raw_data, color="blue", ax=axes[1,1])

'''
9. Pairplots
'''
g = sns.pairplot(raw_data, plot_kws={'color':'green'})


# Example 2 - running on specific columns - green color
g = sns.pairplot(raw_data[['Revenue','Visitors','Marketing Spend']], plot_kws={'color':'#0EDCA9'})

# Cool Way to pick colours
# https://htmlcolorcodes.com/color-picker/

# Example 3 - running on specific columns - adding hue
g = sns.pairplot(raw_data[['Revenue','Visitors','Marketing Spend', 'Promo']], hue = 'Promo')

# Example 4 - running on specific columns - adding hue - adding kind = reg
g = sns.pairplot(raw_data[['Revenue','Visitors','Marketing Spend', 'Promo']], hue = 'Promo', kind="reg", size = 6)

'''
10. JoinPlots
'''
# Example 1 - Revenue vs marketing Spend Relationship with 
g = sns.jointplot("Revenue", "Marketing Spend", data=raw_data, kind="reg", color = 'green', size = 10)

'''
11. Heat Map
'''

# First we need to create a "Dataset" to display on a Heatmap - we will use a correlation dataset
# .corr() is used to find the pairwise correlation of all columns in the dataframe. Any null values are automatically excluded
# The closer to 1 or -1 the better. As one variable increases, the other variable tends to also increase / decrease
# More Info here: https://statisticsbyjim.com/basics/correlations/

# Example 1 - Heatmap for PC

pc = raw_data[['Revenue','Visitors','Marketing Spend', 'Promo']].corr(method ='pearson')

cols = ['Revenue CC','Visitors CC','Marketing Spend CC']

ax = sns.heatmap(pc, annot=True,
                 yticklabels=cols,
                 xticklabels=cols,
                 annot_kws={'size': 50})


# Example 2 - Heatmap for PC - changing cmap

ax = sns.heatmap(pc, annot=True,
                 yticklabels=cols,
                 xticklabels=cols,
                 annot_kws={'size': 50},
                 cmap="BuPu")

# Examples:
# cmap="YlGnBu"
# cmap="Blues"
# cmap="BuPu"
# cmap="Greens"









