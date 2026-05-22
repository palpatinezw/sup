#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:05:57 2026

@author: zhuang@pedagogique.local
"""

Ma1 = [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]       
]
Da1 = {
    0: [2, 3],
    1: [3],
    2: [0],
    3: [0, 1]       
}
La1 = [
    [2, 3],
    [3],
    [0],
    [0, 1]      
]

def testM(Ma, i, j):
    """
        In: Ma matrice d'adjacence; i int; j int
        Out: Bool
    """
    return Ma[i][j] == 1

def testD(Da, i, j):
    """
        In: Da dictionnaire d'adjacence; i int; j int
        Out: Bool
    """
    return j in Da[i]

def testL(La, i, j):
    """
        In: La liste d'adjacence; i int; j int
        Out: Bool
    """
    return j in La[i]

def LtoM(La):
    """
        In: La liste d'adjacence
        Out: matrice d'adjacence
    """
    Ma = []
    for i in range(len(La)):
        Ma.append([1 if j in La[i] else 0 for j in range(len(La))])
    return Ma

def DtoM(Da):
    """
        In: Da dictionnaire d'adjacence
        Out: matrice d'adjacence
    """
    Ma = []
    for i in range(len(Da)):
        Ma.append([1 if j in Da[i] else 0 for j in range(len(Da))])
    return Ma
        
# Ex 2 ========================================================================

Ma2 = [
    [-1, 1, -1, 2, 4],
    [1, -1, 9, -1, 8],
    [-1, 9, -1, 7, -1],
    [2, -1, 7, -1, -1],
    [4, 8, -1, -1, -1]
]

def test_chaine(M, L):
    """
        In: M matrice d'adjacence; L liste de sommets
        Out: Bool
    """
    for i in range(1, len(L)):
        if M[L[i-1]][L[i]] == -1: 
            return False
    return True

def longueur(M, L):
    """
        In: M matrice d'adjacence; L liste de sommets
        Out: Bool
    """
    l = 0
    for i in range(1, len(L)):
        if M[L[i-1]][L[i]] == -1: 
            return -1
        l += M[L[i-1]][L[i]]
    return l

# Ex 3 ========================================================================

def profondeur(G, depart):
    """
        In: G matrice d'adjacence; depart int
        Out: Liste (int)
    """
    parcouru = []
    pile = [depart]
    
    while len(pile) > 0:
        cur = pile.pop()
        if cur in parcouru:
            continue
        parcouru.append(cur)
        
        print(f"[-] Parcours ({cur}) avec {pile}")
        
        for i in range(len(G[cur])):
            if G[cur][i] > 0 and not i in parcouru:
                pile.append(i)
    return parcouru
        
def profondeurRec(G, depart, parcouru = []):
    """
        In: G matrice d'adjacence; depart int; parcouru liste
        Out: liste
    """
    if depart in parcouru:
        return []
    parcouru.append(depart)
    print(f"[-] Parcours ({depart})")
    
    for i in range(len(G[depart])):
        if G[depart][i] > 0 and not i in parcouru:
            profondeurRec(G, i, parcouru)
    return parcouru








































