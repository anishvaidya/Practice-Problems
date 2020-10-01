#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:09:39 2020

@author: vanish
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, pathsum):
        if node:
            pathsum += node.val
            self.dfs(node.left, pathsum)
            self.dfs(node.right, pathsum)
            if not node.left and not node.right:

                if pathsum == self.sum:
                    self.ans = True
            
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.sum = sum
        self.ans = False
        self.dfs(root, 0)
        return self.ans
