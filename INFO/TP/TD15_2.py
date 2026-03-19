#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 14:02:37 2026

@author: zhuang@pedagogique.local
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


m = 0.1 # kg
g = 10 # m s-2
l = 0.2 # m
J = 4e-3 # kg m2
h = 5e-2 # kg s-1

def euler(f, a, b, N, ci = np.array([0,0])):
    """
        In: f fonction de (y, t); a (float, float); b (float, float); N entier; ci float
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

#%% ===========================================================================

def f(y, t):
    """
        In: y (float, float), t float
        Out: (float, float)
    """
    return np.array( (y[1], -m * g * l * np.sin(y[0]) / J) )

def f_frot(y, t):
    """
        In: y (float, float), t float
        Out: (float, float)
    """
    return np.array( (y[1], -m * g * l * np.sin(y[0]) / J - h * l**2 * y[1] / J) )
    

theta0 = [ 0.5, 1, 1.5, 2, 2.5, 3 ]

for t0 in theta0:
    t, fl = euler(f_frot, 0, 5, 100000, np.array([t0, 0]))
    theta = [vec[0] for vec in fl]
    thetap = [vec[1] for vec in fl]
    plt.plot(t, theta, label=f"theta = {t0}")

plt.legend()

#%%============================================================================

H0 = 600 # m2
HA = 500 # m2
T = 365 # j
kL = 0.1e-3 # L j-1
kR = 1e-3 # R j-1 L-1
kM = 5e-2 # R j-1

def H(t):
    return H0 + HA * np.sin( 2 * np.pi / T * t )

def lr(y, t):
    return np.array([ kL * H(t) * y[0] - kR * y[0] * y[1] , kR * y[0] * y[1] - kM * y[1] ])

t, lr = euler(lr, 0, 1500, 500000, np.array([ 200, 100 ]))
lapin = [e[0] for e in lr]
renard = [e[1] for e in lr]

plt.plot(t, lapin, label="lapin")
plt.plot(t, renard, label="renard")
plt.legend()
plt.twinx()
plt.ylim(-100, 1500)
plt.plot(t, [H(tt) for tt in t], label="herbe", color="green")
plt.legend()

plt.figure()
plt.plot(lapin, renard)






























































