#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 001

Source : http://www.pythonchallenge.com/pc/def/map.html

find rare characters in the mess below:
everybody thinks twice before solving this.
"""

text = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""

liste = map(lambda x: x if ord(x) < 97
            else chr(ord(x) - 24) if ord(x) >= 121
            else chr(ord(x) + 2), text)

print(''.join(liste))

# i hope you didnt translate it by hand. thats what computers are for.
# doing it in by hand is inefficient and that's why this text is so long.
# using string.maketrans() is recommended. now apply on the url.

# map => ocr
# http://www.pythonchallenge.com/pc/def/ocr.html
