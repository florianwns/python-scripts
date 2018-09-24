#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Comparaison de séquences

Il est possible de comparer les séquences
"""

print((1, 2, 3) == (1, 2, 3))                               # True
print((97, 98) == ('a', 'b'))                               # False
print((97, 98) == tuple(map(ord,('a', 'b'))))               # True
print((1, 2, 3) == (1.0, 2.0, 3.0))                         # True
print('ABC' < 'C' < 'Pascal' < 'Python')                    # True
print('Ab' == 'ab')                                         # False
print((1, 2, 3, 4) < (1, 2, 4))                             # True
print((1, 2, 0) < (1, 2, -1))                               # False
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))       # True
