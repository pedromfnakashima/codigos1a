# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:54:32 2020

@author: pedro
"""
globals().clear()
import numpy as np

""" Multiplicação de matrizes """
A = np.array([[2,5,9], [3,6,8]])
print(A.shape)
print(A)
print(A.transpose())
B = np.array([[2,7],[4,3], [5,2]])
print(B.shape)
print(B)
print(B.transpose())
print(np.matmul(A,B))

# Matriz inversa
A = np.array([[2,1], [5,3]])
print(A)
A_inv = np.linalg.inv(A)
print(A_inv)

A_A1 = np.matmul(A, A_inv)
print(A_A1)

""" Mínimos quadrados
https://www.mathsisfun.com/data/least-squares-regression.html
"""
print(np.ones(5))

X = np.matrix([np.ones(5),[2,3,5,7,9]]).T
y = np.matrix([[4,5,7,10,15]]).T

XT = X.T

XT_X = np.matmul(XT,X)

XT_X_inv = np.linalg.inv(XT_X)

XT_y = np.matmul(XT,y)

betas = np.matmul(XT_X_inv, XT_y)
print(beta)

import matplotlib.pyplot as plt

print(np.linspace(2,3,2))
xx = np.linspace(2, 3, 2)
yy = np.array(betas[0] + betas[1] * xx)

plt.figure(1)
plt.plot(xx, yy.T, color='b')
plt.scatter(input[:,0], input[:,1], color='r')
plt.show()

