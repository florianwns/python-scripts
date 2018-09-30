#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 018

Source: http://www.pythonchallenge.com/pc/return/balloons.html

can you tell the difference?
it is more obvious that what you might think

the difference is the 'brightness'
=> http://www.pythonchallenge.com/pc/return/brightness.html

maybe consider deltas.gz
"""

import gzip, difflib

f = gzip.open("assets/deltas.gz")

left, right = [], []

for line in f:
    left.append(line[:53].decode() + '\n')
    right.append(line[56:].decode())


diff = difflib.Differ().compare(left, right)

f = open("assets/diff.png", "wb")
f1 = open("assets/diff1.png", "wb")
f2 = open("assets/diff2.png", "wb")

for line in diff:
    print(line)
    bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])
    if line[0] == '+':
        f1.write(bs)
    elif line[0] == '-':
        f2.write(bs)
    else:
        f.write(bs)

f.close()
f1.close()
f2.close()

# http://www.pythonchallenge.com/pc/hex/bin.html
# login : butter
# password : fly
