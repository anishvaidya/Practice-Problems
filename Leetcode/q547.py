#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:59:30 2020

@author: vanish
"""

from typing import List
class Solution:
    def dfs(self, M, i):
        for j in range(len(M[i])):
            if M[i][j] == 1 and j not in self.visited:
                self.visited.add(j)
                self.dfs(M, j)
    
    def findCircleNum(self, M: List[List[int]]) -> int:
        self.visited = set()
        count = 0
        for i in range(len(M)):
            if i not in self.visited:
                count += 1
                self.visited.add(i)
                self.dfs(M, i)
        return count
        
        
#%%
M = [[1,1,0], [1,1,0], [0,0,1]]

ans = Solution()
print (ans.findCircleNum(M))