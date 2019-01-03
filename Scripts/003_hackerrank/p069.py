#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 069

Group(), Groups() & Groupdict()

Source : https://www.hackerrank.com/challenges/re-group-groups/problem
"""
import re
matches = re.findall(r"([a-zA-Z0-9])\1", input())
print(matches[0] if matches else -1)

# other solution
import re
matches = re.search(r'([a-zA-Z0-9])\1', input())
print(matches.group(1) if matches else -1)
