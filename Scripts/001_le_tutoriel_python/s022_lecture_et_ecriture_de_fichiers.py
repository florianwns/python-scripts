#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Lecture et écriture de fichier

source : https://docs.python.org/fr/3/library/functions.html#open
"""
import json

# open(nomfichier, mode) renvoie un objet fichier
# par défaut le mode est 'r' : lecture seule
with open('data/lorem_ipsum.txt') as f:

    # on peut lire une ligne
    print(f.readline(), end='')

    # on peut lire tout le fichier ligne par ligne
    for line in f:
        print(line, end='') # la fin de ligne \n est déjà dans le fichier

    # ou tout d'un bloc
    f.read()

    # revient au début du fichier
    f.seek(0)

    # renvoie toutes les lignes sous forme de liste
    # équivalent à list(f)
    lines = f.readlines()
    print(lines)


# ouvertude écriture
# 'r'	ouvre en lecture (par défaut)
# 'w'	ouvre en écriture, tronquant le fichier
# 'x'	ouvre pour une création exclusive, échouant si le fichier existe déjà
# 'a'	ouvre en écriture, ajoutant à la fin du fichier s’il existe
# 'b'	mode binaire
# 't'	mode texte (par défaut)
# '+'	ouvre un fichier pour le modifier (lire et écrire)
# 'U'	mode universal newlines (obsolète)
with open('data/data.json', 'w+') as f:
    # écrire du json
    json.dump([1, 'simple', 'list'], f)

    try:
        f.seek(0)                   # revient au début du fichier
        x = json.load(f)            # charge les données
        print(x)                    # affiche les données
    except ValueError as e:         # contient json.decoder.JSONDecodeError
        print("Decode Error : " + str(e))
