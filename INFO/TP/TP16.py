# -*- coding: utf-8 -*-
"""
Fonctions cours
"""
import time
import random
import numpy as np
import matplotlib.pyplot as plt


def rse(ls, x):
    """
        In: ls liste d entiers, x entier
        Out: entier compteur
    """
    c = 0
    for e in ls:
        c += 1
        if e == x: return c
    return c

def rde(ls, x):
    """
        In: ls liste d entiers, x entier
        Out: entier compteur
    """
    c = 0
    imin = 0
    imax = len(ls) - 1
    while (imin <= imax):
        c += 1
        imil = imin + imax
        imil //= 2
        e = ls[imil]
        if e == x: return c
        elif e < x: imin = imil+1
        else: imax = imil - 1
    return c        

ls = [random.randint(-10000000, 10000000) for k in range(100)] 
ls.sort()

def tpsRech(f, ls, N, x = None):
    res = []
    for i in range(N):
        t1 = time.perf_counter()

        f(ls, random.randint(-10000000, 10000000) if x == 0 else x)
        # print(res)

        t2 = time.perf_counter()
        T = t2-t1
        res.append(T)

    return np.average(res)

# print("Temps: ", tpsRech(rde, ls, 100, ls[-1]))

l = [k for k in range(1, 10**4)]
H = [ np.average([rde(l[0:k], random.randint(1, k)) for kk in range(1)]) for k in l ]
# Hmeill = [ np.average([rde(l[0:k], k//2) for kk in range(1)]) for k in l ]
Hm = [ np.average([rde(l[0:k], random.randint(1, k)) for kk in range(100)]) for k in l ]
# Recherche d une variable qui existe dans l intervalle
D = [ rde(l[0:k], k) for k in l ]
# Recherche du dernier element (pire des cas)


plt.xlabel('Nombre d elements')
plt.ylabel('Nombre d operations')
plt.plot(l, H, label='Recherche elem quelconque')
plt.plot(l, Hm, label='Recherche elem quelconque moyenne')
plt.plot(l, D, label='Recherche elem dernier')
plt.plot(l, np.log2(l)+1, label='log2')
plt.legend()
plt.show()


























