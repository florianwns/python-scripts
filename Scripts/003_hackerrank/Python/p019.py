#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 019

Validating UID

Source : https://www.hackerrank.com/challenges/validating-uid/problem
"""
import re

r1 = r"^(?=.*[0-9]){3,}(?=.*[a-zA-Z]){2,}([a-zA-Z0-9]+)$"
for _ in range(int(input())):
    try:
        uid = input()
        assert re.match(r1, uid)
        assert len(set(uid)) == 10
        assert len(uid) == 10
    except:
        print('Invalid')
    else:
        print('Valid')
