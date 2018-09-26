#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 011

Source : http://www.pythonchallenge.com/pc/return/5808.html

odd even
"""

from PIL import Image
img = Image.open("cave.jpg")
pixels = img.load()
print(pixels)

for i in range(img.size[0]):       # for every col
    for j in range(img.size[1]):    # for every row
        if i % 2 == 1 or j % 2 == 1:
            pixels[i,j] = (0, 0, 0)    # make a pixel black

img.show()

# you should see 'evil'
