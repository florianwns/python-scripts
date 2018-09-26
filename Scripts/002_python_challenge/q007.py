#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 007

Source : http://www.pythonchallenge.com/pc/def/oxygen.html

Download the image
and read data in RGBA Mode
"""

from PIL import Image
file = Image.open("assets/oxygen.png")
data = list(file.getdata())
width, height = file.size
pixels = [data[i * width:(i + 1) * width] for i in range(height)]

level, text, middle = None, "", height//2
for r, g, b, a in pixels[middle]:
    if r == g and g == b and r != level:
        level = r
        text += chr(level)
print(text)

# smart guy, you made it. the next level is [105, 10, 16, 101, 103, 14, 105, 16, 121]
answer = [105, 10, 16, 101, 103, 14, 105, 16, 121]
print(''.join(chr(i) if i > 100 else chr(i+100) for i in answer))

# integrity
