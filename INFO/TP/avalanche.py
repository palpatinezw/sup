#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 08:19:26 2025

@author: zhuang@pedagogique.local
"""

import random
import matplotlib.pyplot as plt

mont0 = [6,6,5,2,1]

def il_neige(montagne, position):
    """
        In: montagne (Ls des entiers), position (enter indice de neige)
        Out: None
    """
    montagne[position] += 1
    
def est_instable(montagne):
    """
        In: montagne (Ls entiers)
        Out: None
    """
    for i in range(1, len(montagne)):
        if abs(montagne[i] - montagne[i-1]) > 2:
            return True
        
    if montagne[-1] > 2: 
        return True
    
    return False
    
def relaxation(montagne):
    """
        In: montagne (Ls entiers)
        Out: Entier
    """
    if montagne[0] - montagne[1] > 2: 
        montagne[0] -= 2
        montagne[1] += 2
        return 0
    
    for i in range(1, len(montagne)-1):
        if montagne[i] - montagne[i+1] > 2:
            montagne[i] -= 2
            montagne[i+1] += 2
            return 0
        elif montagne[i] - montagne[i-1] > 2:
            montagne[i] -= 2
            montagne[i-1] += 2
            return 0
    
    if montagne[-1] > 2:
        montagne[-1] -= 2
        return 2
    elif montagne[-1] - montagne[-2] > 2:
        montagne[-1] -= 2
        montagne[-2] += 2
        return 0
    
    return 0
        
def relaxation_totale(montagne):
    """
        In: montagne (Ls entiers)
        Out: entier
    """
    rav = 0
    
    while est_instable(montagne):
        rav += relaxation(montagne)
        
    return rav
        
def simulation(N, l, neigetype = 0, nbneige = 1):
    """
        In: N entier nombre de simulations, l largeur de montagne, neigetype entier
        Out: None
    """
    mont = [random.randint(0, 10) for k in range(l)]
    aval = []
    
    def neigeur_rand():
        il_neige(mont, random.randint(0, l-1))

    def neigeur_gauche():
        il_neige(mont, 0)
    
    for i in range(N):
        for j in range(nbneige):
            if neigetype == 0:
                neigeur_rand()
            elif neigetype == 1:
                neigeur_gauche()
        aval.append(relaxation_totale(mont))
        
    plt.hist(aval)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        