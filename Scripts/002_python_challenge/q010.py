#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 010

Source : http://www.pythonchallenge.com/pc/return/bull.html

what are you looking at ?

len(a[30]) = ?
a = [1, 11, 21, 1211, 111221]
solution : http://villemin.gerard.free.fr/Puzzle/SeqComme.htm
"""

a = ["1"]
for i in range(31):
    # init value
    value = ""

    # init temporary variable
    last_char = ""
    number_count = 0
    chars = list(a[i])
    last_char = chars[0]

    # read all chars
    for char in chars:
        if last_char != char:
            value += str(number_count) + last_char
            last_char = char
            number_count = 0

        number_count += 1

    value += str(number_count) + last_char
    a.append(value)


print(a)
print(len(a[30]))

# 5808
