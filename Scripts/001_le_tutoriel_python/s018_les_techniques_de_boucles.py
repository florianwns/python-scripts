#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les techniques de boucles

Parce qu'en python la boucle for utilise les itérateurs
on peut faire plein de choses efficaces
"""

# on peut :
# récupérer les clés : valeurs comme dans avec key => value en PHP
heroes = {"Batman": "Bruce Wayne", "Spider-man": "Peter Parker", "Superman": "Clark Kent"}
for key, value in heroes.items():
    print(key, ":", value)

# faire la même chose avec les listes
liste = ['tic', 'tac', 'toe']
for index, value in enumerate(liste):
    print(index, ":", value)

# faire des boucles sur plusieurs listes en même temps
questions = ["favorite meal", "quest", "favorite color"]
answers = ["Burgers", "Save the universe", "It's red"]
for question, answer in zip(questions, answers):
    print("What's your {0} ?  {1}.".format(question, answer))

# faire une boucle en sens inverse
for value in reversed(liste):
    print(value)
