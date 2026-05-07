#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 08:25:27 2026

@author: zhuang@pedagogique.local
"""

import numpy as np

def pilevide():
    return []

def estVide(p):
    return len(p)==0

def empile(p, a):
    p.append(a)
    
def depile(p):
    return p.pop()

def deversepile(p1, p2):
    while not estVide(p1):
        empile( p2, depile(p1) )

# =============================================================================

def echangepremierdeuxieme(p):
    e1 = depile(p)
    e2 = depile(p)
    empile(p, e1)
    empile(p, e2)

def echangepremierdernier(p):
    e1 = depile(p)
    ptemp = pilevide()
    deversepile(p, ptemp)
    ed = depile(ptemp)
    empile(ptemp, e1)
    deversepile(ptemp, p)
    empile(p, ed)

def echangek(p, k):
    # el en haut = 1 er element
    if k == 1:
        return
    ptemp = pilevide()
    e1 = depile(p)
    for i in range(k-2):
        empile( ptemp, depile(p) )
    ek = depile(p)
    empile(p, e1)
    deversepile(ptemp, p)
    empile(p, ek)

def separe(p):
    ppos = pilevide()
    pneg = pilevide()
    while not estVide(p):
        e = depile(p)
        if e >= 0:
            empile(ppos, e)
        else:
            empile(pneg, e)
    deversepile(pneg, p)
    deversepile(ppos, p)

# =============================================================================

def parenthesenaif(ch):
    c = 0
    for e in ch:
        if e == '(':
            c += 1
        elif e == ')':
            c -= 1
        if c < 0: return False
    if c != 0:
        return False
    return True

def parenthese(ch):
    p = pilevide()
    for e in ch:
        if e == '(':
            empile(p, '(')
        elif e == '{':
            empile(p, '{')
        elif e == '[':
            empile(p, '[')
        elif e == ')':
            if estVide(p) or depile(p) != '(':
                return False
        elif e == '}':
            if estVide(p) or depile(p) != '{':
                return False
        elif e == ']':
            if estVide(p) or depile(p) != '[':
                return False
    return estVide(p)

# =============================================================================

def sommet(p):
    e = depile(p)
    empile(p, e)
    return e

def taille(p):
    c = 0
    ptemp = pilevide()
    while not estVide(p):
        c += 1
        empile(ptemp, depile(p))
    deversepile(ptemp, p)
    
    return c

def retourne(p, k):
    ptemp = pilevide()
    for i in range(k//2):
        echangek(p, k - 2*i)
        empile(ptemp, depile(p))
    deversepile(ptemp, p)
    
def trouvemax(p, k):
    ptemp = pilevide()
    maxel = depile(p)
    empile(ptemp, maxel)
    maxidx = 1
    for i in range(k-1):
        e = depile(p)
        if e > maxel:
            maxel = e
            maxidx = i+2
        empile(ptemp, e)
    deversepile(ptemp, p)
    return maxidx

def tricrepe(p):
    for k in range(taille(p), 0, -1):
        maxidx = trouvemax(p, k)
        retourne(p, maxidx)
        retourne(p, k)
    return p

# =============================================================================

opbin = ['+', '-', '*', '/']
opuni = ['sin', 'cos', 'ln', 'exp']

def appliquebinaire(op, a, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
def appliqueunaire(op, a):
    if op == 'sin':
        return np.sin(a)
    if op == 'cos':
        return np.cos(a)
    if op == 'ln':
        return np.log(a)
    if op == 'exp':
        return np.exp(a)
    
def evaluation(formule):
    p = pilevide()
    for e in formule:
        if type(e) == str:
            if e in opbin:
                a = depile(p)
                b = depile(p)
                empile(p, appliquebinaire(e, a, b))
            if e in opuni:
                a = depile(p)
                empile(p, appliqueunaire(e, a))
        else:
            empile(p, e)
    return depile(p)

# =============================================================================

def insertion(p, a):
    ptemp = pilevide()
    while not estVide(p):
        e = depile(p)
        if e <= a:
            empile(p, e)
            empile(p, a)
            deversepile(ptemp, p)
            return
        else:
            empile(ptemp, e)

    if estVide(p):
        empile(p, a)
        deversepile(ptemp, p)

def tri(p):
    ptemp = pilevide()
    deversepile(p, ptemp)
    while not estVide(ptemp):
        insertion(p, depile(ptemp))
    return p

# =============================================================================

f = [1, 2, 'exp', '+', 3, '*', 'ln']

p = [4, 1, 7, 3, 9, 0]
    
p0 = pilevide()
empile(p0, 6)
empile(p0, 'coucou')
empile(p0, [2, 5])
empile(p0, True)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
