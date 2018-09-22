#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les fonctions anonymes

Démonstration d'une fonction anonyme
"""

def make_incrementor(n):
    """Fonction d'incrémentation.

    Retourne une fonction qui incrémente n.
    """
    return lambda x: x + n



i = make_incrementor(100)
print(make_incrementor.__doc__) # affiche la doc de la fonction
print(i)                        # <function make_incrementor.<locals>.<lambda> at 0x1063e87b8>
print(i(10))                    # affiche 110
