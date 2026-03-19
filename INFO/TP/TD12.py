#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 14:07:12 2026

@author: zhuang@pedagogique.local
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco

# Ex 1 ========================================================================

def g(x):
    """
        In: x (float)
        Out: float
    """
    return -0.2 * (x ** 3) + (x ** 2) + 0.5 * x + 1

# x = np.linspace(4, 6, 1000)
# y = g(x)

# plt.plot(x, y)
# plt.plot(x, np.zeros_like(x))

def dicho(f, a, b, epsilon):
    """
        In: f (fonction), a (float), b(float), epsilon(float)
        Out: (float; int)
    """
    nbIter = 0
    while b - a > 2 * epsilon:
        nbIter += 1
        mil = (a+b)/2
        if (f(a) * f(mil)) > 0:
            a = mil
        else:
            b = mil
    return ((a+b)/2, nbIter)
            
# Ex 2 ========================================================================

K0 = 1.43e-4
P0 = 1 # bar
def equil(tau, P):
    """
        In: tau (float), P (float) en bar
        Out: float
        Renvoie K
    """
    return ( ( tau * ((3 - 2 * tau) ** 2) * (P0**2)) - K0 * (4 * ((1 - tau)**3)) * ( (P) ** 2 ) )

# print(dicho( lambda t : equil(t, 100) , 0, 1, 1e-3))


# pliste = np.linspace(1, 1000, 1000)
# tau = [dicho(lambda t : equil(t, p), 0, 1, 1e-3)[0] for p in pliste]

# plt.plot(pliste, tau)

# Ex 3 ========================================================================

theta = 30/(60*360) * 2 * np.pi # rad 
f2 = 0.02 # m
d = 0.01 # m
D = 0.05 # m

def jumelle(f1):
    """
        In: f1 (float)
        Out: float
    """
    return (theta * 2 * (f1 + f2) * f1) - (d * f1 - D * f2)

# f1l = np.linspace(0, 0.2)
# yl = [jumelle(f1) for f1 in f1l]
# plt.plot(f1l, yl)

# print(dicho(jumelle, 0, 0.2, 1e-4))

# Ex 4 ========================================================================

def eq(x):
    return x**2 - 10

print(dicho(eq, 0, 5, 1e-6))




































