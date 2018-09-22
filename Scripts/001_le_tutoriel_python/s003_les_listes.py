#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les listes

Quelques exemples de manipulations et copies des listes
"""

import copy

liste = [[1, 2], [2, 3], 4]   # initialise une liste

print(liste[0])                     # retourne le premier élément
print(liste[-1])                    # retourne le dernier élément
print(liste[1:], end="\n\n")        # retourne une liste en partant du 2nd élément




# copie de liste
liste1 = liste          # renvoie une copie par référence de la liste, pointe donc vers le même objet

liste2 = liste[:]       # renvoie une copie superficielle de la liste,
                        # équivaux à liste.copy(), ou encore list(liste),
                        # ou encore copy.copy(liste)

liste3 = copy.deepcopy(liste)   # renvoie une copie profonde de la liste, nécessite le module copy

# les 'liste2' et 'liste3' ont de réf différentes,
# si les valeurs de premier niveau de 'liste' sont modifiées, 'liste2' et 'liste3' ne seront pas modifiées
# contrairement à liste1 qui pointe exactement vers les mêmes données
print(id(liste), "==", id(liste1), "!=", id(liste2), "!=", id(liste3), end="\n\n")

# par contre tout le monde pointe vers la même sous liste sauf la copie profonde 'liste3',
# qui a une autre instance de liste d'où son nom
print(id(liste[0]), "==", id(liste1[0]), "==", id(liste2[0]),'!=', id(liste3[0]), end="\n\n")

# les valeurs de toute les listes gardent les mêmes réfs tant qu'elles ne sont pas été modifiées
# même pour la copie profonde
print(id(liste[0][0]), id(liste1[0][0]), id(liste2[0][0]), id(liste3[0][0]))
print("    ↓          ↓          ↓          =    ")
liste[0][0] = 1         # la ref ne change que si la valeur est différente
liste[0][0] = 3
print(id(liste[0][0]), id(liste1[0][0]), id(liste2[0][0]), id(liste3[0][0]))
print("    =          =                          ")
liste[2] = 3            # remarquons que c'est la même ref que la valeur 3
                        # stockée dans liste[0][0] et liste[1][1]
print(id(liste[2]), id(liste1[2]), id(liste2[2]), id(liste3[2]), end="\n\n")


# Il y a donc 3 types de copies différentes
# cf article => https://www.python-course.eu/python3_deep_copy.php


liste2 = [0, 4, 9, 16]
liste2 += [25, 35]    # concatenation avec une autre liste => liste2.extend([25, 35])
liste2[-1] = 36       # remplacement du dernier élément
liste2.append(64)     # ajout d'un élément à la fin de la liste
liste2.insert(-1,49)  # ajout d'un élément à l'index donné en paramètre
liste2[2:] = [2, 5]   # supprime tout les élément à partir de la 3eme
                      # et insère les nouveau éléments
del liste2[0]         # supprime le 1er élément (index 0)
liste2.reverse()      # inverse les données
liste2.sort()         # tri la liste, ne fonctionne qu'avec des données du même type
liste2.remove(4)      # supprime la premier occurence de 4 trouvé dans la liste
                      # ValueError si l'élement n'est pas dans la liste
liste2.pop()          # retourne le dernier élément et le supprime,
                      # pratique pour vider une liste

print(liste2, "=>", len(liste2), "élements")    # affiche le nombre d'élement d'une liste

liste[:] = []         # vide la liste
                      # équivaut à liste.clear()


# les listes peuvent comporter tout types de données
# par contre, dans ce cas la méthode sort() n'est plus utilisable
liste2dim = [['a', 'b', 3], [1, 2, "e"]]
print(liste2dim)

liste = list(range(5))          # on peut aussi créer une liste
print(liste)                    # à partir de l'objet range

liste = [i ** 2 for i in range(1, 30) if i % 2]
print(liste)

liste[0:10:2] = [3, 4, 0, 6, 10]     # De 0 à 9, change un élément tout les 2 élements
print(liste)
