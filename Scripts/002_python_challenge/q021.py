#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 021

Source: ./assets/level_21.zip

Yes! This is really level 21 in here.
And yes, After you solve it, you'll be in level 22!

Now for the level:

* We used to play this game when we were kids
* When I had no idea what to do, I looked backwards.
"""

import zipfile, zlib, bz2

with zipfile.ZipFile("assets/level_21.zip") as zip_file:
    zip_file.extractall(pwd=b"redavni", path="assets/level_21")

with open("assets/level_21/package.pack", "rb") as f:
    data = f.read()
    result = ''
    while True:
        if data.startswith(b'x\x9c'):
            data = zlib.decompress(data)
            result += ' '
        elif data.startswith(b'BZh'):
            data = bz2.decompress(data)
            result += '#'
        elif data.endswith(b'\x9cx'):
            data = data[::-1]
            result += '\n'
        else:
            break
    print(data[::-1].decode())  # look at your logs
    print(result)  # Copper
