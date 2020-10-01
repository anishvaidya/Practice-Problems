#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:53:37 2020

@author: vanish
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def add(self, node, answer):
        if node:
            answer = answer * 10 + node.val
            self.add(node.left, answer)
            self.add(node.right, answer)
            if not node.left and not node.right:
                self.ans += answer
    
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0
        if not root:
            return 0
        else:
            self.add(root,0)
        return self.ans
        