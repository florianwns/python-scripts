#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 004

Source : http://www.pythonchallenge.com/pc/def/linkedlist.php
urllib may help. DON'T TRY ALL NOTHINGS, since it will never
end. 400 times is more than enough.

Début de la routine ici :
    http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

Opening URL: 16044
    Yes. Divide by two and keep going.

Opening URL: 82682
    There maybe misleading numbers in the
    text. One example is 82683. Look only for the next nothing and the next nothing is 63579
"""

import re
from urllib import (parse, request)
import webbrowser

site = "http://www.pythonchallenge.com/pc/def/"
opt = "linkedlist.php?nothing="
nothing = "16044"

while True:
    with request.urlopen(site + opt + nothing) as f:
        text = f.read().decode('utf-8')
        print(text)
        if "the next nothing is" in text:
            nothing = "".join(re.findall('nothing is ([0-9]*)', text))
            print("Opening URL:", nothing)
        elif "Divide" in text:
             nothing = str(int(nothing)/2)
             print("Divided nothing:", nothing)
        else:
            webbrowser.open(site + text)
            break
