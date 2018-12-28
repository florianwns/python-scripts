#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 021

What's Your Name?

Source : https://www.hackerrank.com/challenges/whats-your-name/problem
"""

def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a,b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
