#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 11:27:41 2020

@author: vanish
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node: TreeNode, p_list: list):
        if node:
            p_list.append(node.val)
            p_list = self.inorder(node.left, p_list)
            p_list = self.inorder(node.right, p_list)
        else:
            p_list.append(None)
        return p_list
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.p_list = list()
        self.q_list = list()
        self.p_list = self.inorder(p, self.p_list)
        self.q_list = self.inorder(q, self.q_list)
        if (len(self.q_list) != len(self.p_list)):
            return False
        else:
            for num1, num2 in zip(self.p_list, self.q_list):
                if num1 != num2:
                    return False
            return True