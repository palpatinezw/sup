#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 10:06:47 2025

@author: zhuang@pedagogique.local
"""

llambda = [543, 545.3, 547.6, 542.7, 545.1, 545.4, 541.2, 546.8, 544.4, 545.4]

def moy(l):
    """
        In : liste float
        Out : float
    """

    somme = 0
    for e in l:
        somme += e
    return somme / len(l)

def incerttype(l):
    lexp = moy(llambda)
    N = len(l)
    
    somme = 0
    for e in l:
        somme += (e - lexp)**2

    return (somme/(N*(N-1)))**(0.5)
