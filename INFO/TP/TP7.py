#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 14:06:43 2025

@author: zhuang@pedagogique.local
"""

# Ex 1
def lmax(ls):
    """
        In: liste des nombres
        Out: un nombre
        Renvoie le plus grand element
    """
    cmax = ls[0]
    for e in ls:
        if e > cmax: 
            cmax = e
    return cmax

def lmoyenne(ls):
    """
        In: liste des nombres
        Out: un nombre
        Renvoie la moyenne
    """
    somme = 0
    for e in ls:
        somme += e
    return somme / len(ls)

def lmult5(ls):
    """
        In: liste des nombres
        Out: un nombre
        Renvoie le nb d elements multiples de 5
    """
    nb = 0
    for e in ls:
        if e%5 == 0:
            nb += 1
    return nb

def infmoyenne(ls):
    """
        In: liste des nombres
        Out: liste des nombres
        Renvoie la liste d elements strictement inferieur a la moyenne
    """
    moy = lmoyenne(ls)
    r = []
    for e in ls:
        if e < moy:
            r.append(e)
    return r
    
def paire(ls):
    """
        In: liste des nombres
        Out: couple avec 2 listes des nombres
        1ere liste avec nb paires, 2nde avec nb impaires
    """
    li = []
    lp = []
    
    for e in ls:
        if e%2 == 0:
            lp.append(e)
        else:
            li.append(e)
            
    return (lp, li)
    
def diff(ls):
    """
        In: liste des nombres
        Out: un nombre
        diff entre elements pairs au carre et impaires au carre
    """
    lpi = paire(ls)
    sp = 0
    si = 0
    for e in lpi[0]:
        sp += e**2
    
    for e in lpi[1]:
        si += e**2
        
    return sp - si

def ineg(ls):
    """
        In: liste des nombres
        Out: liste d entiers positifs
        liste des indices des elements negatifs
    """
    r = []
    for i in range(len(ls)):
        if ls[i] <= 0:
            r.append(i)
    return r
    
def imax(ls):
    """
        In: liste des nombres
        Out: liste d entiers positifs
        liste des indices des plus grands elements 
    """
    r = []
    emax = lmax(ls)
    for i in range(len(ls)):
        if ls[i] == emax:
            r.append(i)
    return r

def estOrd(ls):
    """
        In: liste des nombres
        Out: bouleen
        True si ordonnee, False sinon 
    """
    mindiff = 0
    maxdiff = 0
    for i in range(1, len(ls)):
        diff = ls[i] - ls[i-1]
        if diff < mindiff:
            mindiff = diff
        if diff > maxdiff:
            maxdiff = diff
    
    return not(maxdiff > 0 and mindiff < 0)
    

# Ex 2
def mindist(ls):
    """
        In: liste des nombres avec au moins 2 elements
        Out: un nombre
        La plus petite distance entre 2 elements
    """
    
    mndist = abs(ls[1] - ls[0])
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            dist = abs(ls[i] - ls[j])
            if dist < mndist:
                mndist = dist
                
    return mndist

# Ex 3
def prod_scalaire(v1, v2):
    """
        In: v1, v2 vecteurs (couple a 3 nbs)
        Out: un nombre
        Renvoie le prod scalaire
    """
    
    res = 0
    for i in range(3):
        res += v1[i]*v2[i]
    return res

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    