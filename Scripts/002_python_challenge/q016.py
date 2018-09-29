#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 016

Source: http://www.pythonchallenge.com/pc/return/mozart.html

let me get this straight
=> you need to align cols
"""
from PIL import Image

img = Image.open("assets/mozart.gif").convert('RGB')
data = list(img.getdata())
pixels = img.load()
pos = []
for j in range(img.size[1]):         # for every row
    for i in range(img.size[0]):     # for every col
        p = pixels[i, j]
        if p == (255, 0, 255):
            pos.append(i)
            break

new_img = Image.new('RGB', (img.size[0], img.size[1]))
new_pixels = new_img.load()

for j in range(img.size[1]):
    for i in range(img.size[0]):
        new_i = (pos[j] + i) % img.size[0]
        new_pixels[i, j] = pixels[new_i, j]

new_img.show()
# romance
