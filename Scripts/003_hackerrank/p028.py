#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 028

String Formatting

Source : https://www.hackerrank.com/challenges/python-string-formatting/problem
"""
def print_formatted(number):
    w = len("{:b}".format(number))
    for i in range(1,number+1):
        print("{0:>{1}} {0:>{1}o} {0:>{1}X} {0:>{1}b}".format(i,w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
