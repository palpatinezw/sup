# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np


#%%
#EX 1 ===================================

y = input("Entrer un nombre reel: ")
x = float(y)
if x > 0:
    # Multiplier les reels positifs par 2
    print(2*x)
elif x < 0:
    # Reels negatifs
    print(8-x)
else:
    # Nul
    print("IL EST NUL")
    
#%%
    
# EX 2 ===================================

mode = input("Entrer C pour conversion Celsuis > Fahrenheit, F pour Fahrenheit > Celsius: ")
celsius = mode == 'C' 
T = int(input("Entrer la temperature: "))

if celsius:
    print(round(((212-32) / 100)*T + 32, 2))
else:
    print(round(((100) / (212-32))*(T-32), 2))
    
#%%

# EX 3 ====================================

mot1 = input("Mot 1: ")
mot2 = input("Mot 2: ")

if len(mot1) == len(mot2): print("Même taille!")
else: print(mot1 if len(mot1) > len(mot2) else mot2)

#%%

# EX 4 ====================================

rayon = 3
aire = np.pi * (rayon**2)
print(f"L'aire du disque de rayon {rayon} vaut {round(aire, 2)} mètres carrés")

#%%

# EX 5 ====================================

pistonls = ["Piston"]*100
separateur = "\n"
print(separateur.join(pistonls))

#%%

# EX 6 ====================================

secondes = s = 1028302806

annees = s // (365*24*60*60)
s %= (365*24*60*60)
jours = s // (24*60*60)
s %= (24*60*60)
minutes = s // 60
s %= 60

print(f"{secondes} s vaut {annees} annees, {jours} jours, {minutes} minutes, {s}, secondes")

#%%

# EX 7 ====================================

A = 1700

print(f"{A} {'est bisextile' if A%400 == 0 or (A%4 == 0 and A%100 != 0) else 'n est pas bisextile'}.")

#%%

# EX 8 ====================================

a, b, c = 3, 3, 3

if (a < 0 or b < 0 or c < 0): print("Les nombres devraient etre positifs!")
elif (a==b and b==c): print("Triangle equilateral")
elif (a==b or a==c or b==c): print("Triangle isocele")

longueursTires = [a, b, c]
longueursTires.sort()
hypotenuse = longueursTires[-1]
l1, l2 = longueursTires[0], longueursTires[1]

if l1**2 + l2**2 == hypotenuse**2: print("Triangle rectangle")
    
#%%

# EX 10 ====================================

note = int(input("Entrer la note obtenue: "))
totale = int(input("Entrer la note maximale: "))
pourcentage = note/totale * 100

print(
    'A' if pourcentage >= 80
    else 'B' if pourcentage >= 60
    else 'C' if pourcentage >= 50
    else 'D' if pourcentage >= 40
    else 'E'
)


#%%

# EX 11 ====================================

x = int(input("a: "))
y = int(input("b: "))
z = 0

while (x != 0):
    if x%2 == 0:
        x //= 2
        y *= 2
    else:
        x -= 1
        z += y
        
print(z)











































