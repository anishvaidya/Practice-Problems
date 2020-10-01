#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 11:07:07 2020

@author: vanish
"""

from typing import List
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows = len(board)
        columns = len(board[0])
        gonna_crush = False
        
        # check columns
        for c in range(columns):
            for r in range(rows - 2):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -1 * abs(board[r][c])
                    gonna_crush = True
        
        # check rows
        for r in range(rows):
            for c in range(columns - 2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -1 * abs(board[r][c])
                    gonna_crush = True
             
        # crush and gravity
        for c in range(columns):
            wr = rows-1
            for r in range(rows-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0
            
        if gonna_crush:
            return self.candyCrush(board)  
        else: return board          

        
        
        
        
#%%
board = [[110,5,112,113,114],
         [210,211,5,213,214],
         [310,311,3,313,314],
         [410,411,412,5,414],
         [5,1,512,3,3],
         [610,4,1,613,614],
         [710,1,2,713,714],
         [810,1,2,1,1],
         [1,1,2,2,2],
         [4,1,4,4,1014]]

ans = Solution()
print (ans.candyCrush(board))