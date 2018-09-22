#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les listes imbriquées

On les appeles aussi 'tableaux multidimensionnels'
dans d'autres langages
"""

matrix = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6]
]
print(matrix)

# cette compréhension de liste intervertit
# les lignes et les colonnes d'une matrice de 3x4
transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)

# cette exemple est équivalent au lignes suivantes
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
