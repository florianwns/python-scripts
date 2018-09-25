#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 005

Source : http://www.pythonchallenge.com/pc/def/peak.html
pronounce it

peak hell => pickle

les fichiers .p sont des fichiers utilisé par pickle
"""

import pickle

data = pickle.load(open("banner.p", "rb" ))
for elt in data:
    # print "".join([e[1] * e[0] for e in elt])
    for e in elt:
        print(e[1] * e[0], end ="")
    print(e[1] * e[0])
