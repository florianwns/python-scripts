#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 095

String Split and Join

Source : https://www.hackerrank.com/challenges/python-string-split-and-join/problem
"""
def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
