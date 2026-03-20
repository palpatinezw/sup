#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:03:57 2026

@author: zhuang@pedagogique.local
"""

import numpy as np
import matplotlib.pyplot as plt

def puissanceI(x, n):
    res = 1
    for i in range(n):
        res *= x
    return res

def puissanceR(x, n):
    if n == 0:
        return 1
    else:
        return x*puissanceR(x, n-1)

def puissanceRapide(x, n):
    if n == 0:
        return 1
    
    if n % 2 == 0:
        return puissanceRapide(x*x, n//2)
    else:
        return x*puissanceRapide(x*x, n//2)

# =============================================================================

def mystere(ch):
    if ch=="":
        return ""
    else:
        return ch[-1] + mystere(ch[:-1])

def palindrome(s):
    """
        In: s str
        Out: Bool
    """
    if s == '':
        return True
    if s[0] != s[-1]: 
        return False
    else:
        return palindrome(s[1:-1])

def somme_liste(ls):
    """
        In: ls liste de float
        Out: float
    """
    if len(ls) == 0:
        return 0
    
    return ls[-1] + somme_liste(ls[:-1])

# =============================================================================

def syr_rec(n, a):
    """
        In: n entier; a entier
        Out: entier
    """
    if n == 0:
        return a
    
    un = syr_rec(n-1, a)
    if un % 2 == 0:
        return un // 2
    else:
        return 3*un + 1

# plt.plot([k for k in range(120)], [syr_rec(k, 27) for k in range(120)], "-o")

# =============================================================================


def circle(c, r):
    """
        In: c liste de 2 float; r float
        Out: None
    """
    # print(f"Trace [ {c[0]}, {c[1]} ] rayon {r}")
    theta = np.linspace(0, 2*np.pi, 100)
    xl = c[0] + r * np.cos(theta)
    yl = c[1] + r * np.sin(theta)
    
    plt.plot(xl, yl)
    plt.axis("equal")

def fig1(c, r):
    """
        In: c liste de 2 float; r float
        Out: None
    """
    
    if r < 1:
        return
    
    circle(c, r)
    fig1([c[0]+r + r/2, c[1]], r/2)
    fig1([c[0], c[1]-r - r/2], r/2)

def fig2(c, r, prev = -1):
    """
        In: c liste de 2 float; r float; prev entier (entre -1 et 3)
        Out: None
    """
    
    if r < 0.5:
        return
    
    circle(c, r)
    if prev != 1: fig2([c[0]+r + r/2, c[1]], r/2, 0) # 0 droit
    if prev != 0: fig2([c[0]-r - r/2, c[1]], r/2, 1) # 1 gauche 
    if prev != 3: fig2([c[0], c[1]-r - r/2], r/2, 2) # 2 bas
    if prev != 2: fig2([c[0], c[1]+r + r/2], r/2, 3) # 3 haut




























