#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 08:31:02 2020

@author: vanish
"""
#%%
from typing import List
#%%
class Solution:
    def explore_dfs(self, i, j, grid):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != '1':
            return
        else:
            grid[i][j] = "*"
            self.explore_dfs(i + 1, j, grid)
            self.explore_dfs(i - 1, j, grid)
            self.explore_dfs(i, j + 1, grid)
            self.explore_dfs(i, j - 1, grid)
            # use 8 neighbors only if specified
            # self.explore_dfs(i + 1, j + 1, grid)
            # self.explore_dfs(i + 1, j - 1, grid)
            # self.explore_dfs(i - 1, j + 1, grid)
            # self.explore_dfs(i - 1, j - 1, grid)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        c_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.explore_dfs(i, j, grid)
                    c_island += 1
        return c_island
    
#%%

# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
ans = Solution()
print (ans.numIslands(grid))
# %%
