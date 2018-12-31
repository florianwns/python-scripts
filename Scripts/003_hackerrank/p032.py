#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 032

Merge the Tools!

Source : https://www.hackerrank.com/challenges/merge-the-tools/problem
"""
def merge_the_tools(string, max_width):
    for word in zip(*[iter(string)] * max_width):
        print(''.join(sorted(set(word), key=word.index)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
