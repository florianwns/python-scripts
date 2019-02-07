#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 15: Linked List

Source : https://www.hackerrank.com/challenges/30-linked-list/problem
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        current = head
        if head:
            while current.next:
                current = current.next
            current.next = Node(data)
            return head
        else:
            return Node(data)

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
