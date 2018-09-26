#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 012

Source : http://www.pythonchallenge.com/pc/return/evil.html

dealing evil

you have to download :
    http://www.pythonchallenge.com/pc/return/evil2.gfx

Bert is evil! go back ^^
    http://www.pythonchallenge.com/pc/return/bert.html
"""
from PIL import Image
import io

f = open("assets/evil2.gfx", 'rb')
nb_images = 5
raw_images = [b'' for i in range(nb_images)]

byte = True
i = 0
while byte:
    i %= nb_images
    byte = f.read(1)
    raw_images[i] += byte
    i += 1

extensions = ['jpg', 'png', 'gif', 'png', 'jpg']
for i in range(nb_images):
    f = open(f"assets/dealing_evil_{i}.{extensions[i]}", 'wb')
    f.write(raw_images[i])
    f.close()

# disproportional
