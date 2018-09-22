#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les files FIFO

FIFO pour first-in, first-out
« premier entré, premier sorti »

Utiliser popleft() est plus rapide que pop(0) sur une liste
"""

from collections import deque

queue = deque(["orange", "banana", "apple", "kiwi"])

queue.append("raspberry")
print(queue)
print(queue.popleft())
print(queue)
