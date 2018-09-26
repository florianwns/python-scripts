#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 006

Source : http://www.pythonchallenge.com/pc/def/channel.html
The following has nothing to do with the riddle itself. I just
thought it would be the right point to offer you to donate to the
Python Challenge project. Any amount will be greatly appreciated.

-thesamet

Download : http://www.pythonchallenge.com/pc/def/channel.zip
"""

import zipfile
import re

nothing = "90052"
comments = []
with zipfile.ZipFile('assets/channel.zip') as zip_file:
    while True:
        info = zip_file.getinfo(nothing + ".txt")       # récupère les infos
        comments.append(info.comment.decode("utf-8"))   # ajout le commentaire
        file = zip_file.open(info)                      # ouvre le fichier
        text = file.read().decode("utf-8")              # lit la première ligne
        if "Next nothing is" in text:
            nothing = "".join(re.findall('nothing is ([0-9]*)', text))
        else:
            break

print("".join(comments))

# read 'oxygen' and not 'hockey'
