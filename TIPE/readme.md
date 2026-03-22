# Consignes d'utilisation

Lancer l'application d'analyse avec `main.py`. La bande d'extraction de l'image par defaut est mise à `bande = (40, 100)`. Pour adjuster la bande, utiliser `adjusterBande()`

La fonction `calibrer()` doit être obligatoirement appelée à **chaque reinitialisation** avant de faire une analyse. Une analyse simple est effectuée avec la fonction `analyse()` - le resultat est stocké dans `out/resultat_DATE.txt`