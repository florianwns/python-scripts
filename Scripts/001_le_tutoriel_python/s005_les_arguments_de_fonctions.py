#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les arguments de fonctions

Compendre comment les arguments fonctionnent dans python
"""


# les arguments par défaut sont évalués
# lors de la définication de la fonction
i = 5
def f(arg=i):
    print(arg)

i = 6
f()

# L'argument par défaut n'est executé qu'une seule fois
def f(a, L=[]):
    L.append(a)
    return L

# notez ici que la liste L est transmis par référence
# on ne transmet pas un copie de L
print(f(1), f(2))

# Si vous voulez que la valeur par défaut
# soit réinitialisé à chaque appel, employez le mot clé 'None'
# comme ci-dessous
def f(a, L=None):
    if L is None:
        L = []      # Si None, on initialise la liste
    L.append(a)
    return L

print(f(1), f(2))

# le mot clé 'pass' ne sert à rien, mais peut être pratique
# si vous avez prévu d'implémenter une fonction un peu plus tard
def nothing():
    pass        # TODO : coder la fonction qui ne retourne rien


# Les arguments nommés
# on peut appeler une fonction en lui passant les arguments
# dans l'ordre que l'on souhaite en utilisant ou pas les arguments nommées
def is_triangle(a=0, b=0, c=0):
    return a > 0 and b > 0 and c > 0

print(is_triangle(c=3, a=0, b=1))
print(is_triangle(1,2,3))


# Si un ou plusieurs arguments nommées sont passées en arguments
# on peut utiliser le ** pour les récupérer
# sous la forme d'un dictionnaire.
# on peut aussi récupérer les arguments excédents non nommés
# sous la forme d'un tuple, ATTENTION à l'ordre des arguments
# Tout ces arguments sont optionnels
def make_a_movie_script(title, *script, **casting):
    header = "------- {0} ------".format(title)
    print(header)
    for text in script:
        print(text)
    print("-" * len(header))
    for character in sorted(casting.keys()):
        print("{0} : {1}".format(character, casting[character]))


make_a_movie_script('Godzilla', "John : Hello guy", "Pit : Hey John", Pit="Matthew Macgonogay", John="Tom Cruise")



# a l'inverse on peut séparer les éléments d'un tuple avec *
args = [3,6]
print(list(range(*args)))

# ou avec ** pour un dictionnaire
casting = {"Kevin": "Brad Pitt", "Gary": "Bruce Willis"}
make_a_movie_script('La revanche d\'un blond', **casting)
