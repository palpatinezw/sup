# -*- coding: utf-8 -*-
"""
Fonctions cours
"""

import numpy as np
import matplotlib.pyplot as plt

# Application 1
def parallelepipede(x1, x2, x3):
    """
    IN: x1, x2, x3 entiers
    OUT: entier
    Renvoie le volume duu parallelepipede de dimension x1, x2, x3
    """
    
    return x1*x2*x3

# Application 2
def sinc(x):
    """
    IN: x flottant
    OUT: un flottant
    Renvoie sin(x)/x
    Necessite la bibliotheque numpy (prefixe np)
    """
    return (1 if x == 0 else np.sin(x) / x)

# Application 3
def factoriel(n):
    """
    IN: n entier naturel
    OUT: nfact entier
    Revoie n!
    """
    nfact = 1 
    for i in range(1, n+1):
        nfact *= i
        
    return nfact

# Application 4
def suite(n):
    """
    IN: n entier naturel
    OUT: un flottant
    Renvoie u_n dans la suite
    """
    ux = 2
    for i in range(n):
        ux = 0.5*(ux + 2/ux)
    
    return ux

# Application 5
def minmax(l):
    """
    IN: l liste des entiers
    OUT: liste
    Revoie [min(l), max(l)] si l contient au moins 1 element
    """
    if len(l) < 1:
        return l
    emin = emax = l[0]
    
    for e in l:
        if e < emin:
            emin = e
        if e > emax:
            emax = e
            
    return [emin, emax]

# Ex 1
def max2(x, y):
    """
    IN: 2 flottants
    OUT: un flottant
    Revoie le plus grand
    """
    return x if x > y else y

# Ex 2
def racine(a, b, c):
    """
    IN: 3 flottants a,b,c
    OUT: liste de flottants
    Renvoie les racines de l'equation ax^2 + bx + c
    """
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return [None, None]
    else:
        r1 = (-b + discriminant**(0.5) )/(2*a)
        r2 = (-b - discriminant**(0.5) )/(2*a)
        return [r1, r2]

# Ex 3
def nbmots(phrase):
    """
    IN: str
    OUT: int
    Renvoie le nombre des mots
    """
    nb = 0
    for char in phrase:
        if char == ' ':
            nb += 1
    return nb + 1

# Ex 4
def estUnChiffre(char):
    """
    IN: un caractere (en str)
    OUT: bool 
    Renvoie si le caractere est un chiffre
    """
    return char in "1234567890"

def nombreChiffres(phrase):
    """
    IN: phrase (str)
    OUT: liste 
    Renvoie [nombre de chiffres, nombre de lettres]
    """
    nbchiff = nblettres = 0
    for char in phrase:
        if estUnChiffre(char):
            nbchiff += 1
        else:
            nblettres += 1
            
    return [nbchiff, nblettres]
    
# Ex 5
def palindrome(mot):
    """
    IN: mot (str)
    OUT: bool 
    Renvoie si mot est un palindrome
    """
    n = len(mot)
    for i in range(n//2):
        if mot[i] != mot[n-1-i]:
            return False
        
    return True
            
# Ex 6 - PLT ne marche pas
def hydro(n, Z=1):
    """
    IN: n (int), Z (int, =1 par defaut)
    OUT: float
    """
    return -13.6*((Z**2)/(n**2))

h = 6.63e-34
c = 3e8
e = 1.6e-19
for i in range(1, 21):
    E = hydro(i)
    longueur = (h*c)/(E*e)
    plt.bar(longueur / 10e-9, 1, width=0.1)
    
plt.show()




































