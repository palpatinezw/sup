# -*- coding: utf-8 -*-
"""
TP fichier - PTSI / PCSI2

Extraction et mises en forme de données expérimentales.
Diagramme de Bode d'un filtre passe-bande.

"""

import matplotlib.pyplot as plt
import numpy as np


#Ouverture du fichier Filtre_passe_bande2016.txt
#Instanciation de l'objet Fichier de la classe file

# Question 3 : à ccompléter  



#Question 4 : à commenter

chaine = Fichier.read() 
tableau = chaine.split('\n')
                    
for i  in range(len(tableau)):
    tableau[i] = tableau[i].split('\t')



#Question 4 : à commenter et à compléter (Phase)
nb_ligne = len(tableau)
nb_colonne = len(tableau[0])

f = [tableau[ligne][0] for ligne in range(1,nb_ligne)]            
H = [tableau[ligne][1] for ligne in range(1,nb_ligne)]

f = [float(elem) for elem in f]
H = [elem.replace(',','.') for elem in H]

H = [float(elem) for elem in H]

G = [20*np.log10(elem) for elem in H]



#Questions 6 à 9 - à compléter.




#Fermeture du fichier
# A compléter
