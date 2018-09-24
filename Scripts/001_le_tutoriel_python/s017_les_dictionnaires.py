#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les dictionnaires

Parfois aussi appelé "Tableaux associatifs",
les dictionnaires sont indexés par des clés
de type immuables : nombre, chaînes, tuples.

Les dictionnaires sont comme des ensembles de paires clé: valeur,
les clés devant être uniques.
"""

# initialisation et ajout
tel = {'bobby': 3086, 'jerome': 3089}
tel['standard'] = 3099
print(tel)

# initialisation avec les paramètres nommés
tel = dict(bobby=3086, jerome=3089)
print(tel)

# suppresion
del tel['jerome']

# récupère la liste des clés d'un dictionnaire
keys = list(tel)
print(keys)

# vérification de l'existence d'un élément
print('standard' in tel)

# initialisation par compréhension
squares = {x: x**2 for x in range(10)}
print(squares)
