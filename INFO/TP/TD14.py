#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 14:07:33 2026

@author: zhuang@pedagogique.local
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spint

f = 50 # Hz
A = 6 # V
U0 = 5 # V
T = 1/f

def u(t):
    """
        In: t float
        Out: float
    """
    return A * np.sin(2*np.pi*f*t) + U0

def trap(f, a, b, N):
    """
        In: f fonction, a float, b float, N entier
        Out: float
    """
    d = (b-a) / N
    k1 = a
    k2 = a+d
    res = 0
    for k in range(N):
        res += (f(k1) + f(k2))*d/2
        k1 += d
        k2 += d
    return res
    

t = np.linspace(-2*T, 2*T, 1000)
ut = u(t)

plt.plot(t, ut)

print("u_moy: ", trap(u, 0, T, 1000)/T)
print("u_eff: ", (trap(lambda t: u(t)**2, 0, T, 1000)/T) ** (0.5))


#%% Ex 2 ========================================================================

R = 8.314e-3 # kJ mol-1 K-1

Ae = 5.6 # kJ mol-1
Te = 120 # degree
Emoy = 5.6 # kJ mol-1
def E(theta):
    """
        In: theta float
        Out: float en kJ mol-1
    """
    return Ae * np.cos(2*np.pi*theta/Te) + Emoy

def k(T):
    """
        In: T float en K
        Out: float
    """
    integrale = spint.quad( lambda theta: np.exp(-E(theta)/(R * T)) , 0, 360)[0]
    return 1 / integrale
    
def p(theta, T):
    """
        In: theta float en degree, T float en K
        Out: float
    """
    return k(T) * np.exp(- E(theta) / (R * T))
    

t = np.linspace(0, 360, 1000)

Tl = [50, 150, 250, 350, 450, 550]

for T in Tl:
    pl = p(t, T)
    plt.plot(t, pl, label=f"p(theta) pour T = {T} K")

plt.legend()

print("Ex 2.2: ", k(298))


#%% Ex 3 ======================================================================

l = 10 # m
g = 9.81 # m s-1

def rect(f, a, b, N):
    """
        In: f fonction, a float, b float, N entier
        Out: float
    """
    d = (b-a) / N
    k1 = a
    k2 = a+d
    res = 0
    for k in range(N):
        res += f((k1+k2) / 2)*d
        k1 += d
        k2 += d
    return res

def T(theta0):
    """
        In: theta0 en degrees
        Out: periode en s
    """
    integrale = rect(lambda theta: 1 / (2 * (np.cos(theta * 2 * np.pi / 360) - np.cos(theta0 * 2 * np.pi / 360)))**0.5, 0, theta0, 1000)
    return 4 * (l / g)**0.5 * integrale

print("Ex 3.1: ", T(1))



























