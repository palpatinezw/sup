#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:04:01 2026

@author: zhuang@pedagogique.local
"""

import time
import random as rd
import matplotlib.pyplot as plt

def fusion(L1, L2):
    """
        In: L1, L2 (listes)
        Out: liste
    """
    i = 0
    j = 0
    L = []
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L.append(L1[i])
            i+=1
        else:
            L.append(L2[j])
            j+=1
            
    if i < len(L1):
        L += L1[i:]
    if j < len(L2):
        L += L2[j:]
        
    return L

def tri_fusion(L):
    """
        In: L liste de nombres
        Out: liste L triee
    """
    n = len(L)
    if n == 1:
        return L
    L1 = L[:(n//2)]
    L2 = L[(n//2):]
    
    return fusion(tri_fusion(L1), tri_fusion(L2))


def tri_rapide(L):
    """
        In: L liste de nombres
        Out: liste L triee
    """
    n = len(L)
    
    if n <= 1:
        return L
    
    L1 = []
    L2 = []
    pivot = L[0]
    
    for i in range(1, n):
        if L[i] < pivot:
            L1.append(L[i])
        else:
            L2.append(L[i])
    
    return tri_rapide(L1) + [pivot] + tri_rapide(L2)

def tri_selection(L):
    """
        In: L liste de nombres
        Out: liste L triee
    """
    for i in range(0, len(L)):
        minidx = i
        for j in range(i, len(L)):
            if L[j] < L[minidx]:
                minidx = j
        L[i], L[minidx] = L[minidx], L[i]
    return L

def tri_insertion(L):
    """
        In: L liste de nombres
        Out: liste L triee
    """
    for i in range(1, len(L)):
        j = i
        while j > 0 and L[j-1] > L [j]:
            L[j], L[j-1] = L[j-1], L[j]
            j -= 1
            
    return L
        
def chrono(f, Ls):
    """
        In: f fonction de tri; Ls liste de nombres
        Out: temps de tri
    """
    t1 = time.perf_counter()
    f(Ls)
    t2 = time.perf_counter()
    return t2 - t1

def listealea(a, b, N):
    """
        In: a entier; b entier; N entier
        Out: liste de N entiers entre a et b
    """
    return [rd.randint(a, b) for i in range(N)]

def listeinvers(N):
    """
        In: N entier
        Out: liste de [N, ... , 1]
    """
    return [i for i in range(N, 0, -1)]

def listetriee(N):
    """
        In: N entier
        Out: liste de [1, ... , N]
    """
    return [i for i in range(1, N+1)]

# =============================================================================

xliste = [i * 100 for i in range(1, 26)]

tabc = [listetriee(i) for i in xliste]
tabdec = [listeinvers(i) for i in xliste]
tabalea = [listealea(0, 2500, i) for i in xliste]

plt.plot(xliste, [chrono(tri_fusion, ls) for ls in tabc], label="Tri fusion (triee)", color='b', linestyle='--')
plt.plot(xliste, [chrono(tri_fusion, ls) for ls in tabdec], label="Tri fusion (invers)", color='b', linestyle='-.')
plt.plot(xliste, [chrono(tri_fusion, ls) for ls in tabalea], label="Tri fusion (aleatoire)", color='b')

tabc = [listetriee(i) for i in xliste]
tabdec = [listeinvers(i) for i in xliste]
tabalea = [listealea(0, 2500, i) for i in xliste]

plt.plot(xliste, [chrono(tri_rapide, ls) for ls in tabc], label="Tri rapide (triee)", color='r', linestyle='--')
plt.plot(xliste, [chrono(tri_rapide, ls) for ls in tabdec], label="Tri rapide (invers)", color='r', linestyle='-.')
plt.plot(xliste, [chrono(tri_rapide, ls) for ls in tabalea], label="Tri rapide (aleatoire)", color='r')

tabc = [listetriee(i) for i in xliste]
tabdec = [listeinvers(i) for i in xliste]
tabalea = [listealea(0, 2500, i) for i in xliste]

plt.plot(xliste, [chrono(tri_selection, ls) for ls in tabc], label="Tri selection (triee)", color='g', linestyle='--')
plt.plot(xliste, [chrono(tri_selection, ls) for ls in tabdec], label="Tri selection (invers)", color='g', linestyle='-.')
plt.plot(xliste, [chrono(tri_selection, ls) for ls in tabalea], label="Tri selection (aleatoire)", color='g')

tabc = [listetriee(i) for i in xliste]
tabdec = [listeinvers(i) for i in xliste]
tabalea = [listealea(0, 2500, i) for i in xliste]

plt.plot(xliste, [chrono(tri_insertion, ls) for ls in tabc], label="Tri insertion (triee)", color='y', linestyle='--')
plt.plot(xliste, [chrono(tri_insertion, ls) for ls in tabdec], label="Tri insertion (invers)", color='y', linestyle='-.')
plt.plot(xliste, [chrono(tri_insertion, ls) for ls in tabalea], label="Tri insertion (aleatoire)", color='y')

plt.legend()
plt.show()




























