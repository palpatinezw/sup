#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 08:17:27 2025

@author: zhuang@pedagogique.local
"""

import matplotlib.pyplot as plt
import numpy as np
import random


def tracesuite(N):
    """
        In: entier N
        Out: null
        Affichage plot d une suite
    """
    u = []
    for i in range(N):
        if i == 0: 
            u.append(1)
        else:
            u.append((u[i-1] + 1)**(0.5))
            
    plt.plot(u, 'o')
    plt.show()

def tracesin():
    """
        In: null
        Out: null
        Affichage courbe sinus
    """
    
    t = np.linspace(0, 15, 100)
    ys = np.sin(t)
    yc = np.cos(t)
    
    plt.plot(t, ys, 'b-', label="sin t")
    plt.plot(t, yc, 'r--', label="cos t")
    
    plt.xlabel("t")
    plt.legend()
    plt.axis([0, 4*np.pi, None, None])
    
    plt.show()
    
# =============================================================================
# Ex 1

def ex1():
    c0 = 1
    k = 0.1
    tmax = 50
    t = np.linspace(0, tmax, 100)
    
    plt.plot(t, c0 * np.exp(-k * t), '-b', label="[CH3CHO]")
    plt.plot(t, c0 * (1 - np.exp(-k * t)), '-r', label="[CH4]")
    
    plt.axis([0, tmax, 0, None])
    plt.xlabel("Temps t / s")
    plt.ylabel("Concentration c / mol L-1")
    plt.legend()
    plt.title("Cinetique chimique")
    
    plt.show()


def ex2():
    def lssuite(N, mu):
        """
            In: N entier, mu nombre
            Out: liste N termes de la suite (x(mu))
        """
        x = []
        for i in range(N):
            if i == 0:
                x.append(0.1)
            else:
                xp = x[i-1]
                x.append( mu * xp * (1-xp) )
                
        return x
    
    plt.subplot(311)
    plt.plot(lssuite(50, 1), '-*', label="mu = 1")
    plt.subplot(312)
    plt.plot(lssuite(50, 3.1), '-o', label="mu = 3.1")
    plt.subplot(313)
    plt.plot(lssuite(50, 3.9), '-D', label="mu = 3.9")
    
    plt.legend()
    
    plt.show()


def ex3():
    tau = 1
    E = 10
    
    t = np.linspace(0, 5*tau, 100)
    
    uc = E*(1 - np.exp(-t/tau))
    ur = E*(np.exp(-t/tau))
    plt.plot(t, uc, label="u_c(t)")
    plt.plot(t, ur, label="u_R(t)")
    
    plt.legend()
    plt.axis([0, 5*tau, 0, E])
    
    
    plt.figure(2)
    plt.plot(uc, ur)
    
    
    plt.show()

def ex4():
    omega0 = 1e4 # rad s-1
    lsxi = [0,0.2,0.5,0.8]
    A = 1 # V
    
    t = np.linspace(0, (8*np.pi) / omega0, 10000) 
    
    lsu = [A * np.cos(omega0 * ((1 - xi**2)**0.5) * t) * np.exp(-xi*omega0*t) for xi in lsxi]
    
    for i in range(len(lsu)):
        u = lsu[i]
        xi = lsxi[i]
        plt.plot(t, u, label=f"xi = {xi}")
        
    plt.plot(t, A * np.exp(- lsxi[1] * omega0 * t), 'k--')
    plt.plot(t, -A * np.exp(- lsxi[1] * omega0 * t), 'k--')
        
    plt.legend()
        
    plt.show()


def ex5():
    def marcheal(N):
        """
            In: N entier naturel
            Out: 2 listes des entiers resultat marche aleatoire
        """
        
        x = [0]
        y = [0]
        
        dx = [1,-1, 0, 0]
        dy = [0, 0, 1,-1]
        
        for i in range(N):
            k = random.randint(0, 3)
            x.append(x[-1] + dx[k])
            y.append(y[-1] + dy[k])
        
        return (x, y)
    
    for i in range(10):
        marche = marcheal(1500)
        plt.plot(marche[0], marche[1], 'o')

    plt.axis('equal')
    
    plt.show()


def ex6():
    t = np.linspace(0, 2*np.pi, 100)
    
    x = np.sin(t) / (1 + (np.cos(t))**2)
    y = (np.sin(t) * np.cos(t)) / (1 + (np.cos(t))**2)
    
    plt.plot(x, y)
    
    plt.axis('equal')
    
    plt.show()


def ex7():
    N = 50
    f = 1 # Hz
    b = 1 # m
    
    t = np.linspace(0, 1/f, N)
    
    r = (b/2) * ( 1 + np.cos(2 * np.pi * f * t) )
    th = 2 * np.pi * f * t
    
    # plt.polar( th, r )    
    plt.plot( r * np.cos(th), r * np.sin(th), '-*' )


















































