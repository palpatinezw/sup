#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 08:18:17 2026

@author: zhuang@pedagogique.local
"""

# Ex 1 ========================================================================

G = [ [1, 3, 4], [0, 2, 4], [1, 3], [0, 2], [0, 1] ]

def largeur(G, depart):
    """
        In: G liste d'adjacence; depart int
        Out: liste 
    """
    q = [depart]
    parcouru = [depart]
    
    while len(q) > 0:
        cur = q.pop(0)
        print(f"Parcours {cur}")
        for x in G[cur]:
            if not x in parcouru:
                q.append(x)
                parcouru.append(x)

    return parcouru

# Ex 3 ========================================================================

nlig = 3
ncol = 4

Laby0L = [
    [1],
    [0, 5],
    [6],
    [7],
    [5, 8],
    [4, 1],
    [2, 7, 10],
    [3, 6, 11],
    [4, 9],
    [8, 10],
    [9, 6],
    [7]
]

Laby0 = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
]

def numero(i, j):
    """
        In: i int; j int
        Out: int
    """
    return j + 4*i
def denum(n):
    """
        In: n int
        Out: [int, int]
    """
    return ((n//ncol), (n%ncol))

def sortir(i, j):
    dep = numero(i, j)
    parcouru = [dep]
    pile = [dep]
    chemin = []
    
    while len(pile) > 0:
        cur = pile[-1]
        if not cur in chemin:
            chemin.append(cur)
        
        if cur == 3:
            return [denum(x) for x in chemin]
        
        trouve = False
        for x in Laby0L[cur]:
            if not x in parcouru:
                trouve = True
                pile.append(x)
                parcouru.append(x)
                break
        if not trouve:
            pile.pop()
            chemin.pop()
    return -1

# Ex 2 ========================================================================

G0L = [ [1, 2, 6, 4, 5], [0, 2], [1, 0, 6, 3], [2, 6, 4], [5, 0, 6, 3], [0, 4], [0, 2, 4, 3] ]
G0 = [
 [0, 1, 1, 0, 1, 1, 1],
 [1, 0, 1, 0, 0, 0, 0],
 [1, 1, 0, 1, 0, 0, 1],
 [0, 0, 1, 0, 1, 0, 1],
 [1, 0, 0, 1, 0, 1, 1],
 [1, 0, 0, 0, 1, 0, 0],
 [1, 0, 1, 1, 1, 0, 0]
]

def degre(G, sommet):
    """
        In: G matrice d'adjacence; sommet int
        Out: int
    """
    c = 0
    for e in G[sommet]:
        c += e
    return c
def lien(G, i):
    """
        In: G matrice d'adjacence; i int
        Out: liste
    """
    L = []
    for j in range(len(G[i])):
        if G[i][j] == 1:
            L.append(j)
    return L

def trier_liste(L):
    for i in range(1, len(L)):
        for j in range(i, 0, -1):
            if L[j] > L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
            else:
                break
    return L

def trier_sommet(G):
    """
        In: G matrice d'adjacence
        Out: liste
    """
    L = []
    for i in range(len(G)):
        L.append(i)
        ds = degre(G, i)
        for j in range(i, 0, -1):
            if ds > degre(G, L[j-1]):
                L[j], L[j-1] = L[j-1], L[j]
            else:
                break
    return L

def colorer(G):
    L = trier_sommet(G)
    couleurs = [-1 for i in range(len(G))]
    
    ncoul = 1
    
    for x in L:
        if couleurs[x] != -1:
            continue
        
        couleurs[x] = ncoul
        vois = []
        vois += lien(G, x)
        
        for nx in L:
            if couleurs[nx] != -1:
                continue
            if nx in vois:
                continue
            couleurs[nx] = ncoul
            vois += lien(G, nx)
            
        ncoul += 1
        
    return [(i, couleurs[i]) for i in range(len(couleurs))]








































