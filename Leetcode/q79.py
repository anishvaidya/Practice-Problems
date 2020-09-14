#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:36:55 2020

@author: vanish
"""
#%%
from typing import List
class Solution:
    def dfs(self, i, j, board, c, word):
        # print (word)
        if c == len(word):
            return True
        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == "#"):
            # print ("limits")
            return False
        char = board[i][j]
        # print (char),
        # print (word[c])
        board[i][j] = "#"
        if char == word[c]:
            if (self.dfs(i + 1, j, board, c + 1, word)
            or self.dfs(i - 1, j, board, c + 1, word)
            or self.dfs(i, j + 1, board, c + 1, word)
            or self.dfs(i, j - 1, board, c + 1, word)):
                return True
        board[i][j] = char
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # index = 1
                    yes = self.dfs(i, j, board, 0, word)
                    if yes:
                        return True
                else:
                    continue
        return False
    
#%%
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
word = "SEE"
word = "ABCB"
ans = Solution()
print (ans.exist(board, word))