#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 022

Source: http://www.pythonchallenge.com/pc/hex/copper.html

Emulate
or maybe white.gif would be more bright
"""

from PIL import Image, ImageDraw
from random import randint

def random_color():
    return (randint(150, 255), randint(150, 255), randint(150, 255), 255)

img = Image.open("./assets/white.gif")
new_img = Image.new("RGB", (500, 200))
draw = ImageDraw.Draw(new_img)

cx, cy = 0, 100
color = random_color()
for i in range(img.n_frames):
    img.seek(i)
    left, up, right, down = img.getbbox()
    dx, dy = left - 100, up - 100
    if dx == dy == 0:
        cx += 50
        cy = 100
        color = random_color()

    cx += dx
    cy += dy
    draw.point([cx, cy], fill=color)

new_img.show() # Bonus
