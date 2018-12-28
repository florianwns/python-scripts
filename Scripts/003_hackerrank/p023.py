#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 023

Find a string

Source : https://www.hackerrank.com/challenges/find-a-string/problem
"""
def count_substring(string, sub_string):
    return sum(string[i:i+len(sub_string)] == sub_string for i in range(len(string)))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
