#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 031

The Minion Game

Source : https://www.hackerrank.com/challenges/the-minion-game/problem
"""
def is_vowel(c):
    return c in ("A","E","I","O","U")

def minion_game(word):
    p1, p2 = 0, 0
    nb = len(word)
    for i in range(nb):
        if is_vowel(word[i]):
            p2 += nb - i
        else:
            p1 += nb - i
    if p1 > p2:
        print("Stuart", p1)
    elif p1 < p2:
        print("Kevin", p2)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
