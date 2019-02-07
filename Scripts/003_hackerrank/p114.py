#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 114

Words Score

Source : https://www.hackerrank.com/challenges/words-score/problem?
"""
def score_words(words):
    return sum([sum([c in "aeiouy" for c in w]) % 2 or 2 for w in words])

n = int(input())
words = input().split()
print(score_words(words))
