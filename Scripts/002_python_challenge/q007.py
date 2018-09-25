#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 007

Download : http://www.pythonchallenge.com/pc/def/oxygen.html

Download the image
and read data in RGBA Mode
"""

from PIL import Image
file = Image.open("oxygen.png")
pixels = list(file.getdata())
width, height = file.size
middle = height//2

pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

level = None
text = ""
for r, g, b, a in pixels[middle]:
    if r != level:
        level = r
        text += chr(level)

print(text)

# smart guy, you made it. the next level is
# [105, 10, 16, 101, 103, 14, 105, 16, 121]rpngbemkejlfca^_ba_ac
print("".join(list(map(chr, [105, 10, 16, 101, 103, 14, 105, 16, 121]))))
