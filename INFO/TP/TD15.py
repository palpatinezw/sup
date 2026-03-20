#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 14:01:58 2026

@author: zhuang@pedagogique.local
"""

import matplotlib.pyplot as plt
from scipy.integrate import odeint

def euler(f, a, b, N, ci = 0):
    """
        In: f fonction de (y, t); a float; b float; N entier; ci float
        Out: lst, lsf (2 listes)
    """
    lst = [a]
    lsf = [ci]
    h = (b-a)/N
    for i in range(N):
        nt = lst[-1] + h
        lst.append(nt)
        lsf.append(lsf[-1] + h * f(lsf[-1], nt))
    
    return lst, lsf


#%% Ex 1

g = 9.81 # m s-2
k1 = 1.8e-3 # SI
k2 = 9.2e-5 # SI
m = 3.6e-3 # kg

intervalle = (0, 15) # s

def flin(v, t):
    """
        In: v float; t float
        Out: float dv/dt
    """
    return g - (k1 / m)*v

def fquad(v, t):
    """
        In: v float; t float
        Out: float dv/dt
    """
    return g - (k2 / m)*(v**2)

for n in [6, 10, 100]:
    lstl, lsfl = euler(flin, intervalle[0], intervalle[1], n)
    plt.plot(lstl, lsfl, label=f"n = {n}")

# lstl, lsfl = euler(flin, intervalle[0], intervalle[1], 100)
# lstq, lsfq = euler(fquad, intervalle[0], intervalle[1], 100)

# plt.plot(lstl, lsfl, label="lineaire euler")
# plt.plot(lstq, lsfq, label="quadratique euler")

# yl = odeint(flin, 0, lstl)
# yq = odeint(fquad, 0, lstq)

# plt.plot(lstl, yl, label="lineaire scipy")
# plt.plot(lstq, yq, label="quadratique scipy")
plt.legend()

#%% Ex 2

k = 0.1 # L mol-1 s-1
a = 1 # mol L-1
b = 0.01 # mol L-1

intv = (0, 100) # s
N = 10000

def f(x, t):
    """
        In: x float, t float
        Out: float dx/dt
    """
    return k * (a-x) * (b+x)

def dicho(ls, x):
    """
        In: ls liste float, x float
        Out: entier
    """
    imin = 0
    imax = len(ls)+1
    while(imax - imin > 1):
        imil = (imin + imax) // 2
        if ls[imil] > x:
            imax = imil
        else: 
            imin = imil
    return imin
    

lst, lsx = euler(f, intv[0], intv[1], N, 0)

plt.plot(lst, lsx, label="avancement volumique")

plt.legend()

lsv = []
for i in range(1, N+1):
    lsv.append((lsx[i] - lsx[i-1]) / (lst[i] - lst[i-1]))
    
plt.figure()
plt.plot(lst[1:], lsv, label="vitesse")

plt.legend()

print("Temps de demi-reaction: ", lst[dicho(lsx, a/2)])





























