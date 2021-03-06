#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 20:20:43 2020

@author: vanish
"""

from typing import List
#%%
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not len(matrix):
            return matrix
        direction = {'right': [0, 1], 
                     'down': [1, 0],
                     'left': [0, -1],
                     'up': [-1, 0]
                     }
        spiral = list()
        x, y = 0, 0
        seen = 0
        curr_dir = 'right'
        while seen < (len(matrix) * len(matrix[0])):
            if y == len(matrix[0]):
                curr_dir = "down"
                x, y = x + direction[curr_dir][0], y + direction[curr_dir][1] - 1
            if x == len(matrix):
                curr_dir = "left"
                x, y = x + direction[curr_dir][0] - 1, y + direction[curr_dir][1]
            if y < 0:
                curr_dir = "up"
                x, y = x + direction[curr_dir][0], y + direction[curr_dir][1] + 1
            
            if matrix[x][y] == "#":
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
                
            elif matrix[x][y] != "#":
                seen += 1
                spiral.append(matrix[x][y])
                matrix[x][y] = "#"
                x, y = x + direction[curr_dir][0], y + direction[curr_dir][1]
        return spiral
    
#%%
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
ans = Solution()
print (ans.spiralOrder(matrix))
            