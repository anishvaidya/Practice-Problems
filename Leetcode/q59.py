#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:38:26 2020

@author: vanish
"""
from typing import List
#%%
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        spiral = [["#" for i in range(n)] for j in range(n)]
        direction = {'right': [0, 1], 
                     'down': [1, 0],
                     'left': [0, -1],
                     'up': [-1, 0]
                     }
        x, y = 0, 0
        seen = 0
        curr_dir = 'right'
        while seen < (n ** 2):
            if y == n:
                curr_dir = "down"
                x, y = x + direction[curr_dir][0], y + direction[curr_dir][1] - 1
            if x == n:
                curr_dir = "left"
                x, y = x + direction[curr_dir][0] - 1, y + direction[curr_dir][1]
            if y < 0:
                curr_dir = "up"
                x, y = x + direction[curr_dir][0], y + direction[curr_dir][1] + 1
            
            if spiral[x][y] != "#":
                x, y = x - direction[curr_dir][0], y - direction[curr_dir][1]
                
                if curr_dir == "right":
                    curr_dir = "down"
                elif curr_dir == "down":
                    curr_dir = "left"
                elif curr_dir == "up":
                    curr_dir = "right"
                elif curr_dir == "left":
                    curr_dir = "up"
                x, y = x + direction[curr_dir][0], y + direction[curr_dir][1]
                
            elif spiral[x][y] == "#":
                seen += 1
                spiral[x][y] = seen
                x, y = x + direction[curr_dir][0], y + direction[curr_dir][1]
        
        
        return spiral
    
#%%
n = 4
ans = Solution()
print (ans.generateMatrix(n))