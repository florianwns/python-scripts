#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les chaînes de caractères

Quelques exemples de manipulations des chaines
"""

print('c:\some\name')       # ici le \n va nous faire sauter une ligne
print(r'c:\some\name')      # the r evite cela en nous évitant de doubler les \ 

# le \ evite le retour à la ligne, Attention : il ne faut aucune espace après le \
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print(3 * "#" + " Salut toi !")    # Répétition d'une chaîne avec * et concaténation avec le +

# Plusieurs chaines côte côte sont automatiquement concaténé 
# (ne marche pas avec les variables ex : text * 3)
print("°" "-" ")" * 3)              # remarqué que la priorité est différente du +

# les parenthèses permettent de coupeur des chaines sans avoir à sauter de lignes
text = ("Hey qui va là ! "
        "On s'est pas déjà vu quelque part ?")

print(text)

# On peut travailler avec les index
word = "Python"
# en partant de la gauche i >= 0
print(word[0])
# ou en partant de la droit i < 0
print(word[-1])

# On peut écrire des sous chaines
print(word[1:4])        # for(i = 1; i < 4; i++)
print(word[:4])         # for(i = 0; i < 4; i++)                
print(word[4:])         # for(i = 4; i < len(word); i++)
print(word[-2:])        # for(i = len(word) - 2; i < len(word); i++)

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
# 6  -5  -4  -3  -2  -1

# l'affectation avec l'opérateur [] est impossible
# il faut créer une nouvelle chaine
# >>> word[0] = 'p'        
# renverra une erreur

# Longueur d'une chaine
print(len(word))
