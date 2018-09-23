#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les tuples

Un tuple consiste en différentes valeurs séparées par des virgules.
Les tuples sont immuables (qui ne peuvent pas changer) et contiennent souvent
des séquences hétérogènes d’éléments.

Les tuples vides sont construits par une paire de parenthèses vides;
Un tuple avec un seul élément est construit en faisant suivre la valeur
par une virgule.
"""

t = 888, [123, 234], 'test'     # init d'un tuple de plusieurs élément
empty = ()                      # init d'un tuple vide
singleton = 123,                # init d'un tuple avec un seul élément

print(t)
print(singleton)
print(t[0])
print(type(empty))

# déballage de séquence
x, y, z = t
print(x, y, z)

x, y, z = 12, 3, 2
print(x, y, z)
