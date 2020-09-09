#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 12:15:49 2020

@author: vanish
"""

from typing import List
#%%
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        changes = list()
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbor_data = {
                    'live': 0,
                    'dead': 0
                    }
                checks = {(0,1), (0,-1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1,-1)}
                if i == 0:
                    checks.discard((-1, 0))
                    checks.discard((-1, 1))
                    checks.discard((-1, -1))
                if j == 0:
                    checks.discard((0, -1))
                    checks.discard((-1, -1))
                    checks.discard((1, -1))
                if i == (len(board) - 1):
                    checks.discard((1,0))
                    checks.discard((1,-1))
                    checks.discard((1, 1))
                if j == (len(board[0]) - 1):
                    checks.discard((0, 1))
                    checks.discard((-1, 1))
                    checks.discard((1, 1))
                for check in checks:
                    if board[i + check[0]][j + check[1]]:
                        neighbor_data['live'] += 1
                    else:
                        neighbor_data['dead'] += 1
                if board[i][j]:
                    # check live rules
                    if neighbor_data['live'] < 2 or neighbor_data['live'] > 3:
                        changes.append((i, j))
                else:
                    # check dead rules
                    if neighbor_data['live'] == 3:
                        changes.append((i, j))
        for change in changes:
            board[change[0]][change[1]] = int (not board[change[0]][change[1]])
            
        print (board)
        
#%%
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
ans = Solution()
ans.gameOfLife(board)
        
        