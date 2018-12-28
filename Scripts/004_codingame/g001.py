#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""There is no Spoon - Episode 1

Source : https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-1
"""
import sys
import math

# Don't let the machines win. You are humanity's last hope...
def debug (x):
    print(x, file=sys.stderr)
    return

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
nodes = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    debug(line)
    nodes.insert(i, [])
    for j in range(len(line)):
        if line[j] == "0":
            nodes[i].append(j)

debug(nodes)
for i in range(len(nodes)):
    for j in range(len(nodes[i])):
        x1, y1, x2, y2, x3, y3 = nodes[i][j], i, -1, -1, -1, -1

        # if there is a neighbor on the same line
        if j+1 < len(nodes[i]):
            x2, y2 = nodes[i][j+1], i

        # if there is a neighbor on the same row
        found = False
        if i+1 < len(nodes):
            for l in range(i+1, len(nodes)):
                if len(nodes[l]) > 0:
                    for k in range(len(nodes[l])):
                        if not found and nodes[l][k] == nodes[i][j]:
                            x3, y3 = nodes[l][k], l
                            found = True

        print('{} {} {} {} {} {}'.format(x1, y1, x2, y2, x3, y3))
