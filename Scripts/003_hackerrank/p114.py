#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 114

Words Score

Source : https://www.hackerrank.com/challenges/words-score/problem?
"""
def score_words(words):
    return sum([sum(map(word.count, "aeiouy")) % 2 or 2 for word in words])

n = int(input())
words = input().split()
print(score_words(words))
