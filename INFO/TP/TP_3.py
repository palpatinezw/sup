# -*- coding: utf-8 -*-
"""
TP 3 0A 1A 1A
"""

n = input("Nombre a convertir: ")
k = int(input("Base a convertir: "))
r = int(n)
resultat = ''

assert(k <= 10)

while r != 0:
    resultat = str(r%k)+resultat # ajouter nouveau chiffre au debut
    
    r //= k
    
print("Resultat:", n, "en base", k, "est", resultat) 