#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:08:15 2020

@author: vanish
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import deque
from collections import OrderedDict
class Solution:
    def bfs(self, node):
        queue = deque()
        queue.append((0,0, node))
        while queue:
            column, row, node = queue.popleft()
            if node is not None:
                self.nodes.append((column, row, node.val))
                queue.append((column-1, row+1, node.left))
                queue.append((column+1, row+1, node.right))
            
    
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.nodes = []
        self.bfs(root)
        self.nodes.sort()
        print (self.nodes)
        answer = OrderedDict()
        for node in self.nodes:
            if node[0] in answer:
                answer[node[0]].append(node[2])
            else:
                answer[node[0]] = [node[2]]
        return answer.values()
        
        