#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 23: BST Level-Order Traversal

Source : https://www.hackerrank.com/challenges/30-binary-trees/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_r=next-challenge&h_v=zen
"""
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root:
            leftHeight = self.getHeight(root.left)
            rightHeight = self.getHeight(root.right)
            return max(leftHeight, rightHeight) + 1
        else:
            return 0;

    def printLevel(self, root, level):
        if root:
            if level == 0:
                print(root.data, end=" ")
            else:
                self.printLevel(root.left, level - 1)
                self.printLevel(root.right, level - 1)

    def levelOrder(self,root):
        for i in range(self.getHeight(root)):
            self.printLevel(root, i)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
