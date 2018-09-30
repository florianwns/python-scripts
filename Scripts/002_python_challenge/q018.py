#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 018

Source: http://www.pythonchallenge.com/pc/return/balloons.html

can you tell the difference?
it is more obvious that what you might think
"""

from PIL import Image, ImageChops
import numpy

balloons =  Image.open("assets/balloons.jpg")
pixels =  balloons.load()

w, h = balloons.size
w //= 2
img1 = Image.new('RGB', (w, h))
pixels1 = img1.load()
img2 = Image.new('RGB', (w, h))
pixels2 = img2.load()

for j in range(h):
    for i in range(w):
        pixels1[i, j] = pixels[i, j]
        pixels2[i, j] = pixels[i + w, j]

img1.show()
img2.show()
