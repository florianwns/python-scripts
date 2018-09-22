#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les piles LIFO

LIFO pour last-in, first-out
« dernier entré, premier sorti »

Utiliser pop() sur une liste
"""

stack = ["orange", "banana", "apple", "kiwi"]

stack.append("raspberry")
print(stack)
print(stack.pop())
print(stack)
