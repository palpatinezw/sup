#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 08:17:06 2026

@author: zhuang@pedagogique.local
"""

import numpy as np
import time
import matplotlib.pyplot as plt

# Ex 1 ========================================================================

def Symrnep(n):
    """
        In: n entier
        Out: entier
    """
    if n == 0:
        return 1
    return Symrnep(n-1) + 2*Symrneq(n-1)


def Symrneq(n):
    """
        In: n entier
        Out: entier
    """
    if n == 0:
        return 1
    return Symrnep(n-1) + Symrneq(n-1) 

def vitesseConverge(precision):
    """
        In: precision float
        Out: entier
    """
    n = 0
    while abs((Symrnep(n)/Symrneq(n)) - (2**(0.5))) > precision:
        n += 1
    return n

# Ex 2 ========================================================================

def dichr(n, ls):
    """
        In: n entier; ls liste d entiers
        Out: Bool
    """
    if len(ls) == 1:
        return ls[0] == n
    
    mil = ls[len(ls)//2]
    if mil == n: 
        return True
    elif n < mil:
        return dichr(n, ls[:len(ls)//2])
    else:
        return dichr(n, ls[len(ls)//2+1:])

def testdich():
    ls = [1, 3, 5, 9, 21, 44, 124]
    for e in ls:
        if not dichr2(e, ls):
            return False
        
    return not dichr2(14, ls)

def dichr2(n, ls, *args):
    """
        In: n entier; ls liste d entiers; args* 2 entiers indices cherchees
        Out: Bool
    """
    
    imin = 0
    imax = len(ls)
    if len(args) > 0:
        imin = args[0]
        imax = args[1]
        
    if imin == imax:
        return ls[imin] == n
        
    imil = (imin + imax)//2
    if ls[imil] == n:
        return True
    elif ls[imil] < n:
        return dichr2(n, ls, imil+1, imax)
    else:
        return dichr2(n, ls, imin, imil-1)
    
# Ex 3 ========================================================================

def fiboIt(n):
    """
        In: n entier
        Out: entier
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    fibm2 = 0
    fibm1 = 1
    fib = 1
    
    for i in range(2, n+1):
        fib = fibm1 + fibm2
        fibm2 = fibm1
        fibm1 = fib
    
    return fib

def fiboR(n):
    """
        In: n entier
        Out: entier
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fiboR(n-1) + fiboR(n-2)

def fiboM(n, lsF = []):
    """
        In: n entier; lsF liste entiers
        Out: entier
    """
    # print(f"dbug {n}")
    if n == 0:
        return 0
    if n == 1:
        return 1
    if len(lsF) == 0:
        # print(f"init {n}")
        lsF = [-1 for i in range(n+1)]
        lsF[0] = 0
        lsF[1] = 1
    if lsF[n] > 0:
        return lsF[n]

    lsF[n] = fiboM(n-2, lsF) + fiboM(n-1, lsF)
    return lsF[n]

def puissanceMtxRapide(A, n):
    """
        In: A matrice carre, n entier
        Out: matrice carre
    """
    if n == 0:
        return np.identity(A.shape[0])
    
    if n % 2 == 0:
        return puissanceMtxRapide(np.dot(A, A), n//2)
    else:
        return np.dot(A, puissanceMtxRapide(np.dot(A, A), n//2) )

def fiboMtx(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return np.dot(puissanceMtxRapide(np.array([[1, 1], [1, 0]]), n-1) , np.array([ [1], [0] ]))[0]
     
def testF(f, n):
    t1 = time.perf_counter()
    f(n)
    return time.perf_counter() - t1

# Ex 4 ========================================================================

def polygon(a, b, c):
    """
        In: a b c (coordonnees)
        Out: None. Trace un triangle
    """
    X = [a[0], b[0], c[0]]
    Y = [a[1], b[1], c[1]]
    plt.fill(X, Y, 'b')
    
def calcsommet(a, b):
    l = b[0] - a[0]
    return [a[0] + l/2, a[1] + l*np.sin(np.pi / 3)]

def sierpinski(n, a, b):
    """
        In: n entier; a, b coordonnes de base
        Out: None
    """
    
    l = b[0] - a[0]
    c = calcsommet(a, b)
    if n == 0:
        polygon(a, b, c)
        return
    
    w = [a[0] + l/2, a[1]]
    v = calcsommet(a, w)
    u = calcsommet(w, b)
    
    sierpinski(n-1, a, w)
    sierpinski(n-1, w, b)
    sierpinski(n-1, v, u)
    
    plt.axis("equal")
    
    
    
        








































