#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 032

Merge the Tools!

Source : https://www.hackerrank.com/challenges/merge-the-tools/problem
"""
def merge_the_tools(string, max_width):
    l = [string[i:i+max_width] for i in range(0, len(string), max_width)]
    for w in l:
        print("".join(sorted(set(w), key=w.index)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
