#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les ensembles

Un ensemble est une collection non ordonnée sans élément dupliqué.
Utile notamment pour la suppression de doublons.
Les ensembles peuvent aussi gérer des opérations telle que :
l'union, l'intersection, la différence et la différence symétrique (XOR)
"""

# initialisation
fruits = {"banana", "orange", "apple", "orange"}
print(fruits)

# Vérification de l'existance d'un élément
print("banana" in fruits)

# initilisation avec le mot clé 'set'
a = set("bonjour")          #      A                      B
b = set("journée")          # |          |  o   n   |          |
                            # |    b     |    u     |   é  e   |
                            # |          |  j   r   |          |

# lettre dans a mais pas dans b : DIFFÉRENCE
print(a - b)      # {'b'}

# lettre dans a OU dans b : UNION
print(a | b)      # {'b', 'e', 'o', 'n', 'é', 'u', 'r', 'j'}

# lettre dans a ET dans b : INTERSECTION
print(a & b)      # {'r', 'j', 'u', 'o', 'n'}

# lettre dans a OU dans b MAIS PAS les 2 : XOR
print(a ^ b)      # {'e', 'é', 'b'}

# XOR équivaut aussi à UNION - INTERSECTION
print((a | b) - (a & b))    # {'e', 'é', 'b'}
