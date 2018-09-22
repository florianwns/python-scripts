#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Initialisation de listes

Il existe plusieurs façon de initialisater des listes
"""

# on peut créer un liste f(x) = x^2 de plusieurs manières
# en utilisant la méthode append
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# avec lambda
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# ou plus lisible
squares = [x**2 for x in range(10)]
print(squares)


# On peut imbriquer des boucles
tuples = [(x, y) for x in [1, 3, 5] for y in [3, 4, 5] if x != y]
print(tuples)
