#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 08:20:03 2026

@author: zhuang@pedagogique.local
"""

import random as rd
import time
import matplotlib.pyplot as plt

def est_triee(L):
    """
        In: L (liste)
        Out: Bool
    """
    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            return False
        
    return True

def tri_selection(L):
    """
        In: L (liste)
        Out: liste L modifie
    """
    for i in range(len(L), 0, -1):
        maxidx = 0
        for j in range(i):
            if L[j] > L[maxidx]:
                maxidx = j
        L[i-1], L[maxidx] = L[maxidx], L[i-1]
    return L

def tri_insertion(L):
    """
        In: L (liste)
        Out: liste L triee
    """
    for i in range(1, len(L)):
        j = i-1
        while j >= 0 and L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            j -= 1
        
    return L

def tri_bulle(L):
    """
        In: L (liste)
        Out: liste L triee
    """
    for i in range(len(L)-1, 0, -1):
        for j in range(i):
            if L[j] > L[j+1]:
                L[j+1], L[j] = L[j], L[j+1]
    return L

def melange(L):
    """
        In: L (liste)
        Out: liste L triee
    """
    N = len(L)
    nL = []
    for i in range(N):
        i = rd.randint(0, len(L)-1)
        nL.append(L[i])
        L.remove(L[i])
    L = nL
    return L

def tri_stupide(L):
    """
        In: L (liste)
        Out: liste L triee
    """
    while not est_triee(L):
        L = melange(L)
    return L

def listealea(a, b, N):
    """
        In: a (entier); b (entier); N (entier)
        Out: liste de N entiers
    """
    return [rd.randint(a, b) for i in range(N)]

def listeinvers(N):
    """
        In: N entier
        Out: liste de N entiers
    """
    return [i for i in range(N, 0, -1)]

def listetriee(N):
    """
        In: N entier
        Out: liste de N entiers
    """
    return [i for i in range(1, N+1)]

def k_presque_triee(N, k):
    """
        In: N entier; k entier
        Out: liste de N entiers
    """
    lc = listetriee(N)
    for i in range(k//2):
        a = rd.randint(0, N-1)
        b = rd.randint(0, N-1)
        lc[a], lc[b] = lc[b], lc[a]
    return lc
    
def duree(f, L):
    """
        In: f (fonction de tri), L (liste)
        Out: float
    """
    t0 = time.perf_counter()
    f(L)
    t1 = time.perf_counter()
    return t1 - t0

#%% Ex 1

tailles = [(i * 100) for i in range(1, 26)]
tabc = [ listetriee(tailles[i]) for i in range(25) ]
tabdec = [ listeinvers(tailles[i]) for i in range(25) ]
tabalea = [ listealea(0, 2500, tailles[i]) for i in range(25) ]

durc = [ duree(tri_insertion, tabc[i]) for i in range(25) ]
durdec = [ duree(tri_insertion, tabdec[i]) for i in range(25) ]
duralea = [ duree(tri_insertion, tabalea[i]) for i in range(25) ]

tabc = [ listetriee(tailles[i]) for i in range(25) ]
tabdec = [ listeinvers(tailles[i]) for i in range(25) ]
tabalea = [ listealea(0, 2500, tailles[i]) for i in range(25) ]

sdurc = [ duree(tri_selection, tabc[i]) for i in range(25) ]
sdurdec = [ duree(tri_selection, tabdec[i]) for i in range(25) ]
sduralea = [ duree(tri_selection, tabalea[i]) for i in range(25) ]

tabc = [ listetriee(tailles[i]) for i in range(25) ]
tabdec = [ listeinvers(tailles[i]) for i in range(25) ]
tabalea = [ listealea(0, 2500, tailles[i]) for i in range(25) ]

bdurc = [ duree(tri_bulle, tabc[i]) for i in range(25) ]
bdurdec = [ duree(tri_bulle, tabdec[i]) for i in range(25) ]
bduralea = [ duree(tri_bulle, tabalea[i]) for i in range(25) ]
    
plt.plot(tailles, durc, label="Insertion - Croissante", color='b')
plt.plot(tailles, durdec, label="Insertion - Decroissante", color='b', linestyle='-.')
plt.plot(tailles, duralea, label="Insertion - Aleatoire", color='b', linestyle=':')

plt.plot(tailles, sdurc, label="Selection - Croissante", color='r')
plt.plot(tailles, sdurdec, label="Selection - Decroissante", color='r', linestyle='-.')
plt.plot(tailles, sduralea, label="Selection - Aleatoire", color='r', linestyle=':')

plt.plot(tailles, bdurc, label="Bulle - Croissante", color='g')
plt.plot(tailles, bdurdec, label="Bulle - Decroissante", color='g', linestyle='-.')
plt.plot(tailles, bduralea, label="Bulle - Aleatoire", color='g', linestyle=':')
    
plt.legend()
    
#%% Ex 2
    
lk = [(i*50) for i in range(101)]
tablk = [ k_presque_triee(5000, lk[i]) for i in range(101) ]
durk = [ duree(tri_insertion, tablk[i]) for i in range(101) ]

plt.plot(lk, durk)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    