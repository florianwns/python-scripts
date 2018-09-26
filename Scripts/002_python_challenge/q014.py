#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 014

Source: http://www.pythonchallenge.com/pc/return/italy.html

walk around
remember: 100*100 = (100+99+99+98) + (...

bit => you took the wrong curve.
"""
from PIL import Image
img = Image.open("assets/wire.png")
data = list(img.getdata())

# new_img = Image.new('RGB', (100, 100))
# pixels = new_img.load()
# for i in range(new_img.size[0]):       # for every col
#     for j in range(new_img.size[1]):    # for every row
#         pixels[i,j] = data[i + j*100]
#
# new_img.show() # bit => you took the wrong curve.


coord = (-1,0)
length = 100
z = 0
new_img = Image.new('RGB', (100, 100))
pixels = new_img.load()

while length > 0 :
    orders = [
        ((1, 0), length),
        ((0, 1), length - 1),
        ((-1, 0), length - 1),
        ((0, -1), length - 2)
    ]
    for order in orders :
        direction, distance = order
        for i in range(0, distance):
            coord = (
                coord[0] + direction[0],
                coord[1] + direction[1]
            )
            pixel = data[z]
            pixels[coord] = pixel
            z += 1
    length -= 2

# this photo is a cat, and it's name is 'usi'
new_img.show()
