#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les boucles et les instruction de contrôle

Quelques exemples de manipulations des boucles et des instructions
"""

# la suite de fibonnaci
a, b = 0, 1
while a < 20:                
    print(a, end=",")       # on idente de 4 espace l'instruction suivante
    a, b = b, a+b
print()

if a == 21:
    print("_")
elif a == 13:               # 'else if' se note 'elif' en python
    print("°")
else:
    print(")")


# Un peu d'unicode ;) et des boucles for
words = ["Bonjour", "Jeune", "Padawan"]
for w in words:
    if w == "Yoda":
        break               # le 'break' permet de sortie de la boucle,
else:                       # par contre on passe dans le 'else' si le break 
                            # n'est jamais appelé dans la boucle for'
                            # ici on utilise le r de raw_string 
    st = r"""               
                        ____
                    (xXXXX|xx======---(-
                    /     |
                    /    XX|
                    /xxx XXX|
                /xxx X   |
                / ________|
        __ ____/_|_|_______\_
    ###|=||________|_________|_
        ~~   |==| __  _  __   /|~~~~~~~~~-------------_______
            |==| ||(( ||()| | |XXXXXXXX|                    >
        __   |==| ~~__~__~~__ \|_________-------------~~~~~~~
    ###|=||~~~~~~~~|_______  |"
        ~~ ~~~~\~|~|       /~
                \ ~~~~~~~~~
                \xxx X   |
                    \xxx XXX|
                    \    XX|                Incom's T-65B X-wing Space
                    \     |                Superiority Starfighter (4)
                    (xXXXX|xx======---(-
                        ~~~~"""
    print(st)


# on peut aussi utiliser range dans la même idée 
# que la boucle for(i = 0; i < words.length; i++) dans d'autres langage
for i in range(len(words)):
    print(words[i], len(words[i]))


# exemple de range qui est objet iterable, 
# et pas une liste à proprement parlée
range(5)                # 0, 1, 2, 3, 4
range(5, 10)            # 5, 6, 7, 8, 9
range(0, 10, 3)         # 0, 3, 6, 9
range(-10, -100, -30)   # -10, -40, -70


# mot clé 'pass'
a = 9
if a < 10:
    pass        # 'pass' ne fait rien, mais est parfois nécessaire après une instruction
                # TODO : Afficher un message d'erreur...
else:
    print("a supérieur a 10")
