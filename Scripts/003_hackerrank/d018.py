#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 18: Queues and Stacks

Source : https://www.hackerrank.com/challenges/30-queues-stacks/problem?h_r=next-challenge&h_v=zen
"""
import sys
from collections import deque

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = deque() # faster than list

    # stack -> LIFO (last input first output)
    def pushCharacter(self, c):
        self.stack.append(c)

    def popCharacter(self):
        return self.stack.pop()

    # queue -> FIFO (first input first output)
    def enqueueCharacter(self, c):
        self.queue.append(c)

    def dequeueCharacter(self):
        return self.queue.popleft()


# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
