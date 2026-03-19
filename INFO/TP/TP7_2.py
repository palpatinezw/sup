#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 08:57:07 2025

@author: zhuang@pedagogique.local
"""

import random

# Ex 1 ========================================================================

m1 = []

for i in range(5):
    m1.append([])
    for j in range(5):
        m1[i].append(i+1)        
        
def sommeMat(m):
    """
        In: matrice liste de listes
        Out: float
    """
    somme = 0
    for ligne in m:
        for e in ligne:
            somme += e
    return somme

def traceMat(m):
    """
        In: matrice carree liste de listes
        Out: float
    """
    trace = 0
    for i in range(len(m)):
        trace += m[i][i]
        
    return trace

def sommeLigneCol(m):
    """
        In: matrice liste de listes
        Out: liste : [ liste sommes des lignes , liste sommes des colonnes ]
    """
    sommelignes = []
    sommecolonnes =  [0 for i in range(len(m[0]))]
    for ligne in m:
        sommeligne = 0
        for i in range(len(ligne)):
            sommeligne += ligne[i]
            sommecolonnes[i] += ligne[i]
            
        sommelignes.append(sommeligne)
    return [sommelignes, sommecolonnes]

def estImpair(m):
    """
        In: matrice liste de listes
        Out: matrice meme taille que l entree de 0 ou 1
    """
    res = []
    for ligne in m:
        res.append([])
        for e in ligne:
            res[-1].append( e%2 )
    return res
    
    
# Ex 2 ========================================================================
    
ls1 = [random.randint(-100, 100) for i in range(20)]
    
def recherche(ls, a):
    """
        In: ls - liste des entiers, a - un entier
        Out: Bool
    """
    lss = sorted(ls)
    
    imin = 0
    imax = len(lss) - 1
    while(imin <= imax):
        imil = (imin+imax)//2
        if lss[imil] < a:
            imin = imil + 1
        elif lss[imil] > a:
            imax = imil - 1
        else:
            return True
    return False
    
# Ex 3 ========================================================================

def anagramme(s):
    """
        In: str 
        Out: str
    """
    N = len(s)
    res = ""
    sls = s
    
    for i in range(N):
        curpos = random.randint(0, N-i-1)
        res += sls[curpos]
        
        sls = sls[0:curpos] + sls[curpos+1:]
    return res
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    