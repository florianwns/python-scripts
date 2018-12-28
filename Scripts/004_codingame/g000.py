#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Shadows of the Knight - Episode 1

Source : https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1
"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]
last_pos = [{x,},{y}]

once = True
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # trouve l'ancienne position la plus proche
    next_pos = [x, y]
    if "L" in bomb_dir:
        neighbour = 0
        for last_x in last_pos[0]:
            if last_x < x:
                if last_x > neighbour:
                    neighbour = last_x
        diff = int(round((x - neighbour)/2))
        diff = diff if diff > 1 else 1
        next_pos[0] = x - diff
    elif "R" in bomb_dir:
        neighbour = w
        for last_x in last_pos[0]:
            if last_x > x:
                if last_x < neighbour:
                    neighbour = last_x
        diff = int(round((neighbour - x)/2))
        diff = diff if diff > 1 else 1
        next_pos[0] = x + diff

    if "U" in bomb_dir:
        neighbour = 0
        for last_y in last_pos[1]:
            if last_y < y:
                if last_y > neighbour:
                    neighbour = last_y
        diff = int(round((y - neighbour)/2))
        diff = diff if diff > 1 else 1
        next_pos[1] = y - diff

    elif "D" in bomb_dir:
        neighbour = h
        for last_y in last_pos[1]:
            if last_y > y:
                if last_y < neighbour:
                    neighbour = last_y
        diff = int(round((neighbour - y)/2))
        diff = diff if diff > 1 else 1
        next_pos[1] = y + diff

    last_pos[0].add(next_pos[0])
    last_pos[1].add(next_pos[1])

    x, y = next_pos
    print("{} {}".format(x, y))
