#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 107

Company Logo

Source : https://www.hackerrank.com/challenges/most-commons/problem
"""
from collections import Counter
l = sorted(Counter(input()).items(), key=lambda x: (-x[1], x[0]))
[print(*l[i]) for i in range(3)]

# or

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
