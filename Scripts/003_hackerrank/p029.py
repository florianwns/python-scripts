#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 029

Alphabet Rangoli

Source : https://www.hackerrank.com/challenges/alphabet-rangoli/problem
"""
import string

def print_rangoli(size):
    l = list(string.ascii_lowercase)
    width = 2*(2*size-1)-1
    motif = "-"
    for i in range(1,size*2):
        pos = i if i <= size else 2*size-i
        ar = list(reversed(l[size-pos:size]))+l[size-pos+1:size]
        print(motif.join(ar).center(width, motif))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
