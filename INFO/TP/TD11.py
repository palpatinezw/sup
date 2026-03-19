#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 14:08:37 2026

@author: zhuang@pedagogique.local
"""

import numpy as np
import matplotlib.pyplot as plt

N = 11
p0 = np.zeros((N, N))
colorstyle = 'coolwarm'

#  Init murs
for i in range(N):
    p0[0][i] = 20
    p0[i][0] = 20
    p0[N-1][i] = 20
    p0[i][N-1] = 20


# Init porte/fen
for i in range(3,8):
    p0[0][i] = 10
for i in range(6,9):
    p0[i][N-1] = 10
    
# Init radiateur
for i in range(2,5):
    p0[N-2][i] = 60


pk = np.copy(p0)

def evol(pcur):
    """
        In: tableau carre taille N x N
        Out: tableau carre taille N x N
        Une etape d evolution de la temperature
    """
    pnouv = p0.copy()
    for i in range(1,N-1):
        for j in range(1,N-1):
            if p0[i][j] == 0:
                pnouv[i][j] = (pcur[i-1][j] + pcur[i+1][j] + pcur[i][j+1] + pcur[i][j-1])/4
    return pnouv

def norme(M):
    """
        In: matrice
        Out: float
    """
    res = 0.
    for j in range(len(M)):    
        somme = 0.
        for j in range(len(M[i])):
            somme += abs(M[i][j])
        if res < somme: 
            res = somme
    return res
            
pnouv = evol(pk)
while(norme(pnouv - pk) >= 1e-5):
    pk = pnouv
    pnouv = evol(pk)

plt.imshow(pnouv, cmap=colorstyle)
plt.colorbar(label = 'T / °C')

x = np.linspace(0, N-1, N)
y = np.linspace(0, N-1, N)
X, Y = np.meshgrid(x, y)

plt.contour(X, Y, pnouv, 10, cmap = colorstyle)
plt.contourf(X, Y, pnouv, 200, cmap = colorstyle)
















































