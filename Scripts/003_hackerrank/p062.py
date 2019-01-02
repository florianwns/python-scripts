#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 062

ginortS

Source : https://www.hackerrank.com/challenges/ginorts/problem
"""
s = input()
def custom_index(c):
    i = ord(c)
    if i in range(65,91):
        i += 100
    elif i in range(48,58):
        if i%2:
            i += 200
        else:
            i += 300
    return i

print(''.join(sorted(s, key=lambda c: custom_index(c))))

# other solution
print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

# bin(ord('z')) => '0b1111010'
# bin(ord('z')) >> 5 => '0b11
# -ord('z') >> 5 >> 5 => -4
# -ord('Z') >> 5 >> 5 => -3
# -ord('0') >> 5 >> 5 => -2
