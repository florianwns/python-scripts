#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les formatage de données

Il existe plusieurs façon de formater les données
avant écriture ou affichage

source : https://docs.python.org/fr/3/library/string.html#formatspec
         https://pyformat.info/
"""

# en utilisiant les chaines formatées f"" appelées "f-strings"
# nous pouvons directement inclure des variables
year = 2018
pi = 3.14159265359
print(f"Nous sommes en l'an {year}, et π vaut toujours {pi}")

# en utilisant str.format()
print("Nous sommes en l'an {}, et π vaut toujours {}".format(year, pi))
# ou
# print("Nous sommes en l'an {0}, et π vaut toujours {1}".format(year, pi))

# en utilisant la fonction repr() pour rendre compréhensible
# les données pour l'interpréteur ou la fonction eval()
chaine = (
    "Nous sommes en l'an "
    + repr(year)
    + ", et π vaut toujours "
    + repr(pi)
)
print(chaine)

# ou l'ancienne méthode de formatage %
print("Nous sommes en l'an %s, et π vaut toujours %s" % (year, pi))


# on peut ajouter des spécificateurs aux chaines formatées
print(f'La valeur approximtive de pi est : {pi:.3f}.')

# format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
# fill            ::=  <any character>
# align           ::=  "<" | ">" | "=" | "^"
# sign            ::=  "+" | "-" | " "
# width           ::=  digit+
# grouping_option ::=  "_" | ","
# precision       ::=  digit+
# type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

# on peut donc justifier les chaines, et les compléter avec des espaces
phones = {"Pascal": 8004, "David": 8003, "Accueil": 8099}
for name, phone in phones.items():
    print(f"| {name:>10} | {phone:-^10d} |")

# '!a' utilise ascii(), '!s' utilise str(), and '!r' utilise repr():
print(f"chaine = {chaine!a}")
print(f"chaine = {chaine!s}")
print(f"chaine = {chaine!r}")


# on aurait aussi pu accéder au élément du dictionnaire de la manière suivante
print('Accueil : {0[Accueil]:d}'.format(phones))
print('Accueil : {Accueil:d}'.format(**phones))
# vars() renvoie l'ensemble des variables locale sous la forme d'un dictionnaire
print('Accueil : {phones[Accueil]:d}'.format(**vars()))
