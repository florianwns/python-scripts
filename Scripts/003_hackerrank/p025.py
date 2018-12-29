#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 025

Text Alignment

Source : https://www.hackerrank.com/challenges/text-alignment/problem
"""
l = "H"
w = int(input())

#top cone
for i in range(w):
    t = ((2*i)+1)*l
    print(t.center(2*w-1," ").rstrip())

# top pillars
for i in range(w+1):
    t = ""
    for m in [1,0,0,0,1]:
        t += w*(l if m else " ")
    print(t.rjust(w*5+(w-1)//2))

# middle
for i in range((w+1)//2):
    t = ""
    for m in [1,1,1,1,1]:
        t += w*(l if m else " ")
    print(t.rjust(w*5+(w-1)//2))

# bottom pillars
for i in range(w+1):
    t = ""
    for m in [1,0,0,0,1]:
        t += w*(l if m else " ")
    print(t.rjust(w*5+(w-1)//2))

#bottom cone
for i in reversed(range(w)):
    t = ((2*i)+1)*l
    print((" "*(w*4)) + t.center(2*w-1," ").rstrip())
