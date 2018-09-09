"""Play with Turtle

Petit script de prise en main de turtle
"""

import turtle

wn = turtle.Screen()        # creates a graphics window
t = turtle.Turtle()

def carre(taille):
    "fonction qui dessine un carré de taille et de couleur déterminées"
    index = 0
    while index < 4:
        t.forward(taille)
        t.right(90)
        index += 1

t.color("blue")
t.up()
t.goto(-150, 50)
i = 0
while i < 10:
    t.down()
    carre(25)
    t.up()
    t.forward(30)
    i = i +1

a = input()
