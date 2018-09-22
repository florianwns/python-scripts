#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Supprimer les doublons d'une liste

Montre comment rendre supprimer les doublons d'une liste
Travailler en priorité avec les sets,
si vos données sont censés être uniques

Pas mal d'exemple sur :
https://www.peterbe.com/plog/fastest-way-to-uniquify-a-list-in-python-3.6
"""

# On itnitialise une liste avec des doublons
fruits = ["orange", "banana", "apple", "kiwi", "orange"]
print("{0} : {1}".format("orange", fruits.count("orange")))


print(fruits)                       # La liste à l'origine
print(list(set(fruits)))            # => ne garde pas l'ordre des éléments
print(list(dict.fromkeys(fruits)))  # => garde l'ordre des éléments
