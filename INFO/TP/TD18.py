#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:01:56 2026

@author: zhuang@pedagogique.local
"""

def tri_selection(L):
    """
        In: L (liste)
        Out: None; liste L modifie
    """
    for i in range(len(L), 0, -1):
        maxidx = 0
        for j in range(i):
            if L[j] > L[maxidx]:
                maxidx = j
        L[i-1], L[maxidx] = L[maxidx], L[i-1]

def tri_selection_recursif(L, k = -1):
    """
        In: L (liste), k (int)
        Out: None; liste L modifie
        La sous-liste L[:k] triee
    """
    if k == -1:
        k = len(L)
    if k == 0:
        return
        
    maxidx = 0
    for j in range(k):
        if L[j] > L[maxidx]:
            maxidx = j
    L[k-1], L[maxidx] = L[maxidx], L[k-1]
    
    tri_selection_recursif(L, k-1)
    
def tri_comptage(L):
    """
        In: L (liste - elements compris entre 0 et p un entier naturel)
        Out: liste triee
    """
    mx = 0
    for e in L:
        if e > mx:
            mx = e
    H = [0 for i in range(mx+1)]
    
    for i in range(len(L)):
        H[ L[i] ] += 1
    
    res = []
    
    for i in range(len(H)):
        for j in range(H[i]):
            res.append(i)
    return res
    
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

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    